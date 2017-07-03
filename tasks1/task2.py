def trimmed_text(text,limit):
    if len(text)<=limit:
        return text
    i=0
    pr=0
    while i<limit:
        if (text[i]==" "):
            pr=i
        i+=1
    if (pr+3>limit):
        pr-=1
        while (text[pr]!=" " and pr>0):
            pr-=1
    if (pr==0):
        return text[:limit-3]+"..."
    if (pr+3)<=limit:
        return text[:pr]+"..."

def main():
    print(trimmed_text('Python is simple to use, but it is a real programming language.',7))

if __name__ == '__main__':
    main()