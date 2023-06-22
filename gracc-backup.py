import sys
import tomllib
import os
import subprocess
import re

id = sys.argv[1]

toml_path = f'/etc/graccarchive/config/gracc-archive-{id}.toml'
with open(toml_path, 'rb') as f:
    toml_text = tomllib.load(f)
    output_path = toml_text['Directories']['dest']
input_path = f'/var/lib/graccarchive/{id}/output'
secondary_path = f'/var/lib/graccarchive/{id}/secondary'

for file in os.listdir(os.fsencode(input_path)):
    file_name = os.fsdecode(file)
    file_full_path = input_path + '/' + file_name
    file_size = os.stat(file_full_path).st_size
    if file_size == 0 or not file_name.endswith('tar.gz'):
        pass
    elif file_size < 300:
        os.remove(file_full_path)
    else:
        os.environ['X509_USER_CERT'] = '/etc/grid-security/backup-cert/gracc.opensciencegrid.org-cert.pem'
        os.environ['X509_USER_KEY'] = '/etc/grid-security/backup-cert/gracc.opensciencegrid.org-key.pem'
        local_full_path = "file://" + file_full_path
        remote_full_path = output_path + file_name
        print(subprocess.check_output(f'gfal-copy {local_full_path} {remote_full_path}', shell=True))
        unformatted_remote_checksum = subprocess.check_output(f'gfal-sum -v {remote_full_path} MD5', shell=True).decode('utf-8')
        remote_checksum = re.findall('.+ (.+)\\n', unformatted_remote_checksum)[0]
        unformatted_local_checksum = subprocess.check_output(f'gfal-sum -v {file_full_path} MD5', shell=True).decode('utf-8')
        local_checksum = re.findall('.+ (.+)\\n', unformatted_local_checksum)[0]
        print(remote_checksum == local_checksum)