# -*- coding: utf-8 -*-
"""
Created on Tue Apr 03 11:33:02 2018

@author: George
"""

# re ti travame ke mis i horeftries

print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none
"""

print "--------------------"

print poem

print "--------------------"

five = 10 - 3 + 2 -6 + 2

print "This number should be five: %d" % five


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "we would have %d beans, %d jars and %d crates" % secret_formula(start_point)
    