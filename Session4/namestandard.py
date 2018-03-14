s=str(input('Your full name: '))
words = s.split()
for i in range(len(words)):
    words[i] = words[i].capitalize()
print('Updated: ', ' '.join(words))
