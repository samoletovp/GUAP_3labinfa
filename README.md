# GUAP_3labinfa
3 лабораторная по курсу Информатика (ГУАП 1 курс 1 семестр)

Задание лабораторной: 20. Ввести строку и букву, вывести только слова, заканчивающиеся на заданную букву.

1. Код получает от пользователя с клавиатуры строку и букву, на которую должны оканчиваться слова.
2. Проверка циклом while на то, чтобы пользователь вводил конкретно одну буквы, на которую должны заканчиваться слова.
3. Создается список с названием words
4. Введенная строка разделяется по пробелам функцией .split()
5. Запускается цикл, который при помощи среза определяет последнюю букву и, если она совпадает с введенной пользователем буквой, добавляет в список words
6. Вывод списка words с использованием функции .join() для отображения без символов 
