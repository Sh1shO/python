class Book:
    def __init__(self, title, author, isbn):
        self.__title = title #приватный
        self.__author = author  # приватный
        self.__isbn = isbn  # приватный

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn

book1 = Book("Вино из одуванчиков", "Рей Брэдбери", "1111111111111111")
print(book1.__title)
