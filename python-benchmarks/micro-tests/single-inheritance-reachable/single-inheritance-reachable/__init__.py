from typing import Any
from urllib3.util import parse_url
from collections.abc import Callable


class Base:
    def __init__(self, f: Callable[[str], Any]):
        self.f = f


class Derived(Base):
    def __init__(self):
        super().__init__(parse_url)

    def doit(self, url: str) -> Any:
        return self.f(url)


print(Derived().doit("http://www.google.com"))