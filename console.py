#!/usr/bin/python3
""""play with command"""


import cmd


class HBNBCommand(cmd.Cmd):
    """"thw thats is com"""
    prompt = "(hbnb)"
    # def __init__(self):
    #     pass

    def do_EOF(self, line):
        """the last file"""
        return True

    def do_quit(self, line):
        """abort it"""
        return True
    

    def do_help(self, line):
        cmd.Cmd.do_help(self, line)
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()