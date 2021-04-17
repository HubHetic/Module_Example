from MyAuthorModule.MyAuthorModule import NewAuthor
from MyBookModule.MyBookModule import NewBook



author = NewAuthor('J. K. Rowling').get_name()
book = NewBook('Harry Potter').get_title()


print(book, ' was written by ', author)