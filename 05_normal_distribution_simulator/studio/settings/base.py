import os.path

#-----------------------------------------------------------------------------
# PROJECT DIRS

# root path
CURRENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

PROJECT_DIR = PROJECT_ROOT 

#-----------------------------------------------------------------------------
# FOLDERS

OUT_DIR = PROJECT_DIR + "/_outputs"


#-----------------------------------------------------------------------------
# FILES

FRAME_FILE = OUT_DIR + "/frames.mp4"
