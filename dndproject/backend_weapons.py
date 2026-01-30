import sqlite3
from database import add_character


def get_weapons_by_type(weapon_type):
    conn = sqlite3.connect("dnd.db")
    cursor = conn.cursor()
    cursor.execute('''
        SELECT name, images FROM weapons
        WHERE type = ?
        LIMIT 3
    ''', (weapon_type,))
    weapons = cursor.fetchall()
    conn.close()
    return weapons


def confirm_weapon(character_data, selected_weapon):
    if not character_data or not selected_weapon:
        return False, "Missing data"

    try:
        add_character(
            character_data['name'],
            character_data['race'],
            character_data['char_class'],
            character_data['level'],
            character_data['stats'],
            selected_weapon
        )
        return True, f"{character_data['name']} was added with weapon: {selected_weapon}"
    except Exception as e:
        return False, str(e)
