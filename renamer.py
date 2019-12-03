import os
import csv
from tempfile import NamedTemporaryFile
import shutil

INVENTORY_LOCATION = os.environ['INVENTORY_FOLDER']

class Renamer:
    def _processCSV(self, csvFullPath, nameToFind, newName):
        nameToCheck = nameToFind.lower()
        tempCSV = NamedTemporaryFile(delete=False, mode='w')

        found = False

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
                        found = True
                    invWriter.writerow(row)
                    

                except IndexError:
                    # If Row does not have a second column, ignore the error.
                    continue
        if (found == True):
            shutil.copyfile(tempCSV.name, csvFullPath)
            print(f"Moved {tempCSV.name} to {csvFullPath}")


    def _renameLocal(self, oldName, newName):
        for subdir, dirs, files in os.walk(INVENTORY_LOCATION):
            for file in files:
                filepath = subdir + os.sep + file
                if (file.endswith("csv")):
                    self._processCSV(filepath, oldName, newName)
    def _renameAD(self, oldName, newName):
        pass
    
    def Rename(self, oldName, newName):
        self._renameLocal(oldName, newName)
        self._renameAD(oldName, newName)