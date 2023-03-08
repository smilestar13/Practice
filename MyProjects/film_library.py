import random


class Film:

    def __init__(self, name, year, genre, views=0):
        self.name = name
        self.year = year
        self.genre = genre
        self.views = views

    def set_views(self, new_views):
        self.views = new_views

    def play(self):
        self.views += 1

    def __str__(self):
        return f'{self.name} ({self.year}) {self.views}'


class Serial(Film):

    def __init__(self, name, year, genre, series=1, seasons=1, views=0):
        super().__init__(name, year, genre, views)
        self.series = series
        self.seasons = seasons

    def set_series(self, new_series):
        self.series = new_series

    def set_seasons(self, new_seasons):
        self.seasons = new_seasons

    def __str__(self):
        return f'{self.name} S{str(self.seasons).zfill(2)}E{str(self.series).zfill(2)}'


class Library:

    def __init__(self):
        self.library = []

    def add_media(self, serial):
        self.library.append(serial)

    def get_movies(self):
        movies = []
        for el in self.library:
            if type(el) is Film:  # Проверка на тип
                movies.append(el)
        movies = sorted(movies, key=lambda el: el.name)
        return movies

    def get_series(self):
        series = []
        for el in self.library:
            if type(el) is Serial:
                series.append(el)
        series = sorted(series, key=lambda el: el.name)
        return series

    def search(self, name):
        for st in self.library:
            if name in str(st.name):
                return st.name

    def generate_views(self):
        res = random.choice(self.library)
        res.set_views(res.views + random.randint(0, 100))

    def generate_views_x10(self, start=0, stop=10):
        for i in range(start, stop):
            self.generate_views()

    def top_titles(self, n):
        res = sorted(self.library, key=lambda x: x.views, reverse=True)  # Сортировка
        return res[:n]  # Срез

    def __str__(self):
        all_media = ''
        for el in self.library:
            all_media += f'{el}\n'
        return all_media.rstrip()


f1 = Film('Avatar', 2006, 'Fantasy', 1000)  # Создаем фильмы, четвертый параметр по дефолту ноль и не обязательный
f2 = Film('Start', 1997, 'Horror')
f2.set_views(10)  # Переопределяем параметр количества просмотров для второго фильма с 0 на 10
f3 = Serial('Kekas', 2012, 'Trill')  # Создаем так же сериалы
f4 = Serial('Simpsons', 2008, 'Cartoons')
f4.play()  # Смотрим сериал и накручиваем +1 просмотр
f5 = Serial('Boabob', 2022, 'Comedy', 12, 22)

lib = Library()  # Создаем ту самую библиотеку со всем вместе
lib.add_media(f5)
lib.add_media(f4)
lib.add_media(f3)
lib.add_media(f2)
lib.add_media(f1)
print("---------- LIB ----------")
print(lib)  # Выводим всю библиотеку на экран

print("---------- Movies ----------")
print(lib.get_movies())  # Выводим только фильмы

print("---------- Search Boabob ----------")
print(lib.search('Boabob'))  # Ищем фильм которые есть в библиотеке
print("---------- Search Boabobs ----------")
print(lib.search('Boabobs'))  # Ищем фильм которого нет в библиотеке

lib.generate_views()  # Накручиваем рандомные просмотры на рандомный фильм
lib.generate_views_x10()  # Накручиваем рандомные просмотры на рандомный фильм 10 раз

print("---------- LIB with views ----------")
for i in lib.library:  # При повторном выводе библиотеки видим что почти везде изменено количество просмотров
    print(i, "- Views:", i.views)

print("---------- TOP ----------")
for i in lib.top_titles(2):
    print(i, "- Views:", i.views)
