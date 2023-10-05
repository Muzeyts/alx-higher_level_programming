#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    salt = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            salt += int(arg)
    print(salt)
