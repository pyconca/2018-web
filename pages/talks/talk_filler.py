# This is a python script to fill this directory with skeleton data
# for nikola to create the related detail pages

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

ID_START = 9001
ID_STOP = 9026

# Loop to create files
# for talk_number in range(ID_START, ID_STOP + 1):
for talk_number in TALK_IDS:
    filename = str(talk_number) + '.rst'

    context = {
        'talk_number': str(talk_number),
    }
    with open(Path(current_folder, filename), 'w') as text_file:        
        text_file.write(template.render(context))
    print('Auto-filled [{}]'.format(filename))

print('task completed')
