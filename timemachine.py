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

def updateTimestamps(yrs, mths, dys):
    mt = (dys*60*60*24) + (mths*30*60*60*24) + (yrs*12*30*60*60*24)

    def do_update(dt, path, fs):
        for f in fs:
            fp = os.path.join(path, f)
            t = os.path.getmtime(fp) + dt
            os.utime(fp, (t, t))
        
    os.path.walk(".", do_update, mt)

def main():
    yrs = prompt("Delta years?", 0)
    mths = prompt("Delta months?", 0)
    dys = prompt("Delta days?", 0)

    updateTimestamps(yrs, mths, dys)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print "Faulted with exception:"
        print e
