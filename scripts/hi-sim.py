import sys
import os.path


def main(args):
    script_path = os.path.dirname(__file__)
    bochs_path = os.path.join(script_path, "..", "bochs", "bochs.exe")
    bochs_path = os.path.normpath(bochs_path)
    os.system("start cmd /c %s -q -f izanagi/bochsrc.bxrc" % bochs_path)


if __name__=="__main__":
    sys.exit(main(sys.argv))
