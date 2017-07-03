def find_most_frequent(text):
    text = str.lower(text)
    repllist = [",", ".", ":", ";", "!", "?"]
    for x in repllist:
        text = text.replace(x, "")
    dict={}
    for x in text.split(" "):
        if(dict.get(x,-1)==-1):
            dict[x]=0
        dict[x]+=1
    max=0
    for x in dict.keys():
        if (dict[x]>max):
            max=dict[x]
    ret=[]
    for x in dict.keys():
        if (dict[x]==max):
            ret.append(x)
    return ret

def main():
    print (find_most_frequent(raw_input()))


if __name__ == '__main__':
    main()