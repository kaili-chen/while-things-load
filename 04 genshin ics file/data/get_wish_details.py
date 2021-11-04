'''pretty hardcoded'''
import scrap
import json
from datetime import datetime
import os
import re

BASE_URL = 'https://genshin-impact.fandom.com'

# visual studio may not run from where file dir is
cur_dir = os.path.dirname(os.path.realpath(__file__))

# check if there a wish_hisory file in this dir already
wish_history_files = [file for file in os.listdir(cur_dir) if re.match(r'wish_history_[0-9_]*\.json', file)]
filename = os.path.join(cur_dir, wish_history_files[0])
wish_history = json.load(open(filename, 'r'))

detailed_banner_items = []
for wh in wish_history:
    try:
        wish_link = '{}{}'.format(BASE_URL, wh['link'])
        print(wish_link)
        # save_filename = scrap.save_site_html(url=wish_link, filename='04 ics file/data/temp/{}_{}.html'.format(wh['title'], wh['start_date']))
        filename = '04 ics file/data/temp/{}_{}.html'.format(wh['title'], wh['start_date'])
        soup = scrap.get_soup(filename=filename)
        # table has some 2 rows - 1 header, 1 content
        promo_header_span = soup.find(id='Promoted_or_Featured_with_a_Drop-Rate_Boost')
        promoted_table = promo_header_span.parent.findNext('table')
        promoted_table_rows = promoted_table.find_all('tr')
        promoted = promoted_table_rows[1]
        banner_type = promoted.find('th').find('a')['title']
        drop_rate_boost = []
        if banner_type == 'Weapons':
            items = promoted.find('td').find_all('div', {'class': 'card_caption'})
            for item in items:
                item_a = item.find('a')
                item_title = item_a['title']
                item_link = item_a['href']
                drop_rate_boost.append({
                    'title': item_title,
                    'link': item_link
                })
        elif banner_type == 'Characters':
            charas = promoted.find('td').find_all('div', {'class': 'card_container'})
            for chara in charas:
                chara_name = chara.find('div', {'class': 'card_text'})
                chara_name = chara_name.text.strip()
                chara_link = chara.find('div', {'class': 'card_image'})
                chara_link = chara_link.find('a')['href']
                drop_rate_boost.append({
                    'title': chara_name,
                    'link': chara_link
                })
        wh.update({
            'type': banner_type,
            'drop_rate_boosted': drop_rate_boost
        })
        detailed_banner_items.append(wh)
    except:
        continue

timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
with open('wishes_detailed_{}.json'.format(timestamp), 'w') as output_file:
    json.dump(detailed_banner_items, output_file, indent=4, sort_keys=True)
output_file.close()
