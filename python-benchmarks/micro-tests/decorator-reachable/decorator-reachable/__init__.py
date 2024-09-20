import urllib3

def decorator(func):
    return urllib3.util.parse_url

@decorator
def say_hello(name):
    print(f"Hello {name}")

say_hello("some-url")
