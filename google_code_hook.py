#!/usr/bin/python
import cgi

import cgitb
cgitb.enable(display=0, logdir="/usr/local/natcap-webserver-data/post_commit_hook/cgi-bin/google-code-postcommit-webhook")

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers

form = cgi.FieldStorage()
with open('post_commit_hooks.txt', 'a') as f:
	f.write(form)
	f.write('\n')


#print form["key1"].value
#cgi.test()

