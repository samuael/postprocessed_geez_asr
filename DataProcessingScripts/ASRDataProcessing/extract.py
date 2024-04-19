import re
import json

def extract_amharic(filename:str):
    with open(filename, "r", encoding ="utf-8") as f:
        lines = f.read().replace("\n\n", "\n").split("\n")[:-1]
        
        filtered = open(f"{filename.removesuffix('.txt')}_filtered.txt", "w", encoding="utf-8")
        count=0
        last =""
        waiting = ""
        geez_characters = ["ህ","ል", "ም", "ር", "ስ", "ሽ", "ቅ", "ብ", "ቭ", "ት", "ች", "ን", "ኝ", "ክ", "ው", "ዝ", "ዥ", "ይ", "ድ", "ጅ", "ግ", "ጥ", "ጭ", "ጵ", "ጽ", "ፍ", "ፕ", "ኧ", "አ", "ኡ", "ኢ", "ኤ", "እ", "ኦ", "ኸ", "ሀ", "ሁ", "ሂ", "ሄ", "ሆ", "ለ", "ሉ", "ሊ", "ላ", "ሌ", "ሎ", "መ", "ሙ", "ሚ", "ማ", "ሜ", "ሞ", "ረ", "ሩ", "ሪ", "ራ", "ሬ", "ሮ", "ሰ", "ሱ", "ሲ", "ሳ", "ሴ", "ሶ", "ሸ", "ሹ", "ሺ", "ሻ", "ሼ", "ሾ", "ቀ", "ቁ", "ቂ", "ቃ", "ቄ", "ቆ", "በ", "ቡ", "ቢ", "ባ", "ቤ", "ቦ", "ቨ", "ቩ", "ቪ", "ቫ", "ቬ", "ቮ", "ተ", "ቱ", "ቲ", "ታ", "ቴ", "ቶ", "ቸ", "ቹ", "ቺ", "ቻ", "ቼ", "ቾ", "ነ", "ኑ", "ኒ", "ና", "ኔ", "ኖ", "ኘ", "ኙ", "ኚ", "ኛ", "ኜ", "ኞ", "ከ", "ኩ", "ኪ", "ካ", "ኬ", "ኮ", "ወ", "ዉ", "ዊ", "ዋ", "ዌ", "ዎ", "ዘ", "ዙ", "ዚ", "ዛ", "ዜ", "ዞ", "ዠ", "ዡ", "ዢ", "ዣ", "ዤ", "ዦ", "የ", "ዩ", "ዪ", "ያ", "ዬ", "ዮ", "ደ", "ዱ", "ዲ", "ዳ", "ዴ", "ዶ", "ጀ", "ጁ", "ጂ", "ጃ", "ጄ", "ጆ", "ገ", "ጉ", "ጊ", "ጋ", "ጌ", "ጐ", "ጠ", "ጡ", "ጢ", "ጣ", "ጤ", "ጦ", "ጨ", "ጩ", "ጪ", "ጫ", "ጬ", "ጮ", "ጰ", "ጱ", "ጲ", "ጳ", "ጴ", "ጶ", "ጸ", "ጹ", "ጺ", "ጻ", "ጼ", "ጾ", "ፈ", "ፉ", "ፊ", "ፋ", "ፌ", "ፎ", "ፐ", "ፑ", "ፒ", "ፓ", "ፔ", "ፖ", "ኋ", "ሏ", "ሟ", "ሯ", "ሷ", "ሿ", "ቋ", "ቧ", "ቯ", "ቷ", "ቿ", "ኗ", "ኟ", "ኳ", "ዟ", "ዧ", "ዷ", "ጇ", "ጓ", "ጧ", "ጯ", "ጷ", "ጿ", "ፏ", "ፗ", "ጔ", "ኴ", "ኌ", "ቌ", "ጒ", "ኲ", "ኊ", "ቊ", " ", "\n",  "ሠ","ሡ","ሢ","ሣ","ሤ","ሥ","ሦ","ሧ","ሐ","ሑ","ሒ","ሓ","ሔ","ሕ","ሖ","ሃ","ኀ","ኁ","ኂ","ኃ","ኄ","ኅ","ኆ","ፀ","ፁ","ፂ","ፃ","ፄ","ፅ","ፆ","ፇ","ዐ","ዑ","ዒ","ዓ","ዔ","ዕ","ዖ","ጎ","ኰ","ሀ","ሁ","ሂ","ሄ","ህ","ሆ","ለ","ሉ","ሊ","ላ","ሌ","ል","ሎ","ሏ","መ","ሙ","ሚ","ማ","ሜ","ም","ሞ","ሟ","ረ","ሩ","ሪ","ራ","ሬ","ር","ሮ","ሯ","ሰ","ሱ","ሲ","ሳ","ሴ","ስ","ሶ","ሷ","ሸ","ሹ","ሺ","ሻ","ሼ","ሽ","ሾ","ሿ","ቀ","ቁ","ቂ","ቃ","ቄ","ቅ","ቆ","ቊ","ቋ","ቌ","በ","ቡ","ቢ","ባ","ቤ","ብ","ቦ","ቧ","ቨ","ቩ","ቪ","ቫ","ቬ","ቭ","ቮ","ቯ","ተ","ቱ","ቲ","ታ","ቴ","ት","ቶ","ቷ","ቸ","ቹ","ቺ","ቻ","ቼ","ች","ቾ","ቿ","ኊ","ኋ","ኌ","ነ","ኑ","ኒ","ና","ኔ","ን","ኖ","ኗ","ኘ","ኙ","ኚ","ኛ","ኜ","ኝ","ኞ","ኟ","አ","ኡ","ኢ","ኤ","እ","ኦ","ኧ","ከ","ኩ","ኪ","ካ","ኬ","ክ","ኮ","ኰ","ኲ","ኳ","ኴ","ኸ","ወ","ዉ","ዊ","ዋ","ዌ","ው","ዎ","ዘ","ዙ","ዚ","ዛ","ዜ","ዝ","ዞ","ዟ","ዠ","ዡ","ዢ","ዣ","ዤ","ዥ","ዦ","ዧ","የ","ዩ","ዪ","ያ","ዬ","ይ","ዮ","ደ","ዱ","ዲ","ዳ","ዴ","ድ","ዶ","ዷ","ጀ","ጁ","ጂ","ጃ","ጄ","ጅ","ጆ","ጇ","ገ","ጉ","ጊ","ጋ","ጌ","ግ","ጐ","ጒ","ጓ","ጔ","ጠ","ጡ","ጢ","ጣ","ጤ","ጥ","ጦ","ጧ","ጨ","ጩ","ጪ","ጫ","ጬ","ጭ","ጮ","ጯ","ጰ","ጱ","ጲ","ጳ","ጴ","ጵ","ጶ","ጷ","ጸ","ጹ","ጺ","ጻ","ጼ","ጽ","ጾ","ጿ","ፈ","ፉ","ፊ","ፋ","ፌ","ፍ","ፎ","ፏ","ፐ","ፑ","ፒ","ፓ","ፔ","ፕ","ፖ","ፗ",
                           "ኋ", "ሏ", "ሟ", "ሯ", "ሷ", "ሿ", "ቋ", "ቧ", "ቯ", "ቷ", "ቿ", "ኗ", "ኟ", "ኳ", "ዟ", "ዧ", "ዷ", "ጇ", "ጓ", "ጧ", "ጯ", "ጷ", "ጿ", "ፏ", "ፗ", "ጔ", "ኴ", "ኌ", "ቌ", "ጒ", "ኲ", "ኊ", "ቊ",
                           "ህ","ል","ም","ር","ስ","ሽ","ቅ","ብ","ቭ","ት","ች","ን","ኝ","ክ","ው","ዝ","ዥ","ይ","ድ","ጅ","ግ","ጥ","ጭ","ጵ","ጽ","ፍ","ፕ"]
        geez_pattern = re.compile(r'[' + re.escape(''.join(geez_characters)) + ']+')
        for x in lines:
            geez_characters = geez_pattern.findall(x)
            x = ''.join(geez_characters)
            x = re.sub(' +', ' ', x).strip()
            count+=1
            if len(x)<100 and count %25 != 0:
                waiting+=" "+x
                if len(waiting)> 100:
                    filtered.write(waiting.strip()+"\n")
                    waiting=""
                continue
            elif len(x)> 300 or last ==x or len(x)<=3:
                continue
            filtered.write(x.replace("\n", "")+"\n")
            last=x
        filtered.close()


