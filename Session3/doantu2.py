from random import shuffle, choice
array = ['brother','dude','hell','grenade','smoke']
word=choice(array)
split=list(word)
shuffle(split)
print(*split,sep=' ')
count=0
playing=True
while playing:
    guess=str(input('guess the word: '))
    if guess!=word:
        print('wrong')
    else:
        print('right answer!')
        playing=False
    count +=1
    if count ==4:
        print ('GG')
        playing = False
