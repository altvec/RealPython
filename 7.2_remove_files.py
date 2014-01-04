'''
Task description:
=================

Write a script "remove_files.py" that will look in the chapter 7
practices files folder named "little pics" as well all of its subfolders.
The script should use os.remove() to delete any JPG file found in any of
these folders if the file is less than 2 Kb (2,000 bytes) in size.

You can supply the os.path.getsize() function with a full file path to
return the file's size in bytes. Check the contents of the folders before
running your script to make sure that you delete the correct files;
you should only end up removing the files named "to be deleted.jpg" and
"definitely has to go.jpg" - although you should only use the file
extensions and file sizes to determine this.

If you mess up and delete the wrong files, there is a folder named
"backup" that contains an exact copy of the "little pics" folder and all
its contents so that you can copy these contents back and try again.


Actually, you should recreate directories structure to get this work:

/Users/srg/practice_files/little pics
.
├── better\ not\ delete\ me.txt
├── look\ in\ here\ too
│   └── definitely\ has\ to\ go.jpg
├── save\ me\ please.jpg
└── to\ be\ deleted.jpg
'''

import os

_Path = "/Users/srg/practice_files/little pics"

for currentFolder, subfolders, fileNames in os.walk(_Path):
    for fileName in fileNames:
        fileFullPath = os.path.join(currentFolder, fileName)
        if fileName.lower().endswith(".jpg"):
            if os.path.getsize(fileFullPath) < 2000:
                os.remove(fileFullPath)
