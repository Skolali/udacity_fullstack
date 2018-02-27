import os
import string

def rename_files():
    #get the names of files in the folder
    path = r"C:/Users/skolali/NanoDegree/Mod1/alphabet/message"
    file_names = os.listdir(path)
    current_path = os.getcwd()
    os.chdir(path)
    print(filenames)
    for file_name in file_names:
        new_name = file_name.translate(str.maketrans('','','0123456789'))
         #rename the filename for each file
        os.rename(file_name, new_name)
        print("renamed file_name {} to {}".format(file_name,new_name ))
    os.chdir(current_path)

rename_files()
