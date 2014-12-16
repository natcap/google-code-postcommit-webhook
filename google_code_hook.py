#!/usr/bin/python
import cgi

import cgitb
cgitb.enable(display=0, logdir="/usr/local/natcap-webserver-data/post_commit_hook/cgi-bin/google-code-postcommit-webhook")

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers

form = cgi.FieldStorage()
print form["key1"]
#cgi.test()

