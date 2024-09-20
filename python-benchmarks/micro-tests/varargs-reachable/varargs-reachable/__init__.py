from urllib3.util import parse_url

def foo(*args):
    for f in args:
        print(f("http://www.google.com"))

foo(parse_url)