import backend
from tkinter import *

def clear_list():
    list1.delete(0, END)

def fill_books(books):
    if books is not None:
        for book in books:
            my_book = f"ID: {book.id} Title: {book.title}, Author: {book.author}, Year: {book.year}, ISBN: {book.isbn}"
            list1.insert(END, my_book)

def selecting_books_from_database(book_id):
    books = backend.view()
    for book in books:
        if book.id == book_id:
            e1.delete(0, END)
            e1.insert(END, book.title)
            e2.delete(0, END)
            e2.insert(END, book.author)
            e3.delete(0, END)
            e3.insert(END, book.year)
            e4.delete(0, END)
            e4.insert(END, book.isbn)
        else:
            continue

window = Tk()
window.title("Book Store")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)


title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)


list1 = Listbox(window, width=35, height=6)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=0, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

def get_selected_row(event):
    global selected_book
    if len(list1.curselection()) > 0:
        index = list1.curselection()[0]
        selected_book = list1.get(index)
        book_id = int(selected_book[4])
        selecting_books_from_database(book_id)


list1.bind("<<ListboxSelect>>", get_selected_row)

def view_command():
    clear_list()
    books = backend.view()
    fill_books(books)

b1 = Button(window, text="View All", width=12, command=lambda: view_command())
b1.grid(row=2, column=3)

def search_command():
    clear_list()
    books = backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    fill_books(books)

b2 = Button(window, text="Search Entry", width=12, command=lambda: search_command())
b2.grid(row=3, column=3)

def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

b3 = Button(window, text="Add Entry", width=12, command=lambda: add_command())
b3.grid(row=4, column=3)

def update_command():
    book_id = int(selected_book[4])
    backend.update(book_id, title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

b4 = Button(window, text="Update Selected", width=12, command=lambda: update_command())
b4.grid(row=5, column=3)

def delete_command():
    try:
        backend.delete(selected_book[4])
        view_command()
    except NameError:
        view_command()

b5 = Button(window, text="Delete Selected", width=12, command=lambda: delete_command())
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=lambda: window.destroy())
b6.grid(row=7, column=3)

view_command()

window.mainloop()