#!/usr/bin/python
import cgitb
import subprocess
import json
import sys
import os

cgitb.enable(display=0, logdir="/usr/local/natcap-webserver-data/post_commit_hook/cgi-bin/google-code-postcommit-webhook")

print "Content-Type: text/html" # HTML is following
print # blank line, end of headers

data = sys.stdin.read()

repository_dir = os.path.expanduser("~/invest-natcap.webpage/")
with open('post_commit_hooks.txt', 'a') as f:
    f.write(data + '\n')
    f.flush()
    hook_data = json.loads(data)
    f.write(str(hook_data) + '\n')
    f.flush()
    f.write(hook_data["repository_path"] + '\n')
    f.flush()
    if hook_data["repository_path"] == "https://code.google.com/p/invest-natcap.webpage/":
        if not os.path.isdir(repository_dir):
            f.write("cloning\n")
            f.flush()
            subprocess.call(
                ["hg", "clone", hook_data["repository_path"], repository_dir])
        else:
            f.write("pulling\n")
            f.flush()
            subprocess.call(
                ["hg", "pull", "--repository", repository_dir])
        f.write("updating\n")
        f.flush()
        subprocess.call(
            ["hg", "up", "-C",  "--repository", repository_dir])

        f.write("syncing\n")
        f.flush()
        subprocess.call(
            [os.path.join(repository_dir, "sync.sh")])
        f.write("done\n")
