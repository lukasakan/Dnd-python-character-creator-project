import sqlite3


weapon_base_stats = [("axe", "bar", 13,"images/Battleaxe-of-Fury-featured.jpg"),
                     ("greatsword", "bar", 12, "images/Bloodshed-Greatsword-featured.jpg"),
                     ("hammer", "bar", 11,"images/Storm-Hammer-featured.jpg"),
                     ("daggers", "rog", 7, "images/Dagger-of-the-Falling-Skies-featured.jpg"),
                     ("short sword", "rog", 9, "images/Dream-Reaver-featured.jpg"),
                     ("short bow", "rog", 9, "images/1519c5655808e16001815d461f5fa59a.jpg"),
                     ("short bow", "ranged", 9, "images/1519c5655808e16001815d461f5fa59a.jpg"),
                     ("long bow", "ranged", 10, "images/Infernal-Longbow-featured.jpg"),
                     ("crossbow", "ranged", 13, "images/Hunters-Crossbow-featured.jpg"),
                     ("staff", "wiz", 5, "images/Staff-of-the-Star-Stone-featured.jpg"),
                     ("scepter", "wiz", 2, "images/The-Blood-Scepter-featured.jpg"),
                     ("tome", "wiz", 2, "images/g3phyq3lmv571.png"),
                     ("wand", "sor", 1, "images/Wand-of-the-Waverider-featured.jpg"),
                     ("dagger", "sor", 7, "images/Dagger-of-the-Falling-Skies-featured.jpg"),
                     ("sword", "sor", 10,"images/Sword-of-Solaris-featured.jpg"),
                     ("staff", "dru", 5, "images/Staff-of-the-Star-Stone-featured.jpg"),
                     ("spear", "dru", 10, "images/Champion-Spear-featured.jpg"),
                     ("mace", "dru", 11, "images/Social-Media-post-1080-Mace-of-Domination-1024x1024.jpg"),
                     ("mace", "pal", 11,"images/Social-Media-post-1080-Mace-of-Domination-1024x1024.jpg"),
                     ("hammer", "pal", 11, "images/Storm-Hammer-featured.jpg"),
                     ("spear", "pal", 10,"images/Champion-Spear-featured.jpg"),
                     ("flute", "musical", 2, "images/Social-Media-post-1080-Flute-of-the-Faun-1024x1024.jpg"),
                     ("lyre", "musical", 3, "images/9127a7c71d040e6f2d4f7cfe67dcb7cc.jpg"),
                     ("viola", "musical", 4, "images/2ac070fa7b8b59c992d5cfec4aefa16c.jpg"),
                     ("staff", "heal", 5, "images/Staff-of-the-Star-Stone-featured.jpg"),
                     ("axe", "heal", 13, "images/Battleaxe-of-Fury-featured.jpg"),
                     ("sword", "heal", 10, "images/Sword-of-Solaris-featured.jpg")
                     ]


def char_database():
    conn = sqlite3.connect("dnd.db")
    cursor = conn.cursor()


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dnd (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            race TEXT NOT NULL,
            char_class TEXT NOT NULL,
            level INTEGER NOT NULL,
            strength INTEGER NOT NULL,
            constitution INTEGER NOT NULL,
            wisdom INTEGER NOT NULL,
            intelligence INTEGER NOT NULL,
            charisma INTEGER NOT NULL,
            dexterity INTEGER NOT NULL,
            weapon TEXT 
        )
    ''')


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weapons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            damage INTEGER NOT NULL,
            images TEXT
        )
    ''')


    cursor.executemany('''
         INSERT OR IGNORE INTO weapons (name, type, damage,images)
        VALUES (?, ?, ?, ?)
    ''', weapon_base_stats)

    conn.commit()
    conn.close()


char_database()




def add_character(name, race, char_class, level, stats, weapon):
    conn = sqlite3.connect('dnd.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO dnd (name, race, char_class, level, strength, constitution, wisdom, intelligence, charisma, dexterity, weapon)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, race, char_class, level,
          stats['strength'], stats['constitution'], stats['wisdom'],
          stats['intelligence'], stats['charisma'], stats['dexterity'], weapon))
    conn.commit()
    conn.close()


    
   










def fetch_characters():
    conn = sqlite3.connect('dnd.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dnd')
    rows = cursor.fetchall()
    conn.close()
    return rows