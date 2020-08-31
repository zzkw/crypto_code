def jm(num):
    str2='gndk€rlqhmtkwwp}z'
    flag=''
    for i in str2:
        try:
            num+=1
            number=ord(i)-num
            key=chr(number)
            flag+=key
        except:
            pass

    return flag
for i in range(20):
    flag=jm(i)
    print(flag)
    if flag[:4]=='flag':
        print('flag is ---',flag)
        exit(0)
