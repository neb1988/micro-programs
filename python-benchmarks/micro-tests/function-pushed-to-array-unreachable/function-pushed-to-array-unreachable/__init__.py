import urllib3.util
from typing import Any

from collections.abc import Callable

def identity(x): x  

def add(lib: Any, l: list[Callable[[str], Any]]):
    l.append(identity)

funs = []
add(urllib3.util, funs)
for f in funs: f("some_url")