from pwn import *

# io = context.binary = ELF('./main')
io = remote("babyrevjohnson.chal.irisc.tf", 10002)

# process()

# red = 1
# blue = 2
# green = 3
# yellow = 4

# pizza = 1
# pasta = 2
# steak = 3
# chicken = 4

# chosenFoods_2 != pasta && chosenFoods_3 != pasta
# chosenColors_1 != red
# chosenColors[0] != green && chosenColors_1 != green
# chosenFoods[0] != chicken || chosenFoods_3 == steak || chosenColors_2 == blue || chosenColors_3 != blue

io.sendlineafter(b':', b'red')
io.sendlineafter(b':', b'yellow')
io.sendlineafter(b':', b'green')
io.sendlineafter(b':', b'blue')
io.sendlineafter(b':', b'chicken')
io.sendlineafter(b':', b'pasta')
io.sendlineafter(b':', b'steak')
io.sendlineafter(b':', b'pizza')

print(io.recvallS())

io.close()