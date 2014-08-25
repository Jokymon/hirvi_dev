import sys
import os
import os.path


def show_help():
    help_text="""
usage: hi <command> [<args>]

The most commonly used hi commands are:
init        Download, install and setup the tools needed for development
test        Run unit tests

'hi help -a' lists available subcommands. See 'hi help <command>' to read about
a specific subcommand.
"""
    print(help_text)


# Tests:
# 'hi' --> print help, error code = 1
# 'hi unknown-command' --> short error message, error code = 1
# 'hi help' --> print help, error code = 0


def main():
    script_dir = os.path.dirname(sys.argv[0])
    if len(sys.argv)>=2:
        command = sys.argv[1]
        if command=="help":
            show_help()
            return 0
        command_script = "hi-%s.py" % command
        if command_script in os.listdir(script_dir):
            script_path = os.path.join(script_dir, command_script)
            args = " ".join(sys.argv[2:])
            return os.system("%s %s %s" % (sys.executable, script_path, args))
        else:
            print("hi: '%s' is not a hi command. See 'hi --help'." % command)
            return 1
    else:
        show_help()
        return 1

if __name__=="__main__":
    sys.exit(main())
