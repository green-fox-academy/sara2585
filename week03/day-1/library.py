from collections import Counter

class Book:
    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year
    def toString(self):
        print(f"{self.author} : {self.title}({self.year})")

class Bookshelf:
    def __init__(self, booklist = []):
        self.booklist = booklist
        self.booklist.append(Book("Douglas Adams", "The Hitchhiker's Guide to the Galaxy", "1979"))
        self.booklist.append(Book("Marcel Proust", "In Search of Lost Time", "1913"))

    def addBooks(self, book):
        self.booklist.append(book)

    def removeBooks(self, book):
        self.booklist.remove(book)

    def favouriteAuthor(self):
        authorlist = []
        for i in self.booklist:
            authorlist.append(i.author)
        res = Counter(authorlist)
        return f"The favourite author is: {res.most_common(1)}"

    def earliestPublished(self):
        bookyear = {}
        for i in self.booklist:
            bookyear[i.title] = i.year
        earliestyear = min(bookyear.values())
        for key in bookyear:
            if bookyear[key] == earliestyear:
                return f"The earliest published book is: {key}"
    
    def latestPublished(self):
        bookyear = {}
        for i in self.booklist:
            bookyear[i.title] = i.year
        latestyear = max(bookyear.values())
        for key in bookyear:
            if bookyear[key] == latestyear:
                return f"The latest published book is: {key}"

    def toString(self):
        bookcount = len(self.booklist)
        return(f"The number of books: {bookcount}\n{self.favouriteAuthor()}\n{self.earliestPublished()}\n{self.latestPublished()}")
        
    
bookshelf = Bookshelf()
bookshelf.addBooks(Book("Marcel Proust", "Sara test title", "2019"))     
print(bookshelf.favouriteAuthor()) 
print(bookshelf.earliestPublished())
print(bookshelf.latestPublished())
print(bookshelf.toString())

        