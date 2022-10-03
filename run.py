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


def delete_song():
    """
    Access song in record with user input and delete from record.
    """
    clear_screen()

    while True:
        deleted_song = input("Enter the song you would like to delete here:\n")
        current_songs = []
        for song in songs:
            current_songs.append(song)
        if deleted_song.lower() == '':
            print('Your search was invalid, please try again\n')
            continue
        if deleted_song.lower() not in current_songs:
            print(f'''{deleted_song} does not exist
            in your library, please request another song.\n''')
            continue
        print(f'You requested to delete {deleted_song}.')
        if deleted_song.lower() in songs:
            cell = library.find(deleted_song.lower())
            deleted_row = cell.row
            library.delete_rows(deleted_row)
        print('Your entry has been deleted!\n')
        print('Library successfully updated!')
        break

    rep_msg = 'Would you like to delete another entry?'
    repeat("delete", rep_msg, delete_song)


def update_song():
    """
    Find song, artist and genre in library and update with user input.
    """
    clear_screen()

    print('''If you would like to update an entry,
    please type in the song name below.\n''')

    while True:
        song_to_update = input("Enter song name here:\n")
        current_songs = []
        for song in songs:
            current_songs.append(song)
        if song_to_update.lower() == '':
            print('Your input was invalid, please try again.\n')
            continue
        if song_to_update.lower() not in current_songs:
            print('''The song you suggested does not exist
            in your library, please request another song.\'n''')
            continue
        print(f'You requested to update {song_to_update}.')

        if song_to_update.lower() in songs:
            cell = library.find(song_to_update.lower())
            row_to_update = library.row_values(cell.row)
            print(row_to_update)
            library.delete_rows(cell.row)
            print('''\nPlease enter your update
            separated with commas as follows:
            Song Title, Artist, Genre''')
            while True:
                update_input = input('\nEnter your update here:\n')
                updated_row = str(update_input.replace(', ',
                                                       ',')).lower().split(",")
                if update_input.lower() == '':
                    print('Your input was invalid, please try again.\n')
                    continue
                if len(updated_row) != 3:
                    print('''You did not provide enough information,
                    please try again.\n''')
                    continue
                library.append_row(updated_row)
                print(f'\nYou updated {row_to_update} to {updated_row}!')
                break
        break
    rep_msg = 'Would you like to update another entry?'

    repeat("update", rep_msg, update_song)


def search():
    """
    Find song, artist and genre and print all relevant answers for user.
    """
    clear_screen()

    list_of_lists = library.get_all_values()
    library_list = [item for list in list_of_lists for item in list]

    while True:
        search_input = input('''Please enter the song, artist or genre
        you are looking for below:\n''')
        cell_list = library.findall(search_input.lower())
        if search_input == '':
            print('Your input was invalid, please try again.\n')
            continue
        if search_input.lower() not in library_list:
            print('''Your search does not exist in the library,
            please try again.\n''')
            continue
        search_result = []
        for items in cell_list:
            search_result.append(library.row_values(items.row))
        print(tabulate(search_result,
                       headers=['Song Title', 'Artist', 'Genre']))
        break

    rep_msg = 'Would you like to search for something else?'
    repeat("repeat", rep_msg, search)