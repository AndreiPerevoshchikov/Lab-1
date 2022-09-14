import csv
#search = input('Поиск книги')
f = open('result.txt', 'w')
#flag = 0
with open('books.csv', 'r') as csvfile:
    books = csv.reader(csvfile, delimiter=';')
# задание 1
    z = -1
    title = 0
    author = input('Введите желаемого автора: ')
    search = input('Введите 1, если хотите ввести 20 ID книг для библиографической ссылки, иначе введите 0 для случайного набора ')
    id_array = []
    flag = 0
    bible = 20
    if search == '1':
        for i in range(bible):
            id_array.append(input('Введите ID искомой книги '))
    else:
        flag = 1


    for row in books:
        z += 1
        if len(row[1]) > 30:
            title += 1

        year = row[6].split()
        year = year[0].split('.')
        year = year[-1]

        surname = row[3].split()
        surname = surname[-1:]
        if len(surname)>0:
            if (author == str(surname[0])) and int(year) < 2016:
                print(row[1])

        if flag == 0:
            if row[0] in id_array:
                f.write('<' + str(surname[0]) + '>. <' + str(row[1]) + '> - <' + str(year) + '>' + '\n')
        elif(flag == 1) and (z < 22) and (z > 1):
            f.write('<' + str(surname[0]) + '>. <' + str(row[1]) + '> - <' + str(year) + '>' + '\n')



    print(z)
    print(title)
f.close()



