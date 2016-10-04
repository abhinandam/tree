#!/usr/bin/env python3
import subprocess
import sys
import os


#def sortkeys(s):
#  return re.sub('[^A-Za-z0-9]+', '', s).lower()


def createTree(inputDirectory, indentLevel, numDirectories, numFiles):
	files = os.listdir(inputDirectory)
	for index, file in enumerate(files):
		if (file[0] != "."):
			nestedDirectory = inputDirectory + "/" + file
			if (os.path.isfile(nestedDirectory)):
				numFiles += 1
				if (index == len(files) - 1):
					print(indentLevel + '`-- ' + files[index])
				else:
					print(indentLevel + '|-- ' + file)
			elif (os.path.isdir(nestedDirectory)):
				numDirectories += 1
				if (index == len(files) - 1):
					print(indentLevel + '`-- ' + files[index])
				else:
					print (indentLevel + '|-- ' + file)
				indentLevelTemp = indentLevel + '|   '
				numDirectories, numFiles = createTree(nestedDirectory, indentLevelTemp, numDirectories, numFiles)

	return numDirectories, numFiles

if __name__ == '__main__':
	inputDirectory = ""
	if (len(sys.argv) == 1):
		inputDirectory = "."
	else:
		inputDirectory = sys.argv[1]
	print (inputDirectory)
	numDirectories, numFiles = createTree(inputDirectory, "", 0, 0)
	print ("\n" + str(numDirectories) + " directories, " + str(numFiles) + " files")
