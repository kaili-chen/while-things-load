from ics import Calendar, Event
import json

def export_ics(cal, filename):
    with open(filename, 'w') as f:
        f.writelines(cal)
    f.close()
    return filename

wish_events = json.load(open('04 ics file/data/wishes_detailed_20211103210903.json', 'r'))

cal = Calendar()

for we in wish_events:
    if we['end_date'] != "" and we['end_time'] != "":
        start_dt = '{}T{}+08:00'.format(we['start_date'], we['start_time'])
        end_dt = '{}T{}+08:00'.format(we['end_date'], we['end_time'])
        boosted_rates = [i['title'] for i in we['drop_rate_boosted']]
        event_title = '{} ({})'.format(we['title'], ', '.join(boosted_rates))
        event = Event(name=event_title, begin=start_dt, end=end_dt, description=we['type'])
        cal.events.add(event)

export_ics(cal, 'genshin_banners.ics')
# print(cal.events)