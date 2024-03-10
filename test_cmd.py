#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    def __init__(self):
        pass

new_cmd = HBNBCommand()
print(new_cmd.__dict__)


if __name__ == '__main__':
    HBNBCommand().cmdloop()