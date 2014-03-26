from nntplib import *

s = NNTP('web.aioe.org')
(resp, count, first, last, name) = s.group('comp.lang.python')
(resp, subs) = s.xhdr('subject', (str(first) + '-' + str(last)))
for subject in subs[-10:]:
    print(subject)
num = input('Which article do you want to read? ')
(response, info) = s.article(str(num))
for line in info.lines:
    print(line)
    