def uniqueWords():
    with open("corpus_filtered.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        wordsMap = {}
        for x in lines:
            for w in x.split(" "):
                try:
                    wordsMap[w]+=1
                except:
                    wordsMap[w]=1
        newFile = open("words.json", "w", encoding="utf-8")
        json.dump(wordsMap, newFile)
        newFile.close()
        
        newTextFile = open("text_words.txt", "w", encoding="utf-8")
        # json.dump(wordsMap, newFile)
        # newTextFile.writelines(list(wordsMap.keys()))
        wordsMap = addUnique(wordsMap)
        print("Found", len(wordsMap), " Words")
        for y in wordsMap.keys():
            if y == "\n":
                continue
            newTextFile.write(y+"\n")
        # print("Found", len(wordsMap), " Words")
        newTextFile.close()
                    
def addUnique(themap:dict)->dict:
    jFile = open("same_sound_characters.json", "r", encoding="utf-8")
    jsonMap = json.load(jFile)
    jFile.close()
    newmap = {}
    for x in themap.keys():
        if x == "\n":
            continue
        x = x.strip()
        for y in jsonMap.keys():
            nw = x.replace(y, jsonMap[y])
            if nw != x:
                newmap[nw]=0
        newmap[x]=0
    return newmap

def count_longest_sentence():
    with open("faulted_corpus.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        count =0 
        max = 0
        for x in lines:
            if len(x)>500:
                count+=1
            if len(x) > max:
                max = len(x)
        print("Max: ", max, "Count: ", count)


def filter_corpus_by_length():
    with open("replaced_filtered.txt", "r", encoding="utf-8") as file:
        shortened= open("shortened_new.txt", "w", encoding="utf-8")
        lines = file.readlines()
        for x in lines:
            x = x.strip()
            if len(x)<=100 and len(x)>3:
                shortened.write(x+"\n")
        shortened.close()

def join_characters():
    with open("dict_spaced.txt", "r", encoding="utf-8") as file:
        joined= open("dict_joined.txt", "w", encoding="utf-8")
        spaced_new= open("dict_spaced_new.txt", "w", encoding="utf-8")
        lines = file.readlines()
        for x in lines:
            spaced_new.write(x)
            x= x.replace(" ", "")
            joined.write(x)
        
        spaced_new.close()
        joined.close()

def filter():
    items = { "!": " ",
              "፦": " ",
              "‹": " ",
              "(": " ",
              "«": " ",
              "፥": " ",
              "%": " ",
              "»": " ",
              ")": " ",
              "›": " ",
              ".": "",
              "+": " ",
              "፣": " ",
              "-": "",
              "።": " ",
              "/": " ",
              "0": " ",
              "1": " ",
              "2": " ",
              "3": " ",
              "4": " ",
              "5": " ",
              "6": " ",
              "7": " ",
              "8": " ",
              "9": " ",
              "፡": " ",
              "፤": " ",
              "፝": " ",
              "*": " ",
              "#": " ",
              "\"": "",
              "?": " "}
    with open("corpus.txt", "r", encoding="utf-8") as file:
        shortened = open("replaced.txt", "w", encoding="utf-8")
        lines = file.readlines()
        for x in lines:
            x = x.strip()
            for y in items:
                x= x.replace(y, items[y])
            shortened.write(x+"\n")
        shortened.close()

if __name__ == "__main__":
    # uniqueWords()
    extract_amharic("am.txt")
    # count_longest_sentence()
    # count_longest_sentence()
    # filter_corpus_by_length()
    # filter_corpus_by_length()
    # join_characters()
    # filter_corpus_by_length()
    # filter()