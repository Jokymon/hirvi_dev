import sys
import os
import os.path


script_dir = os.path.dirname(sys.argv[0])


def show_help(arguments=None):
    help_text="""
usage: hi <command> [<args>]

The most commonly used hi commands are:
init        Download, install and setup the tools needed for development
test        Run unit tests

'hi help -a' lists available subcommands. See 'hi help <command>' to read about
a specific subcommand.
"""
    def is_a_command(script_name):
        if script_name.startswith("hi-") and script_name.endswith(".py"):
            return True
        return False

    if arguments:
        if "-a" in arguments:
            print("Known 'hi' sub commands:")
            scripts = os.listdir(script_dir)
            scripts = filter(is_a_command, scripts)
            for script in scripts:
                print("    %s" % script[3:-3])
    else:
        print(help_text)


# Tests:
# 'hi' --> print help, error code = 1
# 'hi unknown-command' --> short error message, error code = 1
# 'hi help' --> print help, error code = 0


def main():
    if len(sys.argv)>=2:
        command = sys.argv[1]
        if command=="help":
            show_help(sys.argv[2:])
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
