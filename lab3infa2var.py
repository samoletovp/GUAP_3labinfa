#20.  Ввести строку и букву, вывести только слова, заканчивающиеся на заданную букву.

inputstring = input("Enter words with spaces: ")
inputletter = input("Enter one letter: ")
while len(inputletter) > 1:
    inputletter = input("You need to enter one letter: ")
words = []
inputstring = inputstring.split()
for i in range(len(inputstring)):
    if inputstring[i][-1] == inputletter:
        words.append(inputstring[i])
print(" ".join(words))