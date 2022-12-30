
# Directory - can contain other directories and files. Directory can be empty or can have some elements. Number of elements in the directory should be <= DIR_MAX_ELEMS
# Allowed operations:
# Create directory
# Delete directory
# List files and subdirectories
# Move file or subdirectory to another location



# Create directory
#coding:utf8
import os
import shutil


#Get the current directory with getcwd first 
filewd=os.getcwd()
print(filewd)
# Use relative paths to create directories
# Is the directory path to which the directory is to be created
path1="testcreate"
# Call the chdir method of the OS module to modify the program working directory
os.chdir("E:/")
# Call the mkdir method of the OS module to create the directory
os.mkdir(path1)
print('New DIR created successfully!')  #New DIR created successfully!
f=open('E:/testcreate/testp.txt','w')
f.write('Hello World!')
f.close()

# List files and subdirectories

# Gets all files in the specified directory
listdir1=os.listdir(path1)
print("Files and directories contained in the directory:",listdir1)

# Move file or subdirectory to another location
dsc = 'E:/testcreate/movetest.txt'
shutil.move("E:/testcreate/testp.txt","dsc")
print("After moving the file location:")

# Delete directory
# Delete the directory through using the rmdir method
#path3 Is the directory path of the directory to be deleted
path3="E:/testcreate"
# Invoke the rmdir method of the os module to delete the directory
os.rmdir(path3)
print('Folder deleted successfully!')  #New DIR created successfully!


