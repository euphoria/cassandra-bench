#!/usr/bin/env python
# encoding: utf-8
"""
client.py

Created by Ryan Svihla on 2009-10-01.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift.transport import THttpClient
from thrift.protocol import TBinaryProtocol
import Cassandra

def client_connect(host='127.0.0.1', port=9160):
    socket = TSocket.TSocket(host, port)
    transport = TTransport.TBufferedTransport(socket)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Cassandra.Client(protocol)
    client.transport = transport
    return client




