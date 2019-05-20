class Hardcoverbook:
    def __init__(self, title, author, releaseyear, pagenum):
        self.title = title
        self.author = author
        self.releaseyear = releaseyear
        self.pagenum = pagenum
        self.weight = self.pagenum * 10 + 100

    def toString(self):
        return f"Author: {self.author}\ntitle: {self.title}\nYear: {self.releaseyear}"

class Paperbackbook:
    def __init__(self, title, author, releaseyear, pagenum):
        self.title = title
        self.author = author
        self.releaseyear = releaseyear
        self.pagenum = pagenum
        self.weight = self.pagenum * 10 + 20

    def toString(self):
        return f"Author: {self.author}\ntitle: {self.title}\nYear: {self.releaseyear}"

class Bookshelf:
    def __init__(self, bookshelf=[]):
        self.bookshelf = bookshelf
    
    def addBooks(self, book):
        self.bookshelf.append(book)
    
    def lightestBook(self):
        lightestbook = {}
        for i in self.bookshelf:
            lightestbook[i.author] = i.weight
        lightest = min(lightestbook.values())
        for key in lightestbook:
            if lightestbook[key] == lightest:
                return f"Who is the author of the lightest book: {key}"
    def mostPages(self):
        mostpages = {}
        for i in self.bookshelf:
            mostpages[i.author] = i.pagenum
        mostpage = max(mostpages.values())
        for key in mostpages:
            if mostpages[key] == mostpage:
                return f"Which author wrote the most pages: {key}"

book1 = Paperbackbook("The Hitchhiker's Guide to the Galaxy","Douglas Adams",  "1979",105 )
book2 = Hardcoverbook( "In Search of Lost Time","Marcel Proust", "1913", 150)
bookshelf = Bookshelf()
bookshelf.addBooks(book1)
bookshelf.addBooks(book2)
print(bookshelf.lightestBook())
print(bookshelf.mostPages())




