from character import Character


player1 = Character('Vasya')
player1.show_info()

player2 = Character('Petya', damage=2)
print(player2)

'''
      Зробити так, щоб персонажі атакували
      одне одного до тих пір, доки в одного
      з персонажів не закінчиться здоров'я
'''

p1_damage = player1.attack(player2)
print(f'{player1.name} атакував {player2.name} '
      f'і наніс {p1_damage} шкоди.')
p2_damage = player2.attack(player1)
print(f'{player2.name} атакував {player1.name} '
      f'і наніс {p2_damage} шкоди.')

print(player1, player2, sep='\n')