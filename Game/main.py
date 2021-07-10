from enemy import Enemy, Troll, Vampyre, VampyreKing

dracula = VampyreKing("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)


# ugly_troll = Troll("Pug")
# print("Ugly troll - {}".format(ugly_troll))
#
# another_troll = Troll("Ug")
# print("Another troll - {}".format(another_troll))
# another_troll.take_damage(18)
# print(another_troll)
#
# brother = Troll("Urg")
# print(brother)
#
# ugly_troll.grunt()
# another_troll.grunt()
# brother.grunt()
#
# vamp = Vampyre("Vlad")
# print(vamp)
# vamp.take_damage(5)
# print(vamp)
#
# print("-" * 40)
# another_troll.take_damage(30)
# print(another_troll)
#
# # while vamp.alive:
# #     vamp.take_damage(1)
#         # print(vamp)
#
# vamp._lives = 0
# vamp._hit_points = 1
# print(vamp)
#
# random_monster = Enemy("Basic enemy", 12, 1)
# print(random_monster)
#
# random_monster.take_damage(4)
# print(random_monster)
#
# random_monster.take_damage(8)
# print(random_monster)
#
# random_monster.take_damage(9)
# print(random_monster)
#
# from player import Player
#
# vegita = Player("Vegita")
#
# print(vegita.name)
# print(vegita.lives)
# vegita.lives -= 1
# print(vegita)
#
# vegita.lives -= 1
# print(vegita)
#
# vegita.lives -= 1
# print(vegita)
#
# vegita.lives -= 1
# print(vegita)
#
# vegita._lives = 9
# print(vegita)
#
# vegita.level = 2
# print(vegita)
#
# vegita.level += 5
# print(vegita)
#
# vegita.level = 3
# print(vegita)