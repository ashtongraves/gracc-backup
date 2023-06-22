import sys
import tomllib
import os
import subprocess

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
        os.remove(file)
    else:
        os.environ['X509_USER_CERT'] = '/etc/grid-security/backup-cert/gracc.opensciencegrid.org-cert.pem'
        os.environ['X509_USER_KEY'] = '/etc/grid-security/backup-cert/gracc.opensciencegrid.org-key.pem'
        local_full_path = "file://" + file_full_path
        remote_full_path = output_path + file_name
        print(subprocess.check_output(f'gfal-copy {local_full_path} {remote_full_path}', shell=True))
        remote_checksum = subprocess.check_output(f'gfal-sum {remote_full_path} MD5', shell=True)
        local_checksum = subprocess.check_output(f'gfal-sum {file_full_path} MD5', shell=True)
        print(remote_checksum == local_checksum)