import os
import pyfiglet
directory = "./"
files_in_directory = os.listdir(directory)
filtered_files = [file for file in files_in_directory if file.endswith(".csv")]
for file in filtered_files:
	path_to_file = os.path.join(directory, file)
	os.remove(path_to_file)
result = pyfiglet.figlet_format("Dashboard Data", font = "slant")
print(result)
exeStart = pyfiglet.figlet_format("Execution started", font = "digital" )
print(exeStart)
os.system("fetchIssues.py 1")
os.system("readCsv.py 2")
os.system("moveFiles.py 3")
exeEnd = pyfiglet.figlet_format("Execution Ended", font = "digital" )
print(exeEnd)