import re

s = 'name @ domain1 .domain2.domain3.com'

m = re.match(r'([A-Za-z0-9]+)\s*@\s*(\s*(?:[A-Za-z0-9\s.-]+)\s*\.?\s*)+', s)
print m.groups()
