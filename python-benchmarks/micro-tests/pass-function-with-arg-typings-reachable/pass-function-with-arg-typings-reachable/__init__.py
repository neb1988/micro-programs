import urllib3.util

def identity(x): x  

f = urllib3.util.parse_url if True else identity

f('some-url')
