#Leah Herschmann/Loeb 
#03/01/2022
#WhatABook Final Project

#import statements
from distutils.command.config import config
import mysql.connector 
from mysql.connector import errorcode
import sys

#database connetion
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#main menu
def show_menu():
    print("\n       --- MAIN MENU ---")
    print("Please choose one:\n")
    print ("1. View Books\n2. View Store Locations\n3. My Account\n4. Exit Program\n")
    
    try:
        choice = int(input("Please choose an option: \n"))
        return choice
    
    except ValueError:
        print("\n Invalid number. Goodbye.")
        sys.exit(0)

#show available whatabook books 
def show_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, author, details from book")
    books = _cursor.fetchall()

    print("\n --- DISPLAYING BOOK LIST --- ")
    for book in books:
        print("  Book ID: {}\n  Book Name: {}\n  Author: {}\n".format(book[0], book[1], book[2]))

#show whatabook locations
def show_locations(_cursor):
    
    _cursor.execute("SELECT store_id, locale from store")
    locations = _cursor.fetchall()
    
    print("\n --- DISPLAYING STORE LOCATIONS --- ")
    for location in locations:
        print(" Locale: {}\n".format(location[1]))

#check which user/ if user is valid
def validate_user():
    try:
        user_id = int(input("\nEnter a USER ID: "))
        if user_id < 0 or user_id > 3:
            print("\nPlease try again:")
            validate_user()
        return user_id
    except ValueError:
        print("\n Invalid number. Goodbye.")
        sys.exit(0)

#display user account information
def show_account_menu():
    try:
        print ("\n --- ACCOUNT MENU ---")
        print ("1. Wishlist\n2. Add Book\n3. Main Menu")
        account_choice = int(input("Please choose an option: \n"))
        return account_choice
    except ValueError:
        print("\n Invalid number. Goodbye.")
        sys.exit(0)

#display the users wishlist
def show_wishlist(_cursor, _user_id):
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " +
                    "FROM wishlist " +
                    "INNER JOIN user ON wishlist.user_id = user.user_id " +
                    "INNER JOIN book ON wishlist.book_id = book.book_id " +
                    "WHERE user.user_id = {}".format(_user_id))
   
    wishlist = _cursor.fetchall()
    print("\n --- DISPLAYING WISHLIST ---")
    
    for book in wishlist:
        print("Book Name: {}\n Author: {}\n".format(book[4], book[5]))

#display which books can be added to wishlist
def show_book_to_add (_cursor, _user_id):
    query = ("SELECT book_id, book_name, author, details " 
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    _cursor.execute(query)

    books_to_add = _cursor.fetchall()
    print("\n --- DISPLAYING AVAILABLE BOOKS ---")

    for book in books_to_add:
        print("    Book Id: {}\n    Book Name: {}\n".format(book[0], book[1]))

#add the selected book to wishlist
def add_book_to_wishlist (_cursor, _user_id, _book_id):
   _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

#check over users selections and direct to proper result
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    print ("\n --- WhatABook Application --- ")
    user_selection = show_menu()

    while user_selection !=4:
        if user_selection == 1:
            show_books(cursor)

        if user_selection == 2:
            show_locations(cursor)

        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()
            while account_option != 3:
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)
                if account_option == 2:
                    show_book_to_add(cursor, my_user_id)
                    book_id = int(input("\nEnter the id of the book you want to add: "))
                    add_book_to_wishlist(cursor, my_user_id, book_id)
                    db.commit()
                    print("\n   Book Id: {} was added to your wishlist.".format(book_id))
                if account_option == 3:
                    account_option = show_account_menu()
                if account_option < 0 or user_selection >3:
                    print("\n Invalid option, please retry...")
                account_option = show_account_menu()
        if user_selection < 0 or user_selection >4:
            print("\n Invalid option, please retry...")
        user_selection = show_menu()
    print("\n\nProgram terminated. Goodbye.")

#if error
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
        
    else:
        print(err)
#close program        
finally:
    db.close()