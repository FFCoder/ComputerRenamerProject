import os
import csv
from tempfile import NamedTemporaryFile


INVENTORY_LOCATION = os.environ['INVENTORY_FOLDER']

def processCSV(csvFullPath, nameToFind, newName):
    nameToCheck = nameToFind.lower()
    tempCSV = NamedTemporaryFile(delete=False, mode='w')
    with open(csvFullPath) as invFile, tempCSV:
        invReader = csv.reader(invFile)
        invWriter = csv.writer(tempCSV)
        for row in invReader:
            
            try:
                computerName = row[1].lower()
                if (computerName == nameToCheck):
                    print(f"Computer Name: {nameToCheck} found in {csvFullPath}")
                    print(f"Saving to {tempCSV.name}")
                    row[1] = newName
                    invWriter.writerow(row)
                    return True
                else:
                    invWriter.writerow(row)
                

            except IndexError:
                continue


def renameLocal(oldName, newName):
    for subdir, dirs, files in os.walk(INVENTORY_LOCATION):
        for file in files:
            filepath = subdir + os.sep + file
            if (file.endswith("csv")):
                check = processCSV(filepath, oldName, newName)
                if (check == True) :
                


