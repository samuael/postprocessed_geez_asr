reMap = {
    'ሠ': 'ሰ',
    'ሡ': 'ሱ',
    'ሢ': 'ሲ',
    'ሣ': 'ሳ',
    'ሤ': 'ሴ',
    'ሥ': 'ስ',
    'ሦ': 'ሶ',
    'ሧ': 'ሷ',
    'ሐ': 'ሀ',
    'ሑ': 'ሁ',
    'ሒ': 'ሂ',
    'ሓ': 'ሀ',
    'ሔ': 'ሄ',
    'ሕ': 'ህ',
    'ሖ': 'ሆ',
    'ሃ':  'ሀ',
    'ኀ' : 'ሀ',
    'ኁ' : 'ሁ',
    'ኂ' : 'ሂ',
    'ኃ' : 'ሀ',
    'ኄ' : 'ሄ',
    'ኅ' : 'ህ',
    "ኆ": 'ሆ',
    'ፀ': 'ጸ',
    'ፁ': 'ጹ',
    'ፂ': 'ጺ',
    'ፃ': 'ጻ',
    'ፄ': 'ጼ',
    'ፅ': 'ጽ',
    'ፆ': 'ጾ',
    'ፇ': 'ጿ',
    "ዐ": "አ",
    "ዑ": "ኡ",
    "ዒ": "ኢ",
    "ዓ": "አ",
    "ዔ": "ኤ",
    "ዕ": "እ",
    "ዖ": "ኦ",
    "ጎ": "ጐ",
    "ኰ": "ኮ"
}

def createSentences():
    with open("corpus_filtered.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        sent = ""
        sent_words=0

        nfile = open("new_corpus.txt", "w", encoding="utf-8")
        
        sentences = []
        for a in lines:
            for b in reMap:
                if b in a:
                    a= a.replace(b, reMap[b])
            a = a.strip()
            if len(a)>200:
                continue
            ws = a.split(" ")
            exceed = False
            for w in ws:
                if len(w)>10:
                    exceed=True
            if exceed:
                continue
            if len(ws)<5:
                if sent=="":
                    sent +=a
                else:
                    sent += " "+a
                sent_words+=len(ws)
                continue
            else:
                nfile.write(a+"\n")

            if sent_words>=5:
                nfile.write(sent)
                sent =""
                sent_words=0
        nfile.close()
        print(sentences)
        
        
# def clipSentences():
#      with open("new_corpus.txt", "r", encoding="utf-8") as file:
#         lines = file.readlines()
#         sent = ""
#         sent_words=0

def averageLength():
    with open("faulted_corpus.txt", "r", encoding="utf-8") as file:
    # with open("corpus_filtered.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        count = len(lines)
        sum = 0
        max = 0
        min=600
        for a in lines:
            sum+= len(a)
            if len(a)>max:
                max = len(a)
            if len(a)<min:
                min = len(a)
        print("Average: ", sum/count)
        print("Min: ", min)
        print("Max: ", max)


def compareFile():
    file1 = open("corpus_filtered.txt", "r", encoding="utf-8")
    file2 = open("corpus_filtered_filtered.txt", "r", encoding="utf-8")
    
    file1Lines = file1.readlines()
    file2Lines = file2.readlines()
    
    index =0
    
    while index < len(file1Lines):
        if file1Lines[index] != file2Lines[index]:
            raise ValueError(f"Difference at index {index}\n Sentence 1: {file1Lines[index]}\n Sentence 2: {file2Lines[index]}")
        index+=1
    # print("all right")
    file1.close()
    file2.close()
    
    


if __name__=="__main__":
    createSentences()
    # averageLength()
    # compareFile()