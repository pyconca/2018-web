# This is a python script to fill this directory with some dummy talk data

import names
import lipsum
import random
from pathlib import Path
from jinja2 import FileSystemLoader
from jinja2 import Environment
from talk_ids import TALK_IDS

# Basic setup
current_folder = Path(__file__).resolve().parent
jinja_env = Environment(
    loader=FileSystemLoader(str(current_folder)),
)
template = jinja_env.get_template('talk_skeleton.j2')
tag_mandatory = [
    'beginner',
    'intermediate',
    'expert',
]
tag_optional = [
    'python',
    'talk',
]

ID_START = 9001
ID_STOP = 9026

# Loop to create files
# for talk_number in range(ID_START, ID_STOP + 1):
for talk_number in TALK_IDS:
    filename = str(talk_number) + '.yaml'
    title_words = random.randint(4, 12)
    abstract_sentences = random.randint(2, 6)
    details_paras = random.randint(4, 10)

    # Creating the tag list
    tag_list = []
    tag_list.append(random.choice(tag_mandatory))
    random_tags = random.sample(tag_optional, random.randint(0,2))
    tag_list += random_tags

    context = {
        'name': names.get_full_name(),
        'title': lipsum.generate_words(title_words),
        'abstract': lipsum.generate_sentences(abstract_sentences),
        'details': lipsum.generate_paragraphs(details_paras),
        'talk_tags': tag_list,
    }
    with open(Path(current_folder, filename), 'w') as text_file:        
        text_file.write(template.render(context))
    print('Auto-filled [{}]'.format(filename))

print('task completed')
