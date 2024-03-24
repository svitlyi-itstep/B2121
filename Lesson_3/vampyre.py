from Lesson_2.character import Character


class Vampyre(Character):
    def __init__(self, name, health=100, damage=1, defence=0):
        super().__init__(name, health, damage, defence)


    def attack(self, target):
        vampiric_damage = target.take_damage(self.damage)
        self.health += max(vampiric_damage * 0.1, 0)
        return vampiric_damage
