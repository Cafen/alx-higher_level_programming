#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_len = len(argv) - 1
    if arg_len == 1:
        print("0 arguments.")
    elif arg_len == 2:
        print("{} argument:".format(arg_len))
        print("{}: {}".format(arg_len, argv[1]))
    elif arg_len > 2:
        print("{} arguments:".format(arg_len))
        for i in range(1, arg_len + 1):
            print("{}: {}".format(i, argv[i]))
