#!/usr/bin/env python

import os
import os.path
import time

def prompt(msg, dflt):
    while True:
        print msg, " ["+str(dflt)+"]",
        try:
            r = raw_input()
            if len(r) == 0:
                return dflt
            else:
                return int(r)
        except ValueError:
            print "That doesn't look like a number."

def updateTimestamps(d):
    for f in os.listdir("."):
        ot = time.localtime(os.path.getmtime(f))
        nt = ()
        print dt

def main():
    yrs = prompt("Delta years?", 0)
    mths = prompt("Delta months?", 0)
    dys = prompt("Delta days?", 0)
    hrs = prompt("Delta hours?", 0)
    mins = prompt("Delta minutes?", 0)

    updateTimestamps((yrs, mths, dys, hrs, mins, 0, 0, 0, 0))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print "Faulted with exception:"
        print e
