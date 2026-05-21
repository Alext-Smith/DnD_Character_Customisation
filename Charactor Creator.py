import random

def get_choice(prompt, options):
    print(f"\n{prompt}")
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    while True:
        try:
            choice = int(input("\nEnter the number of your choice: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print(f"  Please enter a number between 1 and {len(options)}.")
        except ValueError:
            print("  Invalid input - please enter a number.")


def describe_class(subclass):
    if subclass == "Fighter":
        print("\n  The Fighter is a master of weapons and armour.")
        print("  They are disciplined, tough, and reliable in any battle.")
        print("  Great for players who want a straightforward, powerful warrior.")
    elif subclass == "Paladin":
        print("\n  The Paladin is a holy warrior blessed with divine power.")
        print("  They can heal allies, smite enemies, and take heavy hits.")
        print("  Great for players who want to be a tank with a heroic feel.")
    elif subclass == "Barbarian":
        print("\n  The Barbarian is a rage-fuelled powerhouse from the wilds.")
        print("  They hit harder than anyone and shrug off enormous damage.")
        print("  Great for players who want to be an unstoppable heavy hitter.")
    elif subclass == "Monk":
        print("\n  The Monk is a swift unarmed combatant trained in martial arts.")
        print("  They move faster than any class and strike with precision.")
        print("  Great for players who want an agile, skilful fighter.")
    elif subclass == "Wizard":
        print("\n  The Wizard studies magic through years of scholarly dedication.")
        print("  They have access to the widest range of spells in the game.")
        print("  Great for players who want versatility and raw magical power.")
    elif subclass == "Sorcerer":
        print("\n  The Sorcerer was born with magic flowing through their veins.")
        print("  They have fewer spells but can bend and twist them in unique ways.")
        print("  Great for players who want instinctive, explosive magical power.")
    elif subclass == "Warlock":
        print("\n  The Warlock made a pact with a powerful and mysterious patron.")
        print("  They have limited spells but they recharge on a short rest.")
        print("  Great for players who want a dark, edgy spellcaster.")
    elif subclass == "Druid":
        print("\n  The Druid draws power from nature and the wild world around them.")
        print("  They can shapeshift into animals and command the elements.")
        print("  Great for players who want a flexible and unpredictable caster.")
    elif subclass == "Rogue":
        print("\n  The Rogue is the classic scoundrel, living by stealth and cunning.")
        print("  They excel at picking locks, stealing, and striking unseen.")
        print("  Great for players who want to be sneaky and resourceful.")
    elif subclass == "Cleric":
        print("\n  The Cleric is a religious healer who heals allies with faith.")
        print("  They can also deal massive damage with the same divine magic.")
        print("  Great for players who want huge burst damage and to support allies.")
    elif subclass == "Bard":
        print("\n  The Bard blends cunning and charm with magical deception.")
        print("  They can cast spells whilst playing music or singing.")
        print("  Great for players who want a clever, creative hybrid character.")
    elif subclass == "Ranger":
        print("\n  The Ranger is a hunter and tracker at home in the wilderness.")
        print("  They excel at ranged combat and have a loyal animal companion.")
        print("  Great for players who want an independent, self-sufficient character.")
    elif subclass == "Artificer":
        print("\n  The Artificer is an inventor who uses magic infused technology.")
        print("  They excel at ranged combat and can have a mechanical companion.")
        print("  Great for players who want an independent, self-sufficient character.")


def weapon_selection(subclass):
    if subclass == "Barbarian" or subclass == "Fighter" or subclass == "Paladin" or subclass == "Ranger":
        print("You have access to Martial and Simple Weapons please select the type of weapon below")
        print("\n  MARTIAL WEAPONS:")
        print("    - Longsword  (1d8 slashing)")
        print("    - Battleaxe  (1d8 slashing)")
        print("    - Greatsword (2d6 slashing)")
        print("    - Warhammer  (1d8 bludgeoning)")
        print("    - Greataxe   (1d12 slashing)")
        print("    - Rapier     (1d8 piercing)")

        print("\n  SIMPLE WEAPONS:")
        print("    - Dagger     (1d4 piercing)")
        print("    - Handaxe    (1d6 slashing)")
        print("    - Quarterstaff (1d6 bludgeoning)")
        print("    - Spear      (1d6 piercing)")
        print("    - Mace       (1d6 bludgeoning)")

        weapon = get_choice(
            "Select your Weapon:",
            ["Longsword", "Battleaxe", "Greatsword", "Warhammer", "Greataxe", "Rapier", "Dagger", "Handaxe",
             "Quarterstaff", "Spear", "Mace"]
        )

    else:
        print("You have access to Simple weapons")
        print("\n  SIMPLE WEAPONS:")
        print("    - Dagger     (1d4 piercing)")
        print("    - Handaxe    (1d6 slashing)")
        print("    - Quarterstaff (1d6 bludgeoning)")
        print("    - Spear      (1d6 piercing)")
        print("    - Mace       (1d6 bludgeoning)")

        weapon = get_choice(
            "Select your Weapon",
            ["Dagger", "Handaxe", "Quarterstaff", "Spear", "Mace"]
        )

    print(f"\n  You selected: {weapon}")
    return weapon


def ranged_weapon_selection(subclass):
    if subclass == "Barbarian" or subclass == "Fighter" or subclass == "Paladin" or subclass == "Ranger":
        print("You have access to Martial and Simple Ranged Weapons please select the type of weapon below")
        print("\n  MARTIAL WEAPONS:")
        print("    - Longbow        (1d8 piercing)")
        print("    - Heavy Crossbow (1d10 piercing)")
        print("    - Hand Crossbow  (1d6 piercing)")
        print("    - Blowgun        (1 piercing)")

        print("\n  SIMPLE WEAPONS:")
        print("    - Light Crossbow (1d8 piercing)")
        print("    - Shortbow       (1d6 piercing)")
        print("    - Sling          (1d4 bludgeoning)")
        print("    - Dart           (1d4 piercing)")

        ranged = get_choice(
            "Select your Ranged Weapon:",
            ["Longbow", "Heavy Crossbow", "Hand Crossbow", "Blowgun",
             "Light Crossbow", "Shortbow", "Sling", "Dart"]
        )

    else:
        print("You have access to Simple Ranged Weapons, please select below")
        print("\n  SIMPLE WEAPONS:")
        print("    - Light Crossbow (1d8 piercing)")
        print("    - Shortbow       (1d6 piercing)")
        print("    - Sling          (1d4 bludgeoning)")
        print("    - Dart           (1d4 piercing)")

        ranged = get_choice(
            "Select your Ranged Weapon:",
            ["Light Crossbow", "Shortbow", "Sling", "Dart"]
        )

    print(f"\n  You selected: {ranged}")
    return ranged


def shield_selection(weapon, ranged_weapon=None):
    two_handed_weapon = ["Greatsword", "Greataxe", "Longbow", "Heavy Crossbow"]

    if weapon in two_handed_weapon or ranged_weapon in two_handed_weapon:
        print("The Weapon you have equipped requires 2 hands to use, you cannot equip a Shield")
        return "No"

    shield = get_choice(
        "Would you like a Shield",["Yes", "No"])
    if shield== "Yes":
           print(" You have equipped a Shield")
    elif shield == "No":
           print(" You have not equipped a Shield")
    return shield


def choose_race():
    race = get_choice(
        "What Race would you like to play as?",
        ["Human", "Half Elf", "Elf", "Orc", "Dwarf", "Halfling", "Tiefling", "Dragonborn"]
    )
    return race


def create_character():
    print("=============================")
    print("   D&D CHARACTER CREATOR     ")
    print("=============================")

    name = input("\nWhat is your character's name? ").strip()
    while not name:
        name = input("  Name cannot be empty. Try again: ").strip()

    race = choose_race()
    print(f"\n  You chose: {race}")
    input("\nPress Enter to continue...")

    role = get_choice(
        "What role would you like to play?",
        ["Warrior", "Mage", "Half Caster"]
    )

    if role == "Warrior":
        subclass = get_choice(
            "What type of Warrior would you like to play?",
            ["Fighter", "Rogue", "Barbarian", "Monk"]
        )
    elif role == "Mage":
        subclass = get_choice(
            "What type of Mage would you like to play?",
            ["Wizard", "Sorcerer", "Druid", "Cleric", "Bard"]
        )
    elif role == "Half Caster":
        subclass = get_choice(
            "What type of Half-Caster would you like to play?",
            ["Paladin", "Artificer", "Warlock", "Ranger"]
        )

    describe_class(subclass)
    input("\nPress Enter to continue...")

    weapon = weapon_selection(subclass)
    input("\nPress Enter to continue...")

    ranged = ranged_weapon_selection(subclass)
    input("\nPress Enter to continue...")

    shield = shield_selection(weapon, ranged)

    print("\n=============================")
    print("       YOUR CHARACTER        ")
    print("=============================")
    print(f"  Name:   {name}")
    print(f"  Race:   {race}")
    print(f"  Role:   {role}")
    print(f"  Class:  {subclass}")
    print(f"  Weapon: {weapon}")
    print(f"  Ranged: {ranged}")
    print(f"  Shield: {shield}")
    print("=============================")

    again = input("\nWould you like to create another character? (yes/no): ").strip().lower()
    if again == "yes":
        create_character()
    else:
        print("\nGood luck on your adventure!\n")


create_character()