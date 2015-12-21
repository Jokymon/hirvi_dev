import hi_config
import sys
import pip
import os, os.path
import tarfile, zipfile
import tempfile


ScriptPath = os.path.dirname(__file__)
SourcePath = os.path.join(ScriptPath, "..", hi_config.src_dir)
EnvPath = os.path.abspath(os.environ["ENVIRONMENT_DIR"])

PyvfsRepoPath = "https://github.com/Jokymon/pyvirtualfs.git"
HirviRepoPath = "https://github.com/Jokymon/hirvi.git"
IzanagiRepoPath = "https://github.com/Jokymon/izanagi.git"

LlvmDownloadPath = "http://repo.continuum.io/pkgs/free/win-64/llvm-3.3-0.tar.bz2"
LlvmpyDownloadPath = "http://repo.continuum.io/pkgs/free/win-64/llvmpy-0.12.7-py34_0.tar.bz2"
BinutilsDownloadPath = "https://www.dropbox.com/sh/zfdfr8j9xrax0uw/AABLLR_71Jwpisx2A2C3ONBra?dl=0"
BochsDownloadPath = "http://downloads.sourceforge.net/project/bochs/bochs/2.6.8/Bochs-2.6.8.exe?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fbochs%2Ffiles%2Fbochs%2F2.6.8%2F"


def install_binutils():
    temp = tempfile.TemporaryDirectory()
    curdir = os.getcwd()
    os.chdir(temp.name)
    print("Creating temporary dir: %s" % temp.name)
    import wget
    wget.download(BinutilsDownloadPath, out="binutils.zip", bar=None)
    #f = zipfile.ZipFile("binutils.zip", "r")
    #f.extractall()
    #f.close()


def install_pyvfs():
    if not os.path.exists(SourcePath):
        os.mkdir(SourcePath)
    os.chdir(SourcePath)
    if not os.path.exists("pyvirtualfs"):
        os.system("git clone %s" % PyvfsRepoPath)
    pip.main(['install', '-e', os.path.join(SourcePath, "pyvirtualfs")])


def install_hirvi():
    os.chdir(SourcePath)
    if not os.path.exists("hirvi"):
        os.system("git clone %s" % HirviRepoPath)


def install_izanagi():
    os.chdir(SourcePath)
    if not os.path.exists("izanagi"):
        os.system("git clone %s" % IzanagiRepoPath)


def install_llvm():
    # download binutils, llvm, llvmpy
    # p = urlparse(LlvmDownloadPath)
    # import wget
    # wget.download(LlvmDownloadPath, os.path.basename(LlvmDownloadPath))
    # f = tarfile.open(os.path.basename(LlvmDownloadPath), "r:bz2")
    # f.extractall(targetdirectory)
    # f.close()
    #hi.main(['untar'], "llvm-3.3.0.tar.bz2")
    pass


def install_bochs():
    #temp = tempfile.TemporaryDirectory()
    #temp_dir = temp.name
    temp_dir = tempfile.mkdtemp()
    import wget
    download_path = os.path.join(temp_dir, "bochs.zip")
    wget.download(BochsDownloadPath, out=download_path, bar=None)
    
    target_path = os.path.join(EnvPath, "bochs")
    f = zipfile.ZipFile(download_path, "r")
    f.extract(path=target_path)
    f.close()


def main(args):
    pip.main(['install', "wget"])
    pip.main(['install', "binstruct"])
    #pip.main(['install', "pyvirtualfs"])
    #install_binutils()
    #install_llvm()
    install_bochs()
    install_pyvfs()
    install_hirvi()
    install_izanagi()
    return 0

if __name__=="__main__":
    sys.exit(main(sys.argv))
