replacementMap = {
    # "አ": "ኣ",
    # "ኣ": "አ",
    "ዐ": "አ",
    "ዑ": "ኡ",
    "ዒ": "ኢ",
    "ዓ": "አ",
    "ዔ": "ኤ",
    "ዕ": "እ",
    "ዖ": "ኦ",
    "ሐ":"ሀ",
    "ሓ":"ሀ",
    "ሑ": "ሁ",
    "ሒ": "ሂ",
    "ሃ":  "ሀ",
    "ሔ": "ሄ",
    "ሕ": "ህ",
    "ኹ": "ሁ",
    "ኺ": "ሂ",
    "ኼ": "ሄ",
    "ኾ": "ሆ",
    "ኽ": "ህ",
    "ኻ": "ሀ",
    "ሖ": "ሆ",
    "ሠ": "ሰ",
    "ሡ": "ሱ",
    "ሢ": "ሲ",
    "ሣ": "ሳ",
    "ሤ": "ሴ",
    "ሥ": "ስ",
    "ሦ": "ሶ",
    "ሧ": "ሷ",
    "ፀ": "ጸ",
    "ፁ": "ጹ",
    "ፂ": "ጺ",
    "ፃ": "ጻ",
    "ፄ": "ጼ",
    "ፅ": "ጽ",
    "ፆ": "ጾ",
    'ዀ':"ሆ",
    'ቓ':"ቃ",
    ';':"",
    'ቐ':"ቀ",
    "ዃ":"ኋ",
    "ዂ":"ኊ",
    "ጎ":"ጐ",
    "ቈ":"ቆ",
    "ዃ": "ኋ",
    "ኋ": "ኋ",
    "ዽ": "ድ"
}

def replace(source:str, destination: str):
    with open(source, "r", encoding="utf-8") as file, open(destination, "w", encoding="utf-8") as file_new:
        lines = file.readlines()
        for a in lines:
            for b in replacementMap.keys():
                if b in a:
                    # print(b, a)
                    a = a.replace(b, replacementMap[b], -1)
            file_new.write(a.strip()+"\n")
            
            
