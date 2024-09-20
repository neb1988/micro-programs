import urllib3.util
class O(object): pass

class O2(object): pass

o = O()
o.foo = urllib3.util.parse_url

o2 = O2()
o2.foo()
