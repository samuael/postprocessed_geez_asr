
def readFiles(firstfile, secondfile):
    ffile = open(firstfile, "r", encoding="utf-8")
    sfile = open(secondfile, "r", encoding="utf-8")
    
    flines = ffile.read().split("\n")[:-1] #.replace("\n\n", "\n").split("\n")[:-1]
    slines = sfile.read().split("\n")[:-1] #.replace("\n\n", "\n").split("\n")[:-1]
    
    count =0
    for a in slines:
        count+=1
        if a =="":
            print("Count: ", count)
 

    assert len(slines) == len(flines), f"Different line of codes First {len(flines)} and Second {len(slines)}"
    
    ffile.close()
    sfile.close()

if __name__ == "__main__":
    readFiles("corpus_filtered.txt","faulted_corpus.txt")