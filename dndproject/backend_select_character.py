
from database import fetch_characters

class CharacterSelectionManager:


    def __init__(self):
        self._characters_data = []

    def load_characters(self):

        raw_characters = fetch_characters()
        

        
        self._characters_data = []
        for char_tuple in raw_characters:

            character_dict = {
                'id': char_tuple[0],
                'name': char_tuple[1],
                'race': char_tuple[2],
                'char_class': char_tuple[3],
                'level': char_tuple[4],
                'strength': char_tuple[5],
                'constitution': char_tuple[6],
                'wisdom': char_tuple[7],
                'intelligence': char_tuple[8],
                'charisma': char_tuple[9],
                'dexterity': char_tuple[10],
                'weapon': char_tuple[11]
            }
            self._characters_data.append(character_dict)
            

        return [(c['id'], c['name']) for c in self._characters_data]

    def get_character_details(self, character_id):

        character = next((c for c in self._characters_data if c['id'] == character_id), None)

        if character:

            details = (
                f"Name: {character['name']}\n"
                f"Race: {character['race']}\n"
                f"Class: {character['char_class']}\n"
                f"Level: {character['level']}\n"
                f"Strength: {character['strength']}\n"
                f"Constitution: {character['constitution']}\n"
                f"Wisdom: {character['wisdom']}\n"
                f"Intelligence: {character['intelligence']}\n"
                f"Charisma: {character['charisma']}\n"
                f"Dexterity: {character['dexterity']}\n"
            )
            if character['weapon']:
                details += f"Weapon: {character['weapon']}\n"
            return details
        return "Character not found."

