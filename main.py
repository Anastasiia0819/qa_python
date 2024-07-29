class BooksCollector:

    def __init__(self):
        self.books_genre = {} #куда можно добавить пару Название книги: Жанр книги.
        self.favorites = [] # содержит избранные книги
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'] #содержит доступные жанры
        self.genre_age_rating = ['Ужасы', 'Детективы'] #содержит жанры с возрастным рейтингом

    # добавляем новую книгу без указания жанра. (максимум 40 символов. Одну и ту же книгу можно добавить только один раз)
    def add_new_book(self, name):
        if not self.books_genre.get(name) and 0 < len(name) < 41:
            self.books_genre[name] = ''

    # устанавливаем книге жанр (если книга есть в books_genre и её жанр входит в список genre)
    def set_book_genre(self, name, genre):
        if name in self.books_genre and genre in self.genre:
            self.books_genre[name] = genre

    # получаем жанр книги по её имени
    def get_book_genre(self, name):
        return self.books_genre.get(name)

    # выводим список книг с определённым жанром
    def get_books_with_specific_genre(self, genre):
        books_with_specific_genre = []
        if self.books_genre and genre in self.genre:
            for name, book_genre in self.books_genre.items():
                if book_genre == genre:
                    books_with_specific_genre.append(name)
        return books_with_specific_genre

    # получаем словарь books_genre
    def get_books_genre(self):
        return self.books_genre

    # возвращаем книги, подходящие детям ( У жанра книги не должно быть возрастного рейтинга)
    def get_books_for_children(self):
        books_for_children = []
        for name, genre in self.books_genre.items():
            if genre not in self.genre_age_rating and genre in self.genre:
                books_for_children.append(name)
        return books_for_children

    # добавляем книгу в Избранное (Книга должна находиться в словаре books_genre. Повторно добавить книгу в избранное нельзя.)
    def add_book_in_favorites(self, name):
        if name in self.books_genre:
            if name not in self.favorites:
                self.favorites.append(name)

    # удаляем книгу из Избранного (если она там есть)
    def delete_book_from_favorites(self, name):
        if name in self.favorites:
            self.favorites.remove(name)

    # получаем список Избранных книг
    def get_list_of_favorites_books(self):
        return self.favorites
