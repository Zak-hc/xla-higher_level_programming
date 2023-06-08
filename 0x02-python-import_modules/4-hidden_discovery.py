#!/usr/bin/python3
import dis
import hidden_4
if __name__ == "__main__":
    names = [name for name in dir(hidden_4)]
    a = len(names)
    for name in names:
        if name == 'my_secret_santa' or name == 'print_hidden':
            print(name)
        elif name == 'print_school':
            print(name)
