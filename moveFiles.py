import os
import shutil
MYDIR = ("outputData")
CHECK_FOLDER = os.path.isdir(MYDIR)
print ("=====> Generating reports")
if not CHECK_FOLDER:
    os.makedirs(MYDIR)
    print("created folder : ", MYDIR)
else:
    print(MYDIR, "folder already exists. Deleting old reports")    
    directory = "./"+MYDIR
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if file.endswith(".csv")]
    for file in filtered_files:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)
src_dir = "./"
dst_dir = "./"+MYDIR+"/"
'''
for root, dirs, files in os.walk(src_dir):
    for f in files:
        if f.endswith('.csv'):
            shutil.copy(os.path.join(root,f), dst_dir)
'''
allfiles = os.listdir(src_dir)
for f in allfiles:
    if f.endswith('.csv'):
        shutil.move(src_dir + f, dst_dir + f)
print ("=====> Reports Generated in '"+MYDIR+"' directory")