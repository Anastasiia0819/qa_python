import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    #1. проверка названия -0, 41 символ и более 41 символа - не добавились в словарь
    @pytest.mark.parametrize('name', ['', 'Смерть приходит за архиепископом, тест, книга, kkk3?','Общая теория занятости, процента и денег!'])
    def test_add_new_book_add_book_incorrect_characters(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    #2. проверка, что genre присвоился name
    def test_set_book_genre_add_genre(self):
        collector = BooksCollector()
        name = "ОНО"
        genre = 'Ужасы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    #3. получить жанр книги по её имени
    def test_get_book_genre_correct_name(self):
        collector = BooksCollector()
        collector.add_new_book("Винни Пух")
        collector.set_book_genre("Винни Пух", 'Мультфильмы')
        assert collector.get_book_genre("Винни Пух") == "Мультфильмы"

    #4. проверка, вывода определенного жанра (Детектив) и что в списке сохраняется несколько названий(не перезаписывается)
    def test_get_books_with_specific_genre_genre_in_list(self):
        collector = BooksCollector()
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс", "Детективы")
        assert "Шерлок Холмс" in collector.get_books_with_specific_genre("Детективы")

    #5. Добавить корреткные значения и проверить, что в ответе словарь
    def test_get_books_genre_check_dict(self):
        collector = BooksCollector()
        collector.add_new_book("Золушка")
        collector.set_book_genre("Золушка", 'Мультфильмы')
        collector.add_new_book("Десять негритят")
        collector.set_book_genre("Десять негритят", "Детективы")
        assert collector.get_books_genre() == {"Золушка": "Мультфильмы", "Десять негритят": "Детективы"}

    #6. добавить книгу, которая подходит детям
    def test_get_books_for_children_book_for_child(self):
        collector = BooksCollector()
        collector.add_new_book("Маленький принц")
        collector.set_book_genre("Маленький принц", 'Мультфильмы')
        collector.add_new_book("Талантливый мистер Рипли")
        collector.set_book_genre("Талантливый мистер Рипли", "Детективы")
        assert len(collector.get_books_for_children()) == 1 and "Маленький принц" in collector.get_books_for_children()

    #7. Добавить книгу в избранное, проверить что книга добавилась в избранное
    def test_add_book_in_favorites_book_added(self):
        collector = BooksCollector()
        collector.add_new_book("Русалочка")
        collector.add_new_book("Азазель")
        collector.add_book_in_favorites("Русалочка")
        collector.add_book_in_favorites("Азазель")
        assert collector.favorites == ["Русалочка", "Азазель"]

    #8. Удалить книгу из избранного, проверить что книга не отображается в избранное
    def test_delete_book_from_favorites_one_book_delete(self):
        collector = BooksCollector()
        collector.add_new_book("Приключения Оливера Твиста")
        collector.add_book_in_favorites("Приключения Оливера Твиста")
        collector.delete_book_from_favorites("Приключения Оливера Твиста")
        assert len(collector.favorites) == 0

    #9. Получить список Избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("Убийство на улице Морг")
        collector.add_book_in_favorites("Убийство на улице Морг")
        assert len(collector.get_list_of_favorites_books()) == 1 and "Убийство на улице Морг" in collector.get_list_of_favorites_books()



