class Player:

    def __init__(self):
        self.gold_coins = 0
        self.lives = 5
        self.health_points = 10

    def __str__(self):
        return "player has {} lives and {} health points and {} coins".format(self.lives, self.health_points, self.gold_coins)
 
    def level_up(self):
        self.lives +=1
        return self.lives

    def collect_treasure(self,treasure=None):
        if treasure:
            self.gold_coins += treasure
        else:
            self.gold_coins +=1
        if self.gold_coins % 10 == 0:
            self.level_up()
        return self.gold_coins

    def do_battle(self, damage):
        self.health_points = self.health_points - damage
        if self.health_points < 1:
            self.lives -= 1 
            self.health_points = 10
        if self.lives == 0:
                self.restart()
        return self.health_points

    def restart(self):
        self.gold_coins = 0
        self.lives = 5
        self.health_points = 10
        print("I have been restarted")

john = Player()
print(john.lives)
print("health points =",john.do_battle(10))
print(john.lives)
print("health points =",john.do_battle(20))
print(john.lives)
print("health points =",john.do_battle(30))
print(john.lives)
print("health points =",john.do_battle(10))
print(john.lives)
print("health points =",john.do_battle(10))
print(john.lives)


# my_player = Player()
# my_player.collect_treasure()
# my_player.collect_treasure()
# my_player.collect_treasure()
# my_player.collect_treasure()
# my_player.collect_treasure()
# my_player.collect_treasure()
# my_player.collect_treasure()
# my_player.collect_treasure()
# my_player.collect_treasure()
# print(my_player.collect_treasure())
# print(my_player.lives)


# my_player.collect_treasure()
# print(my_player.gold_coins, my_player.lives)

# print(my_player.lives)
# #         print(self.gold_coins)

# # my_player = Player()
# # print(my_player.lives)

# # my_2nd_palyer = Player()
# # my_2nd_palyer.gold_coins = 10
# # my_player.gold_coins = 7

# # print('my_2nd_palyer.gold_coins: ',my_2nd_palyer.gold_coins)

# # print('my_player.gold_coins:', my_player.gold_coins)