def replaceTheMap():
    old_Phonemes = {
    "ህኡኣ": "ኋ", "ልኡኣ": "ሏ", "ምኡኣ": "ሟ","ርኡኣ": "ሯ","ስኡኣ": "ሷ","ሽኡኣ": "ሿ","ቅኡኣ": "ቋ",    "ብኡኣ": "ቧ",    "ቭኡኣ": "ቯ",    "ትኡኣ": "ቷ",    "ችኡኣ": "ቿ",    "ንኡኣ": "ኗ",    "ኝኡኣ": "ኟ",    "ክኡኣ": "ኳ",    "ዝኡኣ": "ዟ",    "ዥኡኣ": "ዧ",    "ድኡኣ": "ዷ",    "ጅኡኣ": "ጇ",    "ግኡኣ": "ጓ",    "ጥኡኣ": "ጧ",    "ጭኡኣ": "ጯ",    "ጵኡኣ": "ጷ",    "ጽኡኣ": "ጿ",    "ፍኡኣ": "ፏ",    "ፕኡኣ": "ፗ",    "ግኡኤ": "ጔ","ክኡኤ": "ኴ","ህኡኤ": "ኌ","ቅኡኤ": "ቌ","ግኡኢ": "ጒ","ክኡኢ": "ኲ",    "ህኡኢ": "ኊ",    "ቅኡኢ": "ቊ", "ህ": "ህ",    "ል": "ል",    "ም": "ም",    "ር": "ር",    "ስ": "ስ", "ሽ": "ሽ",    "ቅ": "ቅ",    "ብ": "ብ",    "ቭ": "ቭ",    "ት": "ት",    "ች": "ች",    "ን": "ን",    "ኝ": "ኝ",    "ክ": "ክ",    "ው": "ው",    "ዝ": "ዝ",    "ዥ": "ዥ",    "ይ": "ይ",    "ድ": "ድ",    "ጅ": "ጅ",    "ግ": "ግ",    "ጥ": "ጥ",    "ጭ": "ጭ",    "ጵ": "ጵ",    "ጽ": "ጽ",    "ፍ": "ፍ",    "ፕ": "ፕ", "ህኧ":"ኸ",    "ህኣ": "ሀ",    "ህኡ": "ሁ",    "ህኢ": "ሂ",    "ህኤ": "ሄ",    "ህኦ": "ሆ",    "ልኧ": "ለ",    "ልኡ": "ሉ",    "ልኢ": "ሊ",    "ልኣ": "ላ",    "ልኤ": "ሌ",    "ልኦ": "ሎ",    "ምኧ": "መ",    "ምኡ": "ሙ",    "ምኢ": "ሚ",    "ምኣ": "ማ",    "ምኤ": "ሜ",    "ምኦ": "ሞ",    "ርኧ": "ረ",    "ርኡ": "ሩ",    "ርኢ": "ሪ",    "ርኣ": "ራ",    "ርኤ": "ሬ",    "ርኦ": "ሮ",    "ስኧ": "ሰ",    "ስኡ": "ሱ",    "ስኢ": "ሲ",    "ስኣ": "ሳ",    "ስኤ": "ሴ",    "ስኦ": "ሶ",    "ሽኧ": "ሸ",    "ሽኡ": "ሹ",    "ሽኢ": "ሺ",    "ሽኣ": "ሻ",    "ሽኤ": "ሼ",    "ሽኦ": "ሾ",    "ቅኧ": "ቀ",    "ቅኡ": "ቁ",    "ቅኢ": "ቂ",    "ቅኣ": "ቃ",    "ቅኤ": "ቄ",    "ቅኦ": "ቆ",    "ብኧ": "በ",    "ብኡ": "ቡ",    "ብኢ": "ቢ",    "ብኣ": "ባ",    "ብኤ": "ቤ",    "ብኦ": "ቦ",    "ቭኧ": "ቨ",    "ቭኡ": "ቩ",    "ቭኢ": "ቪ",    "ቭኣ": "ቫ",    "ቭኤ": "ቬ",    "ቭኦ": "ቮ",    "ትኧ": "ተ",    "ትኡ": "ቱ",    "ትኢ": "ቲ",    "ትኣ": "ታ",    "ትኤ": "ቴ",    "ትኦ": "ቶ",    "ችኧ": "ቸ",    "ችኡ": "ቹ",    "ችኢ": "ቺ",    "ችኣ": "ቻ",    "ችኤ": "ቼ",    "ችኦ": "ቾ",    "ንኧ": "ነ",    "ንኡ": "ኑ",    "ንኢ": "ኒ",    "ንኣ": "ና",    "ንኤ": "ኔ",    "ንኦ": "ኖ",    "ኝኧ": "ኘ",    "ኝኡ": "ኙ",    "ኝኢ": "ኚ",    "ኝኣ": "ኛ",    "ኝኤ": "ኜ",    "ኝኦ": "ኞ",    "ክኧ": "ከ",    "ክኡ": "ኩ",    "ክኢ": "ኪ",    "ክኣ": "ካ",    "ክኤ": "ኬ",    "ክኦ": "ኮ",    "ውኧ": "ወ",    "ውኡ": "ዉ",    "ውኢ": "ዊ",    "ውኣ": "ዋ",    "ውኤ": "ዌ",    "ውኦ": "ዎ",    "ዝኧ": "ዘ",    "ዝኡ": "ዙ",    "ዝኢ": "ዚ",    "ዝኣ": "ዛ",    "ዝኤ": "ዜ",    "ዝኦ": "ዞ",    "ዥኧ": "ዠ",    "ዥኡ": "ዡ",    "ዥኢ": "ዢ",    "ዥኣ": "ዣ",    "ዥኤ": "ዤ",    "ዥኦ": "ዦ",    "ይኧ": "የ",    "ይኡ": "ዩ",    "ይኢ": "ዪ",    "ይኣ": "ያ",    "ይኤ": "ዬ",    "ይኦ": "ዮ",    "ድኧ": "ደ",    "ድኡ": "ዱ",    "ድኢ": "ዲ",    "ድኣ": "ዳ",    "ድኤ": "ዴ",    "ድኦ": "ዶ",    "ጅኧ": "ጀ",    "ጅኡ": "ጁ",    "ጅኢ": "ጂ",    "ጅኣ": "ጃ",    "ጅኤ": "ጄ",    "ጅኦ": "ጆ",    "ግኧ": "ገ",    "ግኡ": "ጉ",    "ግኢ": "ጊ",    "ግኣ": "ጋ",    "ግኤ": "ጌ",    "ግኦ": "ጐ",    "ጥኧ": "ጠ",    "ጥኡ": "ጡ",    "ጥኢ": "ጢ",    "ጥኣ": "ጣ",    "ጥኤ": "ጤ",    "ጥኦ": "ጦ",    "ጭኧ": "ጨ",    "ጭኡ": "ጩ",    "ጭኢ": "ጪ",    "ጭኣ": "ጫ",    "ጭኤ": "ጬ",    "ጭኦ": "ጮ",    "ጵኧ": "ጰ",    "ጵኡ": "ጱ",    "ጵኢ": "ጲ",    "ጵኣ": "ጳ",    "ጵኤ": "ጴ",    "ጵኦ": "ጶ",    "ጽኧ": "ጸ",    "ጽኡ": "ጹ",    "ጽኢ": "ጺ",    "ጽኣ": "ጻ",    "ጽኤ": "ጼ",    "ጽኦ": "ጾ",    "ፍኧ": "ፈ",    "ፍኡ": "ፉ",    "ፍኢ": "ፊ",    "ፍኣ": "ፋ",    "ፍኤ": "ፌ",    "ፍኦ": "ፎ",    "ፕኧ": "ፐ",    "ፕኡ": "ፑ",    "ፕኢ": "ፒ",    "ፕኣ": "ፓ",    "ፕኤ": "ፔ",    "ፕኦ": "ፖ", " ኧ": "ኧ",    " ኣ": "ኣ",    " ኡ": "ኡ",    " ኢ": "ኢ",    " ኤ": "ኤ",    " እ": "እ",    " ኦ": "ኦ", "ኧ": "ኧ",    "ኣ": "አ",    " ኡ": "ኡ",    "ኢ": "ኢ",    "ኤ": "ኤ",    "እ": "እ",    "ኦ": "ኦ"}
    for a in old_Phonemes:
        if old_Phonemes[a] in replacementMap.keys():
            old_Phonemes[a]=replacementMap[old_Phonemes[a]]    
    print(old_Phonemes)
            


if __name__ == "__main__":
    # replaceTheMap()
    # replace("tigre.txt", "tigre_new.txt")
    replace("am_filtered_new.txt", "am_filtered_new_new.txt")
    # replace("test/text.txt", "test/text_new.txt")