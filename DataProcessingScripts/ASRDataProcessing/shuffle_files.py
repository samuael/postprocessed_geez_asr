import numpy as np

def shuffle_datapoints():
    with open("text_new.txt", "r", encoding="utf-8") as file:
        shuffled = open("text_shuffle.txt", "w", encoding="utf-8")
        
        lines = file.readlines()
        
        lines = np.asarray(lines)
        indexes = np.arange(len(lines))
        np.random.shuffle(indexes)
        
        print("Len: ",len(lines), " Indexes: ", len(indexes))
        
        lines= lines[indexes]
        print("Shuffled len: ",len(lines))
        for a in lines:
            shuffled.write(a.strip()+"\n")
        
        shuffled.close()


if __name__ == "__main__":
    shuffle_datapoints()