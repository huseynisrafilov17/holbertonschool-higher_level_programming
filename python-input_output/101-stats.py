#!/usr/bin/python3
'''
Documentation
'''

if __name__ == "__main__":
    import sys
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                    "404": 0, "405": 0, "500": 0}
    file_size = 0
    count = 0
    same = False
    while True:
        try:
            string = input()
            x = string.split()
            for j in x:
                if j.isdigit() and j in status_codes.keys() and same == False:
                    status_codes[j] += 1
                    same = True
                elif j.isdigit():
                    file_size += int(j)
            same = False
            count += 1
            if count == 10:
                print("File size: {}".format(file_size))
                for i in status_codes.keys():
                    if status_codes[i] > 0:
                        print("{}: {}".format(i, status_codes[i]))
                count = 0
        except (KeyboardInterrupt, EOFError):
            print("File size: {}".format(file_size))
            for i in status_codes.keys():
                if status_codes[i] > 0:
                    print("{}: {}".format(i, status_codes[i]))
            break
