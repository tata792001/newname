import re
a="1.2.3.123.123.123.23.123.1.2.3"
a=re.findall ('(?:\d?\d?\d\.){3}\d?\d?\d',a)
a=re.findall ('(?:{1-9]|[1-9]|d|1\d\d|2[0-4]\d|25[0-5])(?:\.(?:\d{1-9]d|1\d\d|2[0-4]\d|25[0-5]))',a)


print(a)

import re
a = "1,3,-1, 0.54, -65, 56, 224454 "
a = re.findall('(?: \d [1-9])', a)
print(a)


import re
a = " 56ФИО одощы цвщшз YUO   "
a = re.findall('(?:^| )[А-ЯA-Z]+(?:^| )', a)
print(a)