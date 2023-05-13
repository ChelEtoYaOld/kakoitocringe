
class Cheliki:
    def __init__(self, name='Cheliki'):
        self.name = name


class Gaming:
    def __init__(self, game):
        self.game = game
        self.players = []

    def add_players(self, *mikrochely):
        self.players += mikrochely

    def print_players(self):
        if self.players:
            print(f'Names of players in {self.game}:')
            for p in self.players:
                print(p.name)
            else:
                print(f'Today nobody dont play in {self.game}:')

lolkekcheburek = Cheliki('LoLKeKCheburek')
vova228 = Cheliki('Vova228')
mrpingvin4ik = Cheliki('MrPingvin4ik')
game = Gaming('Roblox')
game.add_players(lolkekcheburek, vova228, mrpingvin4ik)
game.print_players()