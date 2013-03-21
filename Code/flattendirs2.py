import os

direct=direct='D:\\avatar\\bajados\\'
#direct='C:\Documents and Settings\Mariana\Desktop\linx3\prueba\\'
#rmdir /s /q <dirname>
os.chdir(direct)

directoriosbase=os.listdir(os.getcwd())
for db in directoriosbase:
    direct1=direct+db
    print direct1
    os.chdir(direct1)
    dirint=os.listdir(os.getcwd())
    for dd in dirint:
       newd='rmdir /s /q '+dd
       os.system(newd)

    
