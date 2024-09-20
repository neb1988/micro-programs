import urllib3.util

funs = [urllib3.util.parse_url]
for f in funs: f("some_url")