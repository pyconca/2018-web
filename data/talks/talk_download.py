# Download/Format talk information.
# warning this is a python-2 only script.

import os
import json
from pathlib import Path
from jinja2 import FileSystemLoader
from jinja2 import Environment
from selenium import webdriver
from talk_ids import TALK_IDS


URL = 'https://www.papercall.io/cfps/1311/submissions/'

URL_LOGIN = 'https://www.papercall.io/signin'

# Template setup
current_folder = Path(__file__).resolve().parent
jinja_env = Environment(
    loader=FileSystemLoader(str(current_folder)),
)
template = jinja_env.get_template('talk_skeleton.j2')

FULL_TAG_LIST = []

BANNED_TAGS = [
    'fa'
]

# import talk data
raw_data = open('pycon_canada_2018_submissions.json').read()
JSON_DATA = json.loads(raw_data)

try:
    os.environ['PATH'] += ':/home/abrahamv/.local/bin'
    user_paths = os.environ['PATH'].split(os.pathsep)
except KeyError:
    user_paths = []

fp = webdriver.FirefoxProfile('/home/abrahamv/.mozilla/firefox/vlizshp8.default')


# Step 1: login to papercall
driver = webdriver.Firefox(fp)
driver.get(URL_LOGIN)
print('browser opened')

# Step 2: login via github
link = driver.find_element_by_link_text('GitHub')
link.click()
print('logging in')

for talk_id in TALK_IDS:
    talk_source = talk_id.split('-')
    if talk_source[0] == 'A':
        print('Talk = ' + talk_id + ' is not on papercall')
        continue
    # Hopefully, means it's a papercall ID
    full_url = URL + talk_source[1]
    # Step 3: Open paper details link
    driver.get(full_url)
    # Step 4: Grab paper title
    temp = driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div[1]/h1")
    talk_title = temp.text
    # Step 5: Scan JSON for talk details
    needed_details = None
    for talk_details in JSON_DATA:
        if talk_details['title'] == talk_title:
            needed_details = talk_details
            break  # break only inner loop?
    if not needed_details:
        print('Cannot find details for talk [' + talk_id + '] = ' + talk_title)
        continue
    # print('details found,')
    # print(needed_details)

    # Step 6: Fill data in YAML file
    filename = str(talk_id) + '.yaml'
    talk_tags = needed_details.get('tags', [])
    for tag in BANNED_TAGS:
        try:
            talk_tags.remove(tag)
        except ValueError:
            pass  # if not found, don't worry
    FULL_TAG_LIST.extend(talk_tags)

    context = {
        'name': needed_details.get('name', '').replace('"', "'"),
        'title': needed_details.get('title', '').replace('"', "'"),
        'abstract': needed_details.get('abstract', '').replace('"', "'"),
        'details': needed_details.get('description', '').replace('"', "'"),
        'talk_tags': talk_tags,
    }
    with open(Path(current_folder, filename), 'w') as text_file:
        text_file.write(template.render(context))
    print('Auto-filled [{}]'.format(filename))


print('script over')
all_tags = set(FULL_TAG_LIST)
print('tags = ' + str(all_tags))
quit()
