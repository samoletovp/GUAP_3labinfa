#file lab3infa2var.py
#author Petr Samoletov <samoletovp@gmail.com>
#brief 20. Ввести строку и букву, вывести только слова, заканчивающиеся на заданную букву.

input_string = input("Enter words with spaces: ")
input_letter = input("Enter one letter: ")
while len(input_letter) > 1:
    input_letter = input("You need to enter one letter: ")
words = []
input_string = input_string.split()
for i in range(len(input_string)):
    if input_string[i][-1] == input_letter:
        words.append(input_string[i])
print(" ".join(words))