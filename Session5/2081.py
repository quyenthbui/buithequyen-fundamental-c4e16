import string
sentence = input("Type something here: ").lower()
alphabet = list(string.ascii_lowercase)
for i in range(26):
    times = sentence.count(alphabet[i])
    print(alphabet[i], times)
