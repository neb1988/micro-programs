from typing import Any
from urllib3.util import parse_url
from collections.abc import Callable


class Base1:
    def __init__(self, f: Callable[[str], Any]):
        super().__init__()
        self.g = f

class Base2:
    def __init__(self, f: Callable[[str], Any]):
        super().__init__(lambda x: None)
        self.f = f


class Derived(Base2, Base1):
    def __init__(self):
        super().__init__(parse_url)

    def doit(self, url: str) -> Any:
        return self.f(url)


print(Derived().doit("http://www.google.com"))