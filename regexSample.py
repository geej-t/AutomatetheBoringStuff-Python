#! python3


# mo - means matching object

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search('My number is 415-555-4242.')
print(f'Phone number found: {mo.group()}')

# matching mutiple groups with the pipe

heroRegex = re.compile(r'Batman|Tina Fey') # will match either Batman or Tina Fey
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

# optional matching with question

batREgex = re.compile(r'Bat(wo)?man') # match zero or one of the group preceding this questionn mark
mo3 = batREgex.search('The adventure of Batman')
print(mo3.group())

mo4 = batREgex.search('The adventure of Batwoman')
print(mo4.group())

# matching zero or mote with the star

starRegex = re.compile(r'Bat(wo)*man')
mo5 = starRegex.search('The adventures of Batman')
mo6 = starRegex.search('The adventure of Batwowowowoman')
print(mo5.group())
print(mo6.group())

# matching one or more with the plus

plusRegex = re.compile(r'Bat(wo)+man')
mo7 = plusRegex.search('The adventures of Batwoman')
mo8 = plusRegex.search('The adventures of Batwowowoman')
mo9 = plusRegex.search('The adventures of Batman')
print(mo8.group())
print(mo7.group())
print(mo9.group())


# matching specific repetitions with braces






