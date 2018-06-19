#!/usr/bin/env python2.7
# -*- coding: utf_8 -*-

import serial
  
ser = serial.Serial('/dev/ttyUSB0', 9600, bytesize=8, parity='N', stopbits=1, timeout=1)
  
  
def main():
    while True:
        s = ser.readline()
        if s == b'GETSTATUS\r':
            print(s)
        else:
            print('TIMEOUT')
  
  
if __name__ == "__main__":
    main()