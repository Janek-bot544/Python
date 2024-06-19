import random
a = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pasw = ""
long = int(input( "Jak długie chcesz mieć hasło na faceboka???"))
for i in range(long):
    pasw += random.choice(a)

print(f'twoje hasło: - {pasw}')
