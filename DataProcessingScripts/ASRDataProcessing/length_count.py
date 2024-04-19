



tobeDeleted = [6, 8, 11, 14, 23, 25, 28, 32, 34, 36, 39, 42, 51, 60, 61, 67, 72, 77, 78, 79, 81, 83, 89, 92, 96, 99, 100, 101, 102, 106, 111, 113, 117, 118, 123, 125, 129, 136, 140, 144, 147, 149, 150, 152, 157, 162, 167, 170, 171, 178, 192, 197, 202, 204, 206, 210, 211, 227, 228, 242, 245, 246, 247, 248, 253, 263, 267, 275, 278, 280, 292, 295, 300, 302, 304, 305, 309, 319, 328, 333, 334, 343, 344, 360, 386, 399, 403, 409, 413, 416, 417, 426, 430, 432, 433, 436, 438, 444, 448, 449, 451, 456, 457, 465, 467, 474, 477, 496]

def delete():
    with open("val.join", "r", encoding="utf-8") as file, open("val.spa", "r", encoding="utf-8") as dfile:
        alines = file.readlines()
        blines = dfile.readlines()
        
        newa = open("new_val.join", "w", encoding="utf-8")
        newb = open("new_val.spa", "w", encoding="utf-8")
        
        print(len(tobeDeleted))
        count=0
        while count < len(alines):
            if count in tobeDeleted:
                count+=1
                continue
            newa.write(alines[count].strip()+"\n")
            newb.write(blines[count].strip()+"\n")
            count+=1
            
        newa.close()
        newb.close()

def lengthCount():
    lenoo = []
    with open("val.join", "r", encoding="utf-8") as file:
        alines = file.readlines()
        dfile = open("val.spa", "r", encoding="utf-8")
        blines = dfile.readlines()
        dfile.close()
        
        maxTrain = 510
        count = 0
        while count < len(alines):
            if len(alines[count]) >maxTrain:
                # maxTrain= len(a)
                lenoo.append(count)
            count+=1
        count = 0
        while count < len(blines):
            if len(blines[count]) >maxTrain:
                # maxTrain= len(blines[count])
                lenoo.append(count)
            count+=1
        print("Max Train Length: ", maxTrain)
        
    print(lenoo)
        
        
        # cfile = open("val.join", "r", encoding="utf-8")
        # clines = cfile.readlines()
        # cfile.close()
        
        # efile = open("val.spa", "r", encoding="utf-8")
        # elines = efile.readlines()
        # efile.close()
        
        # maxTest = 0
        # for a in clines:
        #     if len(a) >maxTest:
        #         maxTest= len(a)
        # for a in elines:
        #     if len(a) >maxTest:
        #         maxTest= len(a)
        # print("Max Test Length: ", maxTrain)
        


def mergeLines():
    with open("am_filtered.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        
        newFIle = open("am_filtered_new.txt", "w", encoding="utf-8")
        lastSent = ""
        for a in lines:
            if len(a)>350:
                continue
            elif (len(a)+ len(lastSent)) <256:
                lastSent = lastSent.strip()+" "+ a.strip()
            elif len(a)>len(lastSent):
                newFIle.write(a.strip()+"\n")
            else:
                newFIle.write(lastSent.strip()+"\n")
                lastSent = a
        newFIle.write(lastSent.strip())
        newFIle.close()
        
# def replaceRepetition():
#     replacements = {ሓ,  , ዕ, ዑ, ቕ, ኣ, ሕ, ሃ, ቐ, ዄ, ኻ, ኽ, ኺ, ሑ, ዓ, ሐ, ኾ, ኹ, ጏ, ቓ, ሒ, 9, ዃ, ኼ, ዖ, ጎ, ሥ, ሔ, ዔ, ቑ, ዒ, ጕ, ቝ, ቚ, ቛ, ዂ, ቖ, ኵ, ዐ, ቍ, ሖ, ፃ, ፀ, ፅ, ፆ, ፁ, ፂ, ቈ, ዀ, ዅ, ቘ, ኰ, ቒ, ቔ}



derivedCharacters = [
    "ኋ","ሏ","ሟ","ሯ","ሷ","ሿ","ቋ","ቧ","ቯ","ቷ","ቿ","ኗ","ኟ","ኳ","ዟ","ዧ","ዷ","ጇ","ጓ","ጧ","ጯ","ጷ","ጿ","ፏ","ፗ","ጔ","ኴ","ኌ","ቌ","ጒ","ኲ","ኊ","ቊ"
]


def filterSentencesWithoutDerivedCharacters():
    with open("train.spa", "r", encoding="utf-8") as file, open("filtered_sent.txt", "w", encoding="utf-8") as new_file:
        lines = file.readlines()
        for a in lines:
            found = False
            for b in derivedCharacters:
                if b in a:
                    found = True
                    break
            if not found:
                new_file.write(a.strip()+"\n")



def removeTheLong():
    pass
                
if __name__ == "__main__":
    mergeLines()
    # lengthCount()
    # filterSentencesWithoutDerivedCharacters()
    # delete()