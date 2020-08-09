import os 


def isBinod(filename):
    #Return true if binod is present or else false
    with open(filename, "r") as f:
        fileContent=f.read();
        #Detect all forms of binod/Binod/biNOD/biNoD
    if "binod" in fileContent.lower(): 
        return True   
    else:
        return False    




if __name__=="__main__":
    #Listing the content of this folder
    dir_contents=os.listdir();
    nBinod=0
    print(dir_contents)
    #For each textfile we will check if Binod is present.
    for item in dir_contents:
        if item.endswith('txt'):
            print(f"Detecting Binod in {item}\n...\n...\n...")
            flag=isBinod(item)
            if(flag):
                print(f"Binod found in {item}\n")
                nBinod+=1
            else:
                print(f"Binod not found in {item}\n")    

    print("-----Binod Detector Summary-----\n")
    print(f"{nBinod} files found with Binod hidden into them\n")