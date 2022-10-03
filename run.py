"""Imported libraries"""
import sys
import os
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
from title import title_art

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("music_library_generator")

library = SHEET.worksheet("Library")

data = library.get_all_records()

songs = library.col_values(1)

def menu():
    """
    Print menu options to user and request answer with the
    numbers corresponding to relevant menu options.
    Call function based off of user input.
    """
    menu_message = f"""Welcome to
    {title_art}

    What would you like to do?

    1 - View Library
    2 - Add Song
    3 - Delete Song
    4 - Update Song
    5 - Search Library
    6 - Close Program
    """
    print(menu_message)

    while True:
        menu_input = input('Enter a number matching the menu option:\n')

        try:
            int(menu_input)
        except ValueError:
            print('Your input was invalid, please try again.')
            continue
        if int(menu_input) < 1 or int(menu_input) > 6:
            print('''The number you provided is not valid,
            please enter a number between 1 and 6.''')
            continue
        if int(menu_input) == 1:
            view_library()
        elif int(menu_input) == 2:
            add_song()
        elif int(menu_input) == 3:
            delete_song()
        elif int(menu_input) == 4:
            update_song()
        elif int(menu_input) == 5:
            search()
        elif int(menu_input) == 6:
            close_program()
        break


def view_library():
    """
    Get all data from library, organise, and print for user.
    """
    clear_screen()
    data = library.get_all_records()
    print('Loading your library please wait...\n')
    print('Library loaded!\n')

    new_rows = []
    for items in data:

        rows = list(items.values())
        new_rows.append(rows)

    sorted_rows = sorted(new_rows, key=lambda x:x[0])
    print(tabulate(sorted_rows, headers=['Song Title', 'Artist', 'Genre']))

    rep_msg = 'Would you like to return to the menu?'
    repeat("view", rep_msg, view_library)


def add_song():

    """
    Request song input from user, detailing song title,
    artist and genre.
    Check input validity.
    Add new song to sheet and order alphabetically.
    """
    clear_screen()

    while True:
        print('''Please enter your song separated with commas
         as shown: Song Title, Artist, Genre\n''')
        song_str = input("Enter your song here:\n")
        song_input = str(song_str.replace(', ', ',')).lower().split(",")
        if len(song_input) != 3:
            print('''You did not provide enough information,
            please enter your information as follows:
            Song Title, Artist, Genre.\n''')
            continue
        if song_input[0] in songs:
            print('''That song already exists in your library,
            please add a new song.\n''')
            continue
        print(f'You added {song_input}, thank you for your input!\n')
        library.append_row(song_input)
        print('Updating library, please wait...\n')
        print('Library successfully updated!')
        break

    rep_msg = 'Would you like to add another song?'
    repeat("add", rep_msg, add_song)
