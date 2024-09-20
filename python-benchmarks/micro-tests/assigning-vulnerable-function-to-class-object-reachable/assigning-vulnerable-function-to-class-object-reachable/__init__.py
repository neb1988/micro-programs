import urllib3.util
class O(object): pass

o = O()
o.foo = urllib3.util.parse_url
o.foo("some_url")