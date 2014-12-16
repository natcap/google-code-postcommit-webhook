#!/usr/bin/python
import cgi

import cgitb
cgitb.enable(display=0, logdir="/usr/local/natcap-webserver-data/post_commit_hook/cgi-bin/google-code-postcommit-webhook")

cgi.test()

