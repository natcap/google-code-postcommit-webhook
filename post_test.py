import requests

post_url = "http://post_commit.naturalcapitalplatform.org/cgi-bin/google-code-postcommit-webhook/google_code_hook.py"

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post(post_url, data=payload)
print(r.text)
