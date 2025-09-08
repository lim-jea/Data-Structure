import random 

class GaemEntry:
    def __init__(self, name, score):
        self._name = name
        self._score = score
    def get_name(self):
        return self._name
    def get_score(self):
        return self._score
    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)

class Scroeboard:
    def __init__(self, capacity =10):
        self._board = [None] * capacity # Array of game entries
        self._n = 0                     # Number of actual entries
    
    def __getitem__(self,k):
        return self._board[k]

    def __str__(self):
        return '\n'.join(str(self._board[j]) for j in range(self._n))
    
    def add(self, entry):
        score = entry.get_score()
        # Is the new entry a high score?
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1
            
            j = self._n - 1
            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j - 1]
                j -= 1  
            self._board[j] = entry  
    

def main():
    board = Scroeboard()    # Default capacity is 10 Scoreboard(5)
    names = ['Alice', 'Bob', 'Cindy', 'Derek', 'Edith', 'Frank', 'Greta']
    for i in range(10):
        name = random.choice(names)
        score = random.randint(1,100)
        entry = GaemEntry(name, score)
        board.add(entry)
        print('Scoreboard after adding: ')
        print(board)

if __name__ == "__main__":
    main()
    
