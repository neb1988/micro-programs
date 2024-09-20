from urllib3.util import parse_url

class Desc:
    def __set__(self, obj, value):
        print(value("http://www.google.com"))

class Foo:
    f = Desc()

Foo().f = parse_url