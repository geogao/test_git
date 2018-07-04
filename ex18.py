# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 12:47:09 2018

@author: George
"""

# this one is like your script with argv

def print_two ( *args ):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
def print_two_again (arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
def print_none():
    print "I an nothing"
    
print_two("zed","show")
print_two_again("zed","show")
print_none()