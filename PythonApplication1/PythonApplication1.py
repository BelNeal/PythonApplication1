

import openpyxl
import os
import time
import stat
import webbrowser




path = r"Z:\1. Projects"
vendor = "5.  Vendor Information"
vendorEncore = "2.  Vendor Information"
ConstrEncore = "2.  Vendor Information"
Constructionfolder = "4. Engineering\\2. Construction Documents"
removedire = {"0. Approval Documents", '0.5 Plasma Work','0.1. Folder Template' ,'0.2. Common Components','0.3. Issues'}

def GetProjectNum():
   getLastMod(path)
   print('What project# are you looking for')
   global FileName 
   FileName = input()
   searchFile(FileName)
   return FileName

def getLastMod(path):

    date_format = '%Y-%m-%d'
    dirList = os.listdir(path)
   # print(dirList)
    for dirList in dirList:
        fileNameDirSearch = os.path.join(path, dirList)
        modTimeepoch = os   .path.getmtime(fileNameDirSearch)
        modTime = time.strftime('%Y-%m-%d', time.localtime(modTimeepoch))
    #    print(modTime)
        if time.strptime('2021-1-1', date_format) >= time.strptime(modTime, date_format): #<= time.strptime('2022-1-1', date_format):
            removedire.add(dirList)
           # return removedire
    #print(removedire)
    return removedire
    






def searchFile(fileName):
       # print(fileName)
        for root, dir, files in os.walk(path):
         dir[:] =[d for d in dir if d not in removedire]
        # print(dir)
         print('Looking in:', root)
         for dir in dir:
            try:
                found = dir.find(fileName)
                #print(found)
                if found != -1:
                    print(fileName, 'Found')
                    print(dir)
                    print(root)
                    print('Is this the correct Folder: Enter " n" for no, and Press enter for yes')
                    Next1 = input()
                    if Next1.lower == 'n':
                        continue
                    elif (Next1.lower == 'exit'):
                        exit()
                    elif (Next1.lower == 's'):
                        FileName = input()
                        searchFile(FileName)
                    else:            
                        print("Which Folder do you want to open?")
                        print("1.Vendor")
                        print("2.Construction")
                        ChooseFolder = input()
                        if ChooseFolder == "1":
                            if (root.lower().find("encore")!=-1):
                                fileNameDir = os.path.join(root,dir, vendorEncore)
                            else:
                                fileNameDir = os.path.join(root,dir,vendor)
                            print(fileNameDir)
                            Filelist = os.listdir(fileNameDir)
                            print()
                            #Next = input()
                            if found !=  -1:
                                for files in  Filelist:
                                   print(files)
                        elif ChooseFolder == "2":
                            if (root.lower().find("encore")!=-1):
                                fileNameDir = os.path.join(root,dir, ConstrEncore)
                            else:
                                fileNameDir = os.path.join(root,dir, Constructionfolder)
                            print(fileNameDir)
                            Filelist = os.listdir(fileNameDir)
                            print()
                            #Next = input()
                            if found !=  -1:
                                for files in  Filelist:
                                   print(files)
                        
                        print('Enter "o" to open folder or Enter to cont.')
                        openfile = input()

                        if openfile.lower() == 'o':
                            webbrowser.open(os.path.realpath(fileNameDir))

                        print('What project# are you looking for or Type exit to exit')
                        FileName = input()
                        if fileName != 'exit':
                           searchFile(FileName)
                        else:
                            exit()
                            
                        
                    quit()

                   # exit()
                   


            except: 
                break
        print("Not Found")
        print('What project# are you looking for or Type exit to exit')
        FileName = input()
        if fileName != 'exit':
            searchFile(FileName)
        else:
            exit()
        

if __name__ == '__main__':
    GetProjectNum()
    

            
                
  