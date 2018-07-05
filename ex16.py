# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 11:48:22 2018

@author: George
"""

# afta ine tests

from sys import argv

script, filename = argv

print "we are going to erase %r," % filename
print "if you don't want that, hit CTRL-C" 
print "if you do want that, hit RETURN"

raw_input("?")

print "opening the file..."
target = open(filename,'w')
print "truncating the file. Goodbye"
target.truncate()

print "now I am going to ask you for three lines"

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "I am going to write there to the file"

target.write(line1)
target.wrtie("\n")
target.write(line2)
target.wrtie("\n")
target.write(line2)
target.wrtie("\n")

print "and finally, we close it"
target.close()