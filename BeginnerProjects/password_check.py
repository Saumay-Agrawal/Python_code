pswrd = input()

if len(pswrd) >= 8 \
   and pswrd[0].isalpha():
        f1 = False
        for ch in pswrd:
            if ch.isdigit():
                f1 = True
                break:
        f2 = False
        for ch in pswrd:
            if not ch.isdigit() and not ch.isalpha():
                f2 = True
                break:
        if f1 and f2:
            print('Valid')
        else:
            print('Invalid')
else:
    print('Invalid')         
