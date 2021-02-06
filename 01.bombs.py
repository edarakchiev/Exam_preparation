from collections import deque


bomb_effect = deque([int(n) for n in input().split(", ")])
bomb_casings = [int(n) for n in input().split(", ")]


DATURA = 40
CHERRY = 60
DECOY = 120

datura_bombs = 0
cherry_bombs = 0
decoy_bombs = 0
status = False

while bomb_effect:
    current_effect = bomb_effect.popleft()
    while True:
        current_casings = bomb_casings.pop()
        current_sum = current_casings + current_effect
        if current_sum == DATURA:
            datura_bombs += 1
            break
        elif current_sum == CHERRY:
            cherry_bombs += 1
            break
        elif current_sum == DECOY:
            decoy_bombs += 1
            break
        else:
            current_casings -= 5
            bomb_casings.append(current_casings)
    if datura_bombs >= 3 and cherry_bombs >= 3 and decoy_bombs >= 3:
        status = True
        break
    if not bomb_casings:
        break

if status:
    print(f"Bene! You have successfully filled the bomb pouch!")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

if bomb_effect:
    print(f"Bomb Effects: {', '.join([(str(el)) for  el in bomb_effect])}")
else:
    print(f"Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join([(str(el)) for  el in bomb_casings])}")
else:
    print(f"Bomb Casings: empty")
print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {decoy_bombs}")
