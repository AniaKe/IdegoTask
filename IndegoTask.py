#!/usr/bin/python

from difflib import SequenceMatcher

str1 = input()
str2 = input()

matcher = SequenceMatcher(None, str1, str2)
result = matcher.find_longest_match()
print(str1[result.a : result.a + result.size])
