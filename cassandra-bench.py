#!/usr/bin/env python
# encoding: utf-8
"""
cassandra-bench.py

Created by Ryan Svihla on 2009-10-01.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import sys
import getopt
import cassandrabench.bench as b

help_message = '''
usage: cassandra-bench.py -s="server" -t="thread count" -r="html"|"xml" -o="File Location"
'''


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "ho:v", ["help", "server=","threads=","report=","output="])
        except getopt.error, msg:
            raise Usage(msg)
        
        threads = 50
        reporttype = ""
        output = ""
        server ="127.0.0.1:9160"
        # option processing
        for option, value in opts:
            if option == "-v":
                verbose = True
            if option in ("-s", "--server"):
                server = value
            if option in ("-h", "--help"):
                raise Usage(help_message)
            if option in ("-o", "--output"):
                output = value
            if option in ("-r", "--report"):
                reporttype = value
            if option in ("-t", "--threads"):
                threads = int(value)
        b.run(server, threads, reporttype, output)
        
    except Usage, err:
        print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
        print >> sys.stderr, "\t for help use --help"
        return 2


if __name__ == "__main__":
    sys.exit(main())
