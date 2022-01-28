#!usrbinpython
# run by crontab
# removes any files in logs older than 10 days

import os, sys, time
from subprocess import call

def get_file_directory(file)
    return os.path.dirname(os.path.abspath(file))

now = time.time()
cutoff = now - (10  86400)

files = os.listdir(os.path.join(get_file_directory(__file__), logs))
file_path = os.path.join(get_file_directory(__file__), logs)
for xfile in files
    if os.path.isfile(str(file_path) + xfile)
        t = os.stat(str(file_path) + xfile)
        c = t.st_ctime

        # delete file if older than 10 days
        if c  cutoff
            os.remove(str(file_path) + xfile)


