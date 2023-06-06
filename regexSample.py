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
mo9 == None


# matching specific repetitions with braces

haRegex = re.compile(r'(Ha){3}')
mo10 = haRegex.search('HaHaHa')
print(mo10.group())


# greedy and non-greedy matching

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo11 = greedyHaRegex.search('HaHaHaHaHa')
print(mo11.group())

nongreedyHaRegex = re.compile(r'(Ha){2,5}?') # note question mark have two meaning optional group or non-greedy match
mo12 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo12.group())


# character classes
#
# \d - any numeric digit 0 - 9
# \D - not a numeric digit from 0 - 9
# \w - word character and underscore
# \W - any character not a word or underscore
# \s - space, tab, or newline
# \S - not a space, tab, or newline

xmasRegex = re.compile(r'\d+\s\w+')
mo13 = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 5 rings')
print(mo13)


# making your own character classes
#
# example: [a-zA-Z0-9] will match all lowercase letters, uppercase, and numbers.
# note: inside the square bracket no need to escape the symbol
# caret character (^) in opening bracket = opposite/negative class


vowelRegex = re.compile(r'[aeiouAEIOU]') # matching all vowel letters
mo14 = vowelRegex.findall('RoboCop eats BABY FOOD.')
print(mo14)


# caret and dollar sign characters (Carrots cost dollars)
#
# ^ at the beginning and $ at the end indicate the string must end with regex pattern

beginsWithHello = re.compile(r'^Hello')
mo15 = beginsWithHello.search('Hello, world')
print(mo15.group())

endsWithNumber = re.compile(r'\d+$')
mo16 = endsWithNumber.search('Your number is 42')
print(mo16.group())


#  wildcard character
#
# . (dot) char = wildcard and will match any character expect for a newline
#

atRegex = re.compile(r'.at')
mo17 = atRegex.findall('The cat in the hat sat on the flat mat')
print(mo17)



# matching everything with Dot-Star


