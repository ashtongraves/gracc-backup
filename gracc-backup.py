import sys
import tomllib
import os

id = sys.argv[1]

toml_path = f'/etc/graccarchive/config/gracc-archive-{id}.toml'
with open(toml_path, 'rb') as f:
    toml_text = tomllib.load(f)
    output_path = toml_text['Directories']['dest']
input_path = f'/var/lib/graccarchive/{id}/output'
secondary_path = f'/var/lib/graccarchive/{id}/secondary'

for file in os.listdir(os.fsencode(input_path)):
    file_name = os.fsdecode(file)
    if file_name.endswith("tar.gz"):
        file_size = os.stat(input_path + '/' + file_name).st_size
        print(file_size)