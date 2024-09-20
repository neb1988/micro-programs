import urllib3.util

def call(f): f("some-url")

call(urllib3.util.parse_url)
