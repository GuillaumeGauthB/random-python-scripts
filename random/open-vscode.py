# Script to open school folders on vscode cuz im lazy and dont want to do it myself

import os.path
import subprocess
import psutil

isXamppOpen="xampp-control.exe" in (i.name() for i in psutil.process_iter())
rootDirectory=os.path.expanduser('~/ecole')
applicationDirectory=os.path.expanduser('~/Logiciels')

listDirectories = []
notWanted = []

for d in os.listdir(rootDirectory):
	# print(d)
	if "." in d:
		notWanted.append(d)
	else:
		listDirectories.append(d)

print("Which class: \n", listDirectories)
toOpen = input("Class to open: ")
print(toOpen)
if "4w4" in toOpen:
	toOpenLocation="%s\\xampp\\htdocs\\wordpress"%applicationDirectory
	if isXamppOpen is True:
		print("xampp-control is open.\nNo need to open it again")
	else:
		print("xampp-control is not open.\nIt'd probably be good to open it\nBut i'm still scared after it killed my installation")
		# THIS IS EVIL
		# THIS BREAK XAMPP
		# STAY BACK DEMON
		# subprocess.Popen("%s\\xampp-2\\xampp-control.exe"%applicationDirectory)
elif "iwra" in toOpen:
	choice=input("tp, class: ")
	if "tp" in choice:
		print(os.listdir(os.path.expanduser("%s/%s/evaluations/tp"%(rootDirectory, toOpen))))
		choiceTP=input("tt, name: ")
		if "tp" in choiceTP:
			toOpenLocation="%s/%s/evaluations/tp/%s"%(rootDirectory, toOpen, choiceTP)
		else:
			toOpenLocation="%s/%s/evaluations/tp"%(rootDirectory, toOpen)
	elif "class" in choice:
		print(os.listdir(os.path.expanduser("%s/%s/cours"%(rootDirectory, toOpen))))
		choiceEx=input("tt, name: ")
		if "tt" in choiceEx:
			toOpenLocation="%s/%s/cours"%(rootDirectory, toOpen)
		else:
			toOpenLocation="%s/%s/cours/%s"%(rootDirectory, toOpen, choiceEx)
		print(toOpenLocation)
	else:
		toOpenLocation="%s/%s/cours"%(rootDirectory, toOpen)
else:
	toOpenLocation="%s/%s"%(rootDirectory, toOpen)

subprocess.Popen("%s\\VSCode1591\\Code.exe %s"%(applicationDirectory, toOpenLocation))

