import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from models.models import get_db

def seed_lookup_tables():
    with get_db() as conn:

        # Lookup tables
        conn.executemany(
            "INSERT INTO CharacterClass (ClassName, Description) VALUES (?, ?)",
            [
                ("Knight", "A heavily armored noble warrior."),
                ("Archer", "A master of ranged combat."),
                ("Mage", "A wielder of arcane magic."),
                ("Cleric", "A healer devoted to the divine."),
                ("Rogue", "A stealthy and cunning operative."),
                ("Barbarian", "A fierce and untamed fighter.")
            ]
        )

        conn.executemany(
            "INSERT INTO Species (SpeciesName) VALUES (?)",
            [
                ("Human",),
                ("Elf",),
                ("Dwarf",),
                ("Orc",),
                ("Halfling",),
                ("Tiefling",)
            ]
        )

        conn.executemany(
            "INSERT INTO Alignment (AlignmentName) VALUES (?)",
            [
                ("Lawful Good",),
                ("Neutral Good",),
                ("True Neutral",),
                ("Chaotic Neutral",),
                ("Lawful Evil",),
                ("Chaotic Evil",)
            ]
        )

        conn.executemany(
            "INSERT INTO ItemType (TypeName) VALUES (?)",
            [
                ("Weapon",),
                ("Armor",),
                ("Potion",),
                ("Scroll",),
                ("Accessory",),
                ("Tool",)
            ]
        )

        conn.executemany(
            "INSERT INTO Rarity (RarityName) VALUES (?)",
            [
                ("Common",),
                ("Uncommon",),
                ("Rare",),
                ("Epic",),
                ("Legendary",),
                ("Mythic",)
            ]
        )

        conn.executemany(
            "INSERT INTO Region (RegionName) VALUES (?)",
            [
                ("Kingdom of Eldoria",),
                ("Whispering Woods",),
                ("Ironhold Mountains",),
                ("Blackmarsh Swamp",),
                ("Silverkeep Citadel",),
                ("Ashen Plains",)
            ]
        )

        conn.executemany(
            "INSERT INTO Difficulty (DifficultyName) VALUES (?)",
            [
                ("Trivial",),
                ("Easy",),
                ("Moderate",),
                ("Hard",),
                ("Deadly",),
                ("Legendary",)
            ]
        )

        # Core data
        conn.executemany(
            """INSERT INTO Character 
               (CharacterName, ClassID, SpeciesID, AlignmentID, Level)
               VALUES (?, ?, ?, ?, ?)""",
            [
                ("Sir Aldric", 1, 1, 1, 10),
                ("Lyra Swiftarrow", 2, 2, 2, 8),
                ("Thorin Stonebeard", 6, 3, 4, 12),
                ("Elandra the Wise", 3, 2, 3, 15),
                ("Brother Caldus", 4, 1, 1, 9),
                ("Shade Nightfoot", 5, 5, 4, 11)
            ]
        )

        conn.executemany(
            """INSERT INTO Item (ItemName, ItemTypeID, RarityID)
               VALUES (?, ?, ?)""",
            [
                ("Iron Sword", 1, 1),
                ("Steel Plate Armor", 2, 3),
                ("Healing Potion", 3, 1),
                ("Scroll of Fireball", 4, 4),
                ("Ring of Protection", 5, 5),
                ("Lockpick Set", 6, 2)
            ]
        )

        conn.executemany(
            """INSERT INTO Quest (QuestName, RegionID, DifficultyID)
               VALUES (?, ?, ?)""",
            [
                ("Defeat the Bandit Leader", 1, 2),
                ("Rescue the Lost Merchant", 2, 3),
                ("Clear the Goblin Caves", 3, 4),
                ("Purge the Swamp Witch", 4, 5),
                ("Defend Silverkeep", 5, 4),
                ("Slay the Ashen Dragon", 6, 6)
            ]
        )

        conn.commit()
        print("Seeded everything (Medieval Edition ⚔️)")

if __name__ == "__main__":
    seed_lookup_tables()