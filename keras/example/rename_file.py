import os

path = '/Users/loctv/Desktop/test'
files = os.listdir(path)

for file in files:
    base = os.path.basename(os.path.join(path, file))
    splitter = os.path.splitext(base)
    basename = splitter[0]
    extension = splitter[1]
    if basename.startswith("IMG_"):
        basename = basename.replace("IMG_","")
        basename = basename + "_IMG"


    if basename.startswith("VID_"):
        basename = basename.replace("VID_", "")
        basename = basename + "_VID"

    os.rename(os.path.join(path, file), os.path.join(path, basename + extension))