import os

FindFile = "Приказ"
path ="C:/"

filelist = []

for root, dirs, files in os.walk(path):
    for file in files:
        FullPath = os.path.join(root,file)
        #filelist.append(FullPath)
        if (FullPath.find(FindFile) != -1):
            print(FullPath)


"""
for name in filelist:
    print(name)
"""

input("press any key")
