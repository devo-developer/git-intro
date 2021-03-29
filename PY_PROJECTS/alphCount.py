# To find count of Alphabets in a word
txt = "ttaapeeetqrr555rttyurbvvvvzyy"
strn = ""
al = ""
cnt = 1

for x in range(len(txt)):

    if al == txt[x]:
        cnt = cnt+1

        if x == len(txt)-1 and cnt > 1:
            z = str(cnt)
            strn += z+al

    elif al != txt[x]:

        if(cnt > 1):
            z = str(cnt)
            strn += z+al
            al = txt[x]
            cnt = 1

            if x == len(txt)-1:
                strn += txt[x]

        else:

            strn += al
            al = txt[x]
            cnt = 1

print(strn)
