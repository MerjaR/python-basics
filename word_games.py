# Three word games that inherit class WordGame
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):

    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        if len(player2_word) > len(player1_word):
            return 2

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        i = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        word1 = 0
        word2 = 0
        for i in range(0, len(player1_word)):
            char = player1_word[i]
            if char in vowels:
                word1 += 1
        for i in range(0, len(player2_word)):
            char = player2_word[i]
            if char in vowels:
                word2 += 1
        
        if word1 > word2:
            return 1
        if word2 > word1:
            return 2

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        moves = ["rock", "paper", "scissors"]
        if player1_word not in moves and player2_word not in moves:
            pass
        elif player1_word in moves and player2_word not in moves:
            return 1
        elif player2_word in moves and player1_word not in moves:
            return 2
        elif player1_word == "rock" and player2_word == "scissors":
            return 1
        elif player2_word == "rock" and player1_word == "scissors":
            return 2
        elif player1_word == "paper" and player2_word == "rock":
            return 1
        elif player2_word == "paper" and player1_word == "rock":
            return 2
        elif player1_word == "scissors" and player2_word == "paper":
            return 1
        elif player2_word == "scissors" and player1_word == "paper":
            return 2

if __name__ == "__main__":
    p = MostVowels(3)
    p.play()
        







