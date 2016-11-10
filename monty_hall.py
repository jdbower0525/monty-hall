import random


def keep_door(rounds):
    win_count = 0
    for x in range(rounds):
        doors = [0, 0, 1]
        random.shuffle(doors)
        v = doors[0]
        if v == 1:
            win_count += 1
            continue
    return win_count


def switch_and_keep(rounds):
    win_count = 0
    for x in range(rounds):
        doors = [0, 0, 1]
        random.shuffle(doors)
        v = doors[0]
        if v == 0:
            doors.pop()
            x = random.choice(doors)
            if x == 0:
                win_count += 1
                continue
        else:
            continue
    return win_count


def switch_door(rounds):
    win_count = 0
    for x in range(rounds):
        doors = [0, 0, 1]
        random.shuffle(doors)
        v = doors[0]
        if v == 0:
            doors.pop()
            x = doors[0]
            if x == 0:
                win_count += 1
                continue
        else:
            continue
    return win_count


rounds = int(input(
            "How many times would you like to run the Monty Hall Scenario? "
))


print("Win rates for each test:")
sd = (switch_door(rounds)/rounds)*100
print("Changing your door: {0:.2f}%".format(sd))
sk = (switch_and_keep(rounds)/rounds)*100
print("Switching between keeping the door and changing: {0:.2f}%".format(sk))
kd = (keep_door(rounds)/rounds)*100
print("Keeping the first door: {0:.2f}%".format(kd))
