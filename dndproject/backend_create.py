

class_base_stats = {
    'Barbarian': {'strength': 15, 'constitution': 15, 'wisdom': 3, 'intelligence': 2, 'charisma': 3, 'dexterity': 4},
    'Rogue': {'strength': 6, 'constitution': 6, 'wisdom': 4, 'intelligence': 4, 'charisma': 4, 'dexterity': 12},
    'Ranger': {'strength': 7, 'constitution': 8, 'wisdom': 5, 'intelligence': 4, 'charisma': 4, 'dexterity': 10},
    'Wizard': {'strength': 4, 'constitution': 5, 'wisdom': 6, 'intelligence': 12, 'charisma': 4, 'dexterity': 5},
    'Sorcerer': {'strength': 4, 'constitution': 6, 'wisdom': 6, 'intelligence': 9, 'charisma': 7, 'dexterity': 5},
    'Druid': {'strength': 5, 'constitution': 6, 'wisdom': 10, 'intelligence': 8, 'charisma': 5, 'dexterity': 4},
    'Paladin': {'strength': 10, 'constitution': 10, 'wisdom': 4, 'intelligence': 5, 'charisma': 7, 'dexterity': 4},
    'Bard': {'strength': 5, 'constitution': 7, 'wisdom': 6, 'intelligence': 7, 'charisma': 10, 'dexterity': 5},
    'Cleric': {'strength': 7, 'constitution': 8, 'wisdom': 12, 'intelligence': 5, 'charisma': 6, 'dexterity': 4}
}

race_modifiers = {
    'Human':        {'strength': 1, 'constitution': 1, 'wisdom': 0, 'intelligence': 0, 'charisma': 0, 'dexterity': 1},
    'Elf':          {'strength': -1, 'constitution': -1, 'wisdom': 1, 'intelligence': 2, 'charisma': 1, 'dexterity': 2},
    'Dwarf':        {'strength': 1, 'constitution': 2, 'wisdom': 0, 'intelligence': 0, 'charisma': -1, 'dexterity': -1},
    'Halfling':     {'strength': -1, 'constitution': 0, 'wisdom': 0, 'intelligence': 1, 'charisma': 1, 'dexterity': 2},
    'Orc':          {'strength': 2, 'constitution': 2, 'wisdom': -2, 'intelligence': -2, 'charisma': -1, 'dexterity': 0},
    'Tiefling':     {'strength': 0, 'constitution': 0, 'wisdom': 0, 'intelligence': 2, 'charisma': 2, 'dexterity': 0},
    'Drow':         {'strength': 0, 'constitution': -1, 'wisdom': 0, 'intelligence': 2, 'charisma': 2, 'dexterity': 2},
    'Dragonborn':   {'strength': 2, 'constitution': 1, 'wisdom': 0, 'intelligence': 0, 'charisma': 1, 'dexterity': 0}
}

class_weapon_type = {
    'Barbarian': 'bar',
    'Rogue': 'rog',
    'Ranger': 'ranged',
    'Wizard': 'wiz',
    'Sorcerer': 'sor',
    'Druid': 'dru',
    'Paladin': 'pal',
    'Bard': 'musical',
    'Cleric': 'heal'
}


class CharacterManager:
    def __init__(self):
        self.remaining_points = 8

    def calculate_base_stats(self, selected_class, selected_race):
        if selected_class and selected_race:
            class_stats = class_base_stats.get(selected_class, {})
            race_bonus = race_modifiers.get(selected_race, {})
            
            calculated_stats = {}
            for stat in ['strength', 'dexterity', 'constitution', 'wisdom', 'intelligence', 'charisma']:
                base = class_stats.get(stat, 0) + race_bonus.get(stat, 0)
                calculated_stats[stat] = base
            return calculated_stats
        return {}

    def update_remaining_points(self, selected_class, selected_race, current_stat_values):
        class_stats = class_base_stats.get(selected_class, {})
        race_bonus = race_modifiers.get(selected_race, {})
        total_used = 0

        for stat, value in current_stat_values.items():
            base = class_stats.get(stat, 0) + race_bonus.get(stat, 0)
            total_used += value - base

        self.remaining_points = 8 - total_used
        return self.remaining_points

    def get_weapon_type_for_class(self, selected_class):
        return class_weapon_type.get(selected_class, 'bar')