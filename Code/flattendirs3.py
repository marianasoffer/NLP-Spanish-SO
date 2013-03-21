import os

direct='D:\\avatar\\bajados\\'
os.chdir(direct)

directoriosbase=os.listdir(os.getcwd())
for db in directoriosbase:
    direct1=direct+db
    print direct1
    os.chdir(direct1)
    i=0
    for root, dirs, files in os.walk(os.getcwd()):
        files1=files
        os.chdir(root)
        for j in range(len(files1)):
            i=i+1
            newf=str(i)+files1[j]
            os.renames(files1[j],newf)
        newd='move *.* \"'+direct1+'\"'
        print newd
        print os.getcwd()
        os.system(newd)
    
