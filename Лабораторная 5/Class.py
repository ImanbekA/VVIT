class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return self.title, self.author, self.year
Prorok = Book('Prorok', 'Pushkin', 1828)
Her = Book('Her', 'Iman', 1232)
print(Prorok.get_info())