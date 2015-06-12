import hi_config
import sys
import pyvirtualfs.pyvfs as pyvfs

def main(args):
    print("Bootloader sources: %s" % hi_config.bootloader_source_dir)
    cmd = pyvfs.PyvfsCommandInterpreter()
    cmd.interprete("create izanagi_hd.img 18M".split())
    cmd.interprete("fdisk create image://izanagi_hd.img:hd/partition0 start=150 end=16550 type=6".split())
    cmd.interprete("mkfs image://izanagi_hd.img:hd/partition0".split())
    cmd.interprete("copy hirvi\kernel.elf image://izanagi_hd.img:hd/partition0/kernel.elf".split())
# TODO: setupmbr call to setup the MBR and install the bootloader in the newly created image

if __name__=="__main__":
    sys.exit(main(sys.argv))
