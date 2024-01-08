try:    
    with open("the", "r") as file:
        orig_flag = file.read()

    runed = []
    z = ord(orig_flag[0])

    for v in orig_flag[1:]:
        runed.append(chr(ord(v) - z))
        z = ord(v) - z

    flag = ''.join(runed)  

    print('i' +flag)

except Exception as e:
    print(e)