#!/usr/bin/python3
'''
Documentation
'''


import sys
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0,
                "405": 0, "500": 0}
file_size = 0
count = 0
while True:
    try:
        string = input()
        x = string.split()
        file_size += int(x[8])
        status_codes[x[7]] += 1
        count += 1
        if count == 10:
            print("File size: {}".format(file_size))
            for i in status_codes.keys():
                if status_codes[i] > 0:
                    print("{}: {}".format(i, status_codes[i]))
            count = 0
    except KeyboardInterrupt:
        print("File size: {}".format(file_size))
        for i in status_codes.keys():
            if status_codes[i] > 0:
                print("{}: {}".format(i, status_codes[i]))
        break
