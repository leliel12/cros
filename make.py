
import os
import shlex
import subprocess

from lib import DocumentConverter

#===============================================================================
# CONSTANS
#===============================================================================

INCLUDE = (
    "cros",
    
)

TAGS = ".hgtags"

OUT = "dist"

BUILD = "build"


#===============================================================================
# INTERNAL
#===============================================================================

PATH = os.path.abspath(os.path.dirname(__file__))

INCLUDE_PATHS = map(lambda i: os.path.join(PATH, i), INCLUDE)

TAG = "HG"

if os.path.isfile(os.path.join(PATH, TAGS)):
    with open(os.path.join(PATH, TAGS)) as f:
        tags = f.read().splitlines()
        if tags:
            tag = tags[-1].strip()
            if tag:
                tag.split()[-1]
                TAG = tag if tag else TAG

OUT_PATH = os.path.join(PATH, OUT)

BUILD_PATH = os.path.join(PATH, BUILD)


#===============================================================================
# FUNCTIONS
#===============================================================================

def start_oo_service():
    cmd = ['ooffice', '-accept="socket,port=8100;urp;"']
    return subprocess.Popen(cmd)
    

