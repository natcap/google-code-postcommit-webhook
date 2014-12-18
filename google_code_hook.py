#!/usr/bin/python
"""Module used to process a post commit hook from Google code to
    automatically update a webpage that exists in that repoistory."""

import cgitb
import subprocess
import json
import sys
import os
import time

cgitb.enable(display=0, logdir=".")

print "Content-Type: text/html" # HTML is following
print # blank line, end of headers


REPOSITORY_PATH = "https://code.google.com/p/invest-natcap.webpage/"
REPOSITORY_DIR = os.path.expanduser("~/invest-natcap.webpage/")
with open('post_commit_hooks.log', 'a') as LOG_FILE:
    NULL_FH = open("NUL", "w")
    try:
        HOOK_DATA = json.loads(sys.stdin.read())
        if HOOK_DATA["repository_path"] == REPOSITORY_PATH:
            if not os.path.isdir(REPOSITORY_DIR):
                subprocess.call(
                    ["hg", "clone", HOOK_DATA["repository_path"], REPOSITORY_DIR],
                    stdout=NULL_FH, stderr=NULL_FH)
            else:
                subprocess.call(
                    ["hg", "pull", "--repository", REPOSITORY_DIR],
                    stdout=NULL_FH, stderr=NULL_FH)
            subprocess.call(
                ["hg", "up", "-C", "--repository", REPOSITORY_DIR],
                stdout=NULL_FH, stderr=NULL_FH)
            subprocess.call(
                [os.path.join(REPOSITORY_DIR, "sync.sh")])
            LOG_FILE.write("[%s] successfuly updated\n" % time.strftime("%c"))

    except Exception as exception:
        LOG_FILE.write(
            "[%s] Exception\n%s\n" % (time.strftime("%c"), str(exception)))
        LOG_FILE.flush()
    NULL_FH.close()
