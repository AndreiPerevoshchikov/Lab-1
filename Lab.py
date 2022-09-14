import csv
search = input('Поиск книги')
f = open('result.txt', 'w')
flag = 0
with open('books.csv', 'r') as csvfile:
    books = csv.reader(csvfile, delimiter=';')
# задание 1
    print(len(list(books))-1)

    title = 0
    for row in list(books):
        if len(row['Название']) > 30:
            title += 1
    print(title)

    for row in list(books):
        lower_case = row[3, 4].lower()
        index = lower_case.find(search.lower())
        if (index != -1):
            print(len(row[1]))
            flag = 1
            f.write(row[1] + '.' + row[3] + '. Стоимость ' + row[4] + 'рублей.\n')

    if (flag == 0):
        print('Nothing found')

