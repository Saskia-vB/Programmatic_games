# dictionary
# assign a value(points) to keys (letters)

# sum of the values of they keys being called out


while True:

    score = {"a": 1 , "b": 3 , "c": 3 , "d": 2 ,
             "e": 1 , "f": 4 , "g": 2 , "h": 4 ,
             "i": 1 , "j": 8 , "k": 5 , "l": 1 ,
             "m": 3 , "n": 1 , "o": 1 , "p": 3 ,
             "q": 10, "r": 1 , "s": 1 , "t": 1 ,
             "u": 1 , "v": 4 , "w": 4 , "x": 8 ,
             "y": 4 , "z": 10}


    def scrabble_score(word):
        total = 0
        if len(word) != 5:
            return "Your word has to be 5 letters long"
        elif len(word) == 5:
            for letter in word:
                total += score[letter]
            return total


    word = input("Choose your 5 letter word: ")
    print(scrabble_score(word))


## def scrabble_calc(word):
##      return sum(score[letter] for letter in word)
