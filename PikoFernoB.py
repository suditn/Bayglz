import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Рогалики, дедуктивно-логическая игра. Автор Эл Свейгарт al@inventwithpython.comI я думаю о {}-значном числе без повторяющихся цифр. Попробуйте угадать, что это такое. Вот несколько подсказок: Когда я говорю: Это означает: 
У Пико одна цифра правильная, но в неправильном положении. 
У Ферми одна цифра правильная и в правильном положении. 
У бубликов ни одна цифра не правильная. Например, если секретное число было 248, а ваше предположение - 843, подсказками были бы Ферми Пико.'''.format(NUM_DIGITS))

    while True:
    
        secretNum = getSecretNum()
        print('- Я придумал номер.')
        print('У вас есть {} догадки, чтобы получить это.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''

            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print ('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess,secretNum)
            print(clues)
            numGuesses +=1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('У вас закончились догатки')
                print('Ответом было число {}.'.format(secretNum))


        print('Хотите сыграть снова?(y or n)')
        if not input('> ').lower().startswith('y'):
            break

    print ('Спасибо за игру')

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range (NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'Ты угадал'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Ферми')
        elif guess[i] in secretNum[i]:
            clues.append('Пико')

    if len(clues)==0:
        return 'Пирожки'
    else:
        clues.sort()
        return ' '.join(clues)



if __name__ == '__main__':
    main()
