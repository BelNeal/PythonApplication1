

import openpyxl
import os
import webbrowser

print('What project# are you looking for')
FileName = input()

path = r"Z:\1. Projects"
vendor = "5.  Vendor Information"
removedire = {"0. Approval Documents", '0.5 Plasma Work' }


def searchFile(fileName):
       for root, dir, files in os.walk(path):
        dir[:] =[d for d in dir if d not in removedire]
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
                    if Next1 == 'n':
                        continue
                    else:
                        fileNameDir = os.path.join(root,dir,vendor)
                        print(fileNameDir)
                        Filelist = os.listdir(fileNameDir)
                        print()
                        #Next = input()
                        if found !=  -1:
                            for files in  Filelist:
                               print(files)
                        print('Enter "o" to open folder or Enter to cont.')
                        openfile = input()

                        if openfile == 'o':
                            webbrowser.open(os.path.realpath(fileNameDir))

                        print('What project# are you looking for or Type exit to exit')
                        FileName = input()
                        if fileName != 'exit':
                           searchFile(FileName)
                        else:
                            quit()
                            
                        
                    quit()

                   # exit()
                   


            except:
              break

                            
                  
 
if __name__ == '__main__':
    searchFile(FileName)
                                    
            
                
  