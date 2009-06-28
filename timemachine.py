#!/usr/bin/env python

import datetime
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
    td = datetime.timedelta(yrs*365 + mths*31 + dys)

    def do_update(td, path, fs):
        for f in fs:
            fp = os.path.join(path, f)
            try:
                ft = datetime.date.fromtimestamp(os.path.getmtime(fp))
                print "Updated timestamp of %s from %d-%d-%d" % (fp, ft.year, ft.month, ft.day),
                t =  ft + td
                print "to %d-%d-%d" % (t.year, t.month, t.day)
                t = time.mktime(t.timetuple())
                os.utime(fp, (t, t))
            except:
                print "Failed update of ", fp
            
        
    os.path.walk(".", do_update, td)

def main():
    yrs = prompt("Delta years?", 0)
    mths = prompt("Delta months?", 0)
    dys = prompt("Delta days?", 0)

    updateTimestamps(yrs, mths, dys)

if __name__ == "__main__":
#    try:
        main()
#    except:
#        print "Something bad happened"
#    finally:
#        raw_input()
