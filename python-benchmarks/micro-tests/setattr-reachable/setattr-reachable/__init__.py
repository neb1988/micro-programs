from __future__ import annotations
from urllib3.util import parse_url

class Foo:
    def __setattr__(self, name: str, value: Any, /) -> None:
        print(value("http://www.google.com"))

Foo().f = parse_url