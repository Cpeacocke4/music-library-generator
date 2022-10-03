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
