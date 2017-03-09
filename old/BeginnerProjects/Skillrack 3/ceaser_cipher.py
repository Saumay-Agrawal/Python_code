word = input()
d = int(input())

for ch in word:
    if 65 <= ord(ch) <= 90:
        ch = ord(ch)+d
        if ch > 90:
            ch = ch - 26
    elif 97 <= ord(ch) <= 122:
        ch = ord(ch)+d
        if ch > 122:
            ch = ch - 26
    print(chr(ch), end='')
    
