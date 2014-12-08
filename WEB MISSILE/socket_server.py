#!/usr/bin/python
# -*- coding: cp1252 -*-
"""
VII Pylestras - Diversão e lucro com Raspberry Pi
dezembro de 2014
"""
import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 8888)
print >>sys.stderr, 'Iniciando servidor %s porta: %s' % server_address
sock.bind(server_address)

while True:
    print >>sys.stderr, '\nAguardando comando...'
    data, address = sock.recvfrom(8888)
    #DEBUG
    print >>sys.stderr, 'recebido %s bytes de %s' % (len(data), address)
    print >>sys.stderr, data
    
