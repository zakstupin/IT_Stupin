# TODO Найдите количество книг, которое можно разместить на дискете
disk = 1.44 * 1024 * 1024
pages = 100
strings = 50
symbols = 25
one_symbol = 4
book = one_symbol * symbols * strings * pages
print("Количество книг, помещающихся на дискету:", int(disk//book))
