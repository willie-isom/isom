import os

if os.path.isfile(os.path.abspath(os.path.join(os.getcwd(), "..")) + r'\fileName.txt'): 
	with open(os.path.abspath(os.path.join(os.getcwd(), "..")) + r'\fileName.txt', 'r') as file :
		fileName = file.readline().strip()
		fileName = fileName.split(',')
		fileName = 'git add ' + fileName[2]
		os.system(fileName)
		os.system(r'git commit -m "add"')
		os.system(r'git push')