import sys
import pip


def main():
    print("System setup summary:")
    print("=====================\n")
    print("Python executable: %s" % sys.executable)
    print("Python version:    %s" % sys.version)
    print("-----------------------------")
    print("Installed packages:")
    pip.main(['list'])
    print("-----------------------------")


if __name__=="__main__":
    sys.exit(main())
