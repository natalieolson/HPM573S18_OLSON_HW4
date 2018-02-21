from enum import Enum
import numpy as np

class coin(Enum):
 #result of coin flip
    HEADS = 0
    TAILS = 1

class game(object):
    def __init__(self, id):
        self._id = id
        self._coin = coin.TAILS
        self._count_wins = 0
        self._count_tails = 0
        self._flip_number = 1
        self._total_flips = 20
        self._rnd = np.random
        self._rnd.seed(self._id * self._flip_number)

    def next_flip(self):
# use previous flip as "if" statement, then adjust tails and win count for next flip
        if self._coin == coin.TAILS:
            if self._rnd.random_sample() > 0.4:
                self._coin = coin.TAILS
                self._count_tails += 1

            if self._rnd.random_sample() < 0.4:
                if self._count_tails >= 2:
                    self._count_wins += 1
                self._coin = coin.HEADS
                self._count_tails = 0

        elif self._coin == coin.HEADS:
            if self._rnd.random_sample() > 0.4:
                self._coin = coin.TAILS
                self._count_tails = 1

            if self._rnd.random_sample() < 0.4:
                self._coin = coin.HEADS
                self._count_tails = 0

        self._flip_number += 1

    def play(self):
        for i in range(1, self._total_flips+1):
            self._rnd = np.random
            self._rnd.seed(self._id * self._flip_number)
            self.next_flip()

    def reward(self):
        self.play()
        self._payout = -250
        self._payout += 100*self._count_wins
        return self._payout

class cohort:
    # initialize empty list of players (1000 id's)
    def __init__(self, id, numPlayers):
        self._players = []
        n = 1
        while n <= numPlayers:
            player = game(id=id * numPlayers + n)
            self._players.append(player)
            n += 1

    def simulate(self):
        game_rewards = []
        for player in self._players:
            game_rewards.append(player.reward())
            #calculate average of all games
        return sum(game_rewards)/len(game_rewards)

estimate = cohort(id=1, numPlayers=1000)
print(estimate.simulate())
