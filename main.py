from MyAuthorModule.MyAuthorModule import Author
from MyBookModule.MyBookModule import Book



author = Author('J. K. Rowling').get_name()
book = Book('Harry Potter').get_title()


print(book, ' was written by ', author)