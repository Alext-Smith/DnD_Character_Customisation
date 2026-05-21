import random

def roll_stat():
    rolls = [random.randint(1, 6) for _ in range(4)]
    lowest = min(rolls)
    rolls.remove(lowest)
    total = sum(rolls)
    return rolls, lowest, total

def all_stats():
    stats = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

    print("=============================")
    print("         STAT ROLLER         ")
    print("=============================")

    input("\nPress Enter to roll your stats: ")

    results = {}

    for stat in stats:
        rolls, lowest, total = roll_stat()
        results[stat] = total
        print(f"\n  {stat}")
        print(f"  Rolls: {rolls}, Drop Lowest: {lowest}")
        print(f"  Total: {total}")

    input("\nPress Enter to view your final stats: ")

    print("\n=============================")
    print("        FINAL STATS          ")
    print("=============================")

    for stat in results:
        print(f"  {stat}: {results[stat]}")

    print("=============================")

all_stats()