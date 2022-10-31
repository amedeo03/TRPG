import time
import attack_damage

char_name = str(input("insert your character name: "))
char_health = 10
char_attack = 2
char_evade_stat = 10
pots = 5
# each entity in this game will have their stats stored in a list composed by 4 element.
# 1. entity name, 2. entity max HPs, 3. entity attack stat, 4. entity evasion chance in %
mons1_data = ["Slime", 5, 1, 0]
# mons2_data =

char_rem_hp = char_health
foe_rem_hp = mons1_data[1]
in_combat = True

print(char_name, "encountered a", mons1_data[0])
while in_combat:
    action = int(input("\nWhat do you want to do? (Attack = 1, restore health = 2): "))

    # attack is chosen
    if action == 1:
        # using the attack function from attack_damage.py
        foe_rem_hp = foe_rem_hp - attack_damage.attack(char_attack, mons1_data[3])
        # enemy death condition
        if foe_rem_hp <= 0:
            time.sleep(1)
            print("\n", char_name, "Successfully defeated a", mons1_data[0])
            break

        # summary of your attack
        print("\nYou dealt", char_attack, "damage to the enemy")
        print("The", mons1_data[0], "have", foe_rem_hp, "HPs remaining")

    # restore health is chosen
    if action == 2:
        pots = pots - 1
        if pots > 0:
            char_rem_hp = char_rem_hp + 3
            if char_rem_hp > char_health:
                char_rem_hp = char_health
            print("You're drinking a potion gaining 3 HPs. You now have", char_rem_hp, "HPs and ", pots, "potions left")
        else:
            print("You have no potions left, choose another action")
            continue

    # Enemy combat turn
    print("\nThe", mons1_data[0], "is preparing its attack!")
    char_rem_hp = char_rem_hp - attack_damage.attack(mons1_data[2], char_evade_stat)
    time.sleep(1)
    print("\nYou lost", mons1_data[2], "HPs")
    print("You now have", char_rem_hp, "HPs remaining")