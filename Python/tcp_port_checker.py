#!/usr/bin/env python3
#tcp_port_checker.py

import socket
import re
import sys

def check_server(address, port):
    #create a TCP socket
    s = socket.socket()
    print (f"Attempting to connect to {address} on port {port}")
    try:
        s.connect((address, port))
        print(f"Connected to {address} on port {port}")
        return True
    except socket.error as e:
        print(f"Connection to {address} on port {port} failed: {e}")
        return False


def new_func(parser):
    parser.add_option("-p", "--port", dest="port", type="int", default=443, help="PORT for server", metavar="PORT")

def new_func1(new_func, parser):
    new_func(parser)

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-a", "--address", dest="address", default='localhost', help="ADDRESS for server", metavar="ADDRESS")
    new_func1(new_func, parser)
    (options, args) = parser.parse_args()
    print(f'options: {options}, args:{args}')
    check = check_server(options.address, options.port)
    print(f'check_server returned {check}')
    sys.exit(not check)