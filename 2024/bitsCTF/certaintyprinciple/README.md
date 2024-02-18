# MogamBro's Certainty Principle (PWN)

`Description`

MogamBro's Certainty Principle states that the more accurate you are the more delay you'll face. Δt • Δp ≥ frustration / ram_space; where p is precission and t is time.

```
$ nc 20.244.33.146 4445
Enter password: A
Incorrect password
Time taken:  8.574516805406616e-05
```

`Solution`

Base from the description of the challenge, every input password will give us the time taken. So I tried a lot of inputs like single characters.

```
$ nc 20.244.33.146 4445
Enter password: s
Incorrect password
Time taken:  0.10007056659247279

$ nc 20.244.33.146 4445
Enter password: s
Incorrect password
Time taken:  0.10003479356750938
```

I noticed that if I input 's' the time taken is constant < 1 so this guessing game. So I wrote a script to brute force the password.

```python
from pwn import *

charset = 'abcdefghijklmnopqrstuvwxyz'

stored_nums = '7' # decimal part of the time taken
stored_nums2 = '7' # decimal part of the time taken

password1 = 'sloppytoppywithatwist'
password2 = 'gingerdangerhermoinegranger'
password3 = 'hickerydickerydockskibididobdobpop'
password4 = 'snickersnortsupersecureshortshakingsafarisadistic'
password5 = 'boompopwhizzleskizzleraptrapmeowbarkhowlbuzzdrumburpfartpoo'

context.log_level = 'info'

# any chars execpt 's' gives Time Taken > 0.1000....
# so start with 0.1 get only the decimal part of the time taken

while True:
    for c in charset:
        io = remote('20.244.33.146', 4445)
        io.sendlineafter(':', password1) # level 1 passed
        io.sendlineafter(':', password2) # level 2 passed
        io.sendlineafter(':', password3) # level 3 passed
        io.sendlineafter(':', password4)  # level 4 passed
        io.sendlineafter(':', password5 + c) # level 5
        io.recvline()
        res = io.recvline().decode().strip().split(' ')[-1]
        info(f'c: {c}, res: {res}, password: {password1}, password2: {password2}, password3: {password3}, password4: {password4}, password5: {password5 + c}')
        

        res2 = res.split('.')[1]

        # since the decimal places values is not constant that's why I used the first 2 decimal places
        if res2[1] != stored_nums[-1] or res2[2] != stored_nums2[-1]:
            stored_nums += res2[1]
            stored_nums2 += res2[2]
            password5 += c
            print(password5)
            break
        io.close()
```
My solution is not quite good since every right precision (character) the time taken will getting slower and slower (takes more hours to bruteforce when you reach level 4 - 5). You can enhance this by running multithreading.

After found the password for level 5, we got the flag.

```
└─$ nc 20.244.33.146 4445
Enter password: sloppytoppywithatwist
Congratulations! You have unlocked the door to level 2!
Enter password: gingerdangerhermoinegranger
Congratulations! You have unlocked the door to level 3!
Enter password: hickerydickerydockskibididobdobpop
Congratulations! You have unlocked the door to level 4!
Enter password: snickersnortsupersecureshortshakingsafarisadistic
Congratulations! You have unlocked the door to level 5!
Enter password: boompopwhizzleskizzleraptrapmeowbarkhowlbuzzdrumburpfartpoop
Congratulations! You have unlocked all the doors. THe flag is BITSCTF{c0n6r47ul4710n5_0n_7h3_5ucc355ful_3n7ry}
```