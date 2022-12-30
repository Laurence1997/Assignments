# Log text file - a text file that can be modified by appending lines to the end of the file.
# Allowed operations:
# Create file
# Delete file
# Move file
# Readfile (returns file content)
# Append a line to the end of the file
import datetime
import os
import shutil

# Create file
logfile= open('test001.txt',"w",encoding='utf-8')
logfile.write('something test')
logfile.write('information retrieval systems\n')
logfile.close()

# Readfile (returns file content)
with open(r'test001.txt',"r",encoding='utf-8') as aa:
 t=aa.readline()
 print(t)
logfile.close()

# Append a line to the end of the file
with open("test001.txt", "a") as bb:
 bb.write("Well Done!\n")


# Move file
shutil.copy("test001.txt","test001.txt.bak") #copy file
shutil.move("test001.txt","movetest001.txt")

# Delete file
os.remove('movetest001.txt')


