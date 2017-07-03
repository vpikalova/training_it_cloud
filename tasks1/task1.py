text = raw_input()
text = text.upper()
repllist = [",",".",":",";","!","?"]
for x in repllist:
    text=text.replace(x,"")
list = text.split(" ")
count = 0
for x in list:
    if (len(x) > 0):
        if (x==x[::-1]):
            count += 1
print(count)
