from urllib3.util import parse_url

class Foo:
    def __init__(self):
        self._f = None

    @property
    def f(self):
        pass

    @f.setter
    def f(self, value):
        print(value("http://www.google.com"))

Foo().f = parse_url