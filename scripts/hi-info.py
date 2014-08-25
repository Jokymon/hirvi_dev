import sys


def main():
    print("System setup summary:")
    print("=====================\n")
    print("Python executable: %s" % sys.executable)
    print("Python version:    %s" % sys.version)


if __name__=="__main__":
    sys.exit(main())
