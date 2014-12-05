#!/usr/bin/python
# -*- coding: cp1252 -*-
"""
WEB MISSILE
VII Pylestras - Diversão e lucro com Raspberry Pi
Based on https://github.com/codedance/Retaliation
"""
import socket
import sys
import platform
import time
import usb.core
import usb.util


class WebMissile(object):

    DOWN  = 0x01
    UP    = 0x02
    LEFT  = 0x04
    RIGHT = 0x08
    FIRE  = 0x10
    STOP  = 0x20

    DEVICE_ORIGINAL = 'Original'
    DEVICE_THUNDER  = 'Thunder'

    def __init__(self):
        self._get_device()
        self._detach_hid()
        self.DEVICE.set_configuration()

    def _get_device(self):
        self.DEVICE = usb.core.find(idVendor=0x2123, idProduct=0x1010)
        if self.DEVICE is None:
            self.DEVICE = usb.core.find(idVendor=0x0a81, idProduct=0x0701)
            if self.DEVICE is None:
                raise ValueError('Missile device not found')
            else:
                self.DEVICE_TYPE = self.DEVICE_ORIGINAL
        else:
            self.DEVICE_TYPE = self.DEVICE_THUNDER

    def _detach_hid(self):
        if "Linux" == platform.system():
            try:
                self.DEVICE.detach_kernel_driver(0)
            except Exception, e:
                pass

    def send_cmd(self, cmd):
        if self.DEVICE_THUNDER == self.DEVICE_TYPE:
            self.DEVICE.ctrl_transfer(0x21, 0x09, 0, 0,
                                      [0x02, cmd, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        elif self.DEVICE_ORIGINAL == self.DEVICE_TYPE:
            self.DEVICE.ctrl_transfer(0x21, 0x09, 0x0200, 0,
                                      [cmd])

    def send_move(self, cmd, duration_ms):
        self.send_cmd(cmd)
        time.sleep(duration_ms / 1000.0)
        self.send_cmd(self.STOP)


instance = WebMissile()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 8888)
print >>sys.stderr, 'Iniciando web missile [%s] porta: %s' % server_address
sock.bind(server_address)

while True:
    data, address = sock.recvfrom(8888)
    
    #print >>sys.stderr, 'recebido %s bytes de %s' % (len(data), address)
    #print >>sys.stderr, data
    
    if data=="38": #cima
    	instance.send_move(instance.UP,100)

    if data=="40": #baixo
    	instance.send_move(instance.DOWN,100)

    if data=="37": #esquerda
    	instance.send_move(instance.LEFT,100)

    if data=="39": #direita
    	instance.send_move(instance.RIGHT,100)

    if data=="13": #enter (atirar)
    	instance.send_cmd(instance.FIRE)

