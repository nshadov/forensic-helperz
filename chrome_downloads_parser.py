#!/usr/bin/env python

import sys
import csv
import sqlite3
from datetime import datetime, timedelta

def convert_timestamp(ts):
    return str(datetime(1601,1,1)+timedelta(microseconds=int(ts)))

def usage():
    print "USAGE: %s <Chrome_Installation_Path>/Chrome/<Profile_Name>/History" % sys.argv[0]
    print "\tPath to profile you could find here: https://support.google.com/chrome/answer/142059?hl=en"
    sys.exit(0)
    
def main():
    if len(sys.argv) < 2: usage()
    
    conn = sqlite3.connect(sys.argv[1])
    c = conn.cursor()
    for row in c.execute("SELECT id,current_path,start_time,received_bytes,state,opened,referrer,mime_type,tab_url,site_url FROM downloads ORDER BY start_time"):
        (id,path,time,bytes,state,opened,referrer,mime,tab,site) = row
        time = convert_timestamp(time)
        id = str(id)
        print "%s %s %s %s %s %s %s %s" % (id, time, bytes, "downloaded" if state == 1 else "aborted", "opened" if opened == 1 else "not-opened", mime, referrer, path)

if __name__ == "__main__":
    main()
