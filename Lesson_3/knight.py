from Lesson_2.character import Character


class Knight(Character):
    def __init__(self, name, health=100, damage=1, defence=0):
        super().__init__(name, health, damage, defence)


    def take_damage(self, damage):
        final_damage = max(damage - (damage * self.defence / 100), 0)
        self.health -= final_damage
        return final_damage