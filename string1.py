#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic string exercises
import sys
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in string2.py.


# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
def donuts(count):
  if count >= 10:
    x = "many"
  else:
    x = str(count)
  return "Number of donuts: " + x


# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
  if len(s) < 2:
    return ""
  else:
    return s[0:2]+s[len(s)-2:len(s)]



# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s):
# I applied two different methods. method 1 is looping through the individual characters
# and creates a new string during this progress. I then return the new string
#  occ = s[0]               # make a variable with the first character of string s
#  strb = ""                # make sure to start with a new empty string (strb) 
#  for i in s:              # for every character(i) in string s
#    if i != occ:           # if the current character i is not equal to the first character occ
#      strb = strb + i      # then add the current character to the new string (strb)
#    elif len(strb) == 0:   # if the first if isn't TRUE and the length of strb is 0 then
#      strb = strb + i      # Then add the current character to string b (strb)
#    else:                  # The only character left is the character which is the same as occ, but not on position 1. We replace that by *
#      strb = strb + "*"    # We then add the * to string b (strb)
#  return strb              # we return the newly made str

#For the second method I define the first character of the string. Then I replace all
#the characters which are equal to the first with * (including the 1st character)
# Lastly I make string y by adding up the first character with the replaced string
# However, I cut the string so the first character does not come through. 
  occ = s[0]                #make a variable with the first character of string s
  x = s.replace(occ,"*")    #replace all the characters in s which are equal to occ with * and store this in variable x
  y = occ + x[1:len(x)]     # make a new variable y with is the first character occ + the string of the previous strip without it's first character
  return y                  # return the the string y

# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
  first_char_a = a[0:2]                                 # Store the first 2 values of string a
  first_char_b = b[0:2]                                 # Store the first 2 values of string b
  first_string = a.replace(first_char_a,first_char_b)   # Replace the first 2 characters of string a(first_char_a) by the first characters of b (first_char_b)
  second_string = b.replace(first_char_b,first_char_a)  # Do the same for the second string
  added_strings = first_string + " " + second_string    # Concatenate the replaced strings with a space inbetween
  return added_strings                                  # return the result of the concatenation


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print donuts
  # Each line calls donuts, compares its result to the expected for that call.
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')

  print
  print 'both_ends'
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends('a'), '')
  test(both_ends('xyz'), 'xyyz')

  
  print
  print 'fix_start'
  test(fix_start('babble'), 'ba**le')
  test(fix_start('aardvark'), 'a*rdv*rk')
  test(fix_start('google'), 'goo*le')
  test(fix_start('donut'), 'donut')

  print
  print 'mix_up'
  test(mix_up('mix', 'pod'), 'pox mid')
  test(mix_up('dog', 'dinner'), 'dig donner')
  test(mix_up('gnash', 'sport'), 'spash gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
1
