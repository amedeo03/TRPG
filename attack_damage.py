import random

# this function will return the damage suffered by an entity
def attack(att_stat_attacker, evade_stat_defender):
    evade_roll = random.randint(0, 100)
    if evade_roll < evade_stat_defender:
        damage = 0
    else:
        damage = att_stat_attacker

    return damage