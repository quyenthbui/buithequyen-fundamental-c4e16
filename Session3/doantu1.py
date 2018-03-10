from random import shuffle

word='deptrai'
split=list(word)
shuffle(split)
print(*split,sep=' ')


playing=True
count=0
while playing:
    guess=str(input('guess a word: '))
    if guess!=word:
        print(':( wrong!')

    else:
        print('right answer!')
        playing=False
    count+=1
    if count==3:
        print('you loose!!!')
        playing =False
