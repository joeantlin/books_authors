from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

def index(request):
    print("I'm Home")
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, "library/index.html", context)

#Create new book
def newbook(request):
    if request.method == "POST":
        if len(request.POST["title"]) > 1 and len(request.POST["desc"]) > 1:
            data = {
                "title":  request.POST["title"],
                "desc": request.POST["desc"]
            }
            print(data)
            Book.objects.create(title=f"{data['title']}", desc=f"{data['desc']}")
            print(Book.objects.all().values())
            return redirect('/')
        else: 
            return redirect('/')

#New Author Page
def authorpage(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, "library/new_author.html", context)

#Create new author
def newauthor(request):
    if request.method == "POST":
        if len(request.POST["fname"]) > 1 and len(request.POST["lname"]) > 1:
            data = {
                "fn":  request.POST["fname"],
                "ln": request.POST["lname"],
                "notes": request.POST["notes"]
            }
            print(data)
            Author.objects.create(first_name=f"{data['fn']}", last_name=f"{data['ln']}", notes=f"{data['notes']}")
            print(Author.objects.all().values())
            return redirect('/authors')
        else: 
            return redirect('/')

#Books Page
def books(request, book_num):
    context = {
        "the_book": Book.objects.get(id=f"{book_num}"),
        "book_authors": Book.objects.get(id=f"{book_num}").authors.all(),
        "all_authors": Author.objects.exclude(books=f"{book_num}")
    }
    return render(request, "library/books.html", context)

#Add author to book
def addauthor(request):
    if request.method == "POST":
        data = {
            "auth": request.POST["author"],
            "book": request.POST["book"],
        }
        print(data)
        Book.objects.get(id=f"{data['book']}").authors.add(Author.objects.get(id=f"{data['auth']}"))
        return redirect('/books/'+ data['book'])

#Authors Page
def authors(request, author_num):
    context = {
        "the_author": Author.objects.get(id=f"{author_num}"),
        "book_authors": Author.objects.get(id=f"{author_num}").books.all(),
        "all_books": Book.objects.exclude(authors=f"{author_num}")
    }
    return render(request, "library/authors.html", context)

#Add book to author
def addbook(request):
    if request.method == "POST":
        data = {
            "auth": request.POST["author"],
            "book": request.POST["book"],
        }
        print(data)
        Author.objects.get(id=f"{data['auth']}").books.add(Book.objects.get(id=f"{data['book']}"))
        return redirect('/authors/'+ data['auth'])