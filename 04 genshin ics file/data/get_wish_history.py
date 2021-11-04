import scrap
import json
from datetime import datetime
import os
import re

URL = 'https://genshin-impact.fandom.com/wiki/Wishes/History'

# visual studio may not run from where file dir is
cur_dir = os.path.dirname(os.path.realpath(__file__))

# check if there a wish_hisory file in this dir already
wish_history_files = [file for file in os.listdir(cur_dir) if re.match(r'wish_history_[0-9_]*\.html', file)]
if len(wish_history_files) < 1:
    filename = scrap.save_site_html(URL)
else:
    filename = wish_history_files[0]
filename = os.path.join(cur_dir, filename)
# filename = '04 ics file/data/wish_history_20211102_1951.html'

soup = scrap.get_soup(filename=filename)
all_wishes_span = soup.find(id='All_Wishes')

wishes_table = all_wishes_span.parent.findNext('table')
table_rows = wishes_table.find_all('tr')
# headers = table_rows[0]
headers = ['image', 'name', 'start', 'end']
wish_rows = table_rows[1:]
wish_history = []
for wr in wish_rows:
    wish_data = wr.find_all('td')
    
    # IMAGE
    image = wish_data[0].find('img')
    image_attrs = image.attrs
    if 'data-src' in image_attrs.keys():
        image_src = image_attrs['data-src']
    elif 'src' in image_attrs.keys():
        image_src = image_attrs['src']
    
    # NAME
    name_cell = wish_data[1].find('a')
    link = name_cell.attrs['href']
    name = name_cell.attrs['title']
    if name.find('/') > -1:
        name = name[:name.rfind('/')]
    name = name.strip()

    # START DATE/TIME
    start = wish_data[2]
    start = start.attrs['data-sort-value']
    start = start.split(' ')
    start_date = start[0]
    start_time = ''
    if len(start) == 2:
        start_time = start[1]

    # END DATE/TIME
    end = wish_data[3]
    end = end.attrs['data-sort-value']
    end_date = ''
    end_time = ''
    if end != 'none':
        end = end.split(' ')
        end_date = end[0]
        if len(end) == 2:
            end_time = end[1]
    
    wish_history.append({
        'image': image_src,
        'title': name,
        'link': link,
        'start_date': start_date,
        'start_time': start_time,
        'end_date': end_date,
        'end_time': end_time
    })

timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
with open('wish_history_{}.json'.format(timestamp), 'w') as output_file:
    json.dump(wish_history, output_file, indent=4, sort_keys=True)
output_file.close()