from Lesson_2.character import Character
from berserk import Berserk
from vampyre import Vampyre
from knight import Knight


player1 = Vampyre('Vampyre', damage=15)
player1.show_info()

player2 = Berserk('Berserk', damage=10)
print(player2)

player3 = Knight('Knight', damage=0, defence=150)
print(player3)

while player1.is_alive() and player3.is_alive():
      p1_damage = player1.attack(player3)
      print(f'{player1.name} атакував {player3.name} '
            f'і наніс {p1_damage} шкоди.')

      # p2_damage = player2.attack(player1)
      # print(f'{player2.name} атакував {player1.name} '
      #       f'і наніс {p2_damage} шкоди.')

      p3_damage = player3.attack(player1)
      print(f'{player3.name} атакував {player1.name} '
            f'і наніс {p3_damage} шкоди.')

      print(player1, player3, sep='\n')

