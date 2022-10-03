# The Music Library Generator
The Music Library Generator is a command-line application built to allow the user to create and manipulate a library of music, detailing song, artist and genre.

This application is targeted towards a user who would like to compile, organise and easily access a music library of their choice.

Welcome to [The Music Library Generator](https://cpeacocke4.github.io/avatar-quiz/)

![Mock-up of The Ultimate Avatar Quiz on various devices](assets/README-images/mock-up.png)

## **Contents** 

* [UX](#ux)
* [Features](#current-features)
* [Future Features](#future-features)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

## **UX**

### **User Stories**
* As a user I want to understand the purpose of the application upon arrival.
* As a user I want easily understand how to navigate the program.
* As a user I want to be able to create a library and interact with that library in a clear and simple manner.
* As a user I want to be able to manipulate the data in a simple manner.
* As a user I want to have a clean and concise experience of the application.

### **Structure**
The Music Library Generator is structured using functions and loops that access data stored within a Google Sheet, and allow the user to manipulate this data using text based commands. Upon every manipulation from the user the data within the Google Sheet is updated and the user is able to access and see their updated library. 

[Back to Top](#the-music-library-generator)

## **Features** 
The Music Library Generator contains 6 main features that are desplayed within a menu. These features are:
* View Library
* Add Song
* Delete Song
* Update Entry
* Search Library
* Close Program 

Upon completion of every function, the user is asked whether they would like to repeat that function or return to the menu. 

### **Menu**

* The menu was created to clearly and simply define the functionalities available to the user, and request an input from the user to choose between the 6 menu items. Upon user input the function to run the respective menu item is called.

![Screenshot of nav bar](assets/README-images/logo.png) 

### • **View Library** 
* The View Library function allows the user to see the existing library of music in an alphabetically ordered, clear and neatly layed out format.


![Screenshot of hero image](assets/README-images/welcome-screen.png)

### • **Add Song** 
* The add song function requests 3 fields of input from the user: song, artist, and genre. It validates the input by checking for the correct number of input fields, and whether the input already exists within the library. Upon succesful validation the input is then updated to the library, and the user is notified.


![Screenshot of ethos section](assets/README-images/question-screen.png)

### • **Delete Song** 
* The delete song function requests input from the user detailing the song they would like to delete. It validates the input by checking whether the song exists within the library already, and whether there is input present. Upon succesful validation the entry is deleted from the library, and the user is notified.

![Screenshot of times section](assets/README-images/result-screen.png)

### • **Update Entry** 

* The Update entry function requests input from the user detailing the song they would like to update. It validates the input by checking whether the song exists within the library, and whether there is input present. Upon succesful validation the row with the song, artist and genre is accessed and printed for the user, and the user is asked to input the update in 3 fields, song, artist and genre. Upon succesful validation of the second input, the library is updated and the user is notified.

### • **Search** 

* The Search function requests input from the user detailing either a song, genre or artist. It validates the input by checking whether the input exists within the library, and whether there is any input present. Upon succesful validation the search results are printed in a clear and organised format for the user.

### • **Close Program** 

* The Close Program function prints a goodbye message and closes the program upon the users request.

### • **Input Validation**

* All input is validated and checked for empty input fields, insufficient input, and respectively whether the input is present, or is not present within the data.

## **Future Features**
The Music Library Generator has many possibilities for future features, including:
* The ability to create albums.
* The ability to create playlists based off of genre or artist.
* A detailed report of the library including percentages of genres present, eg: '60% pop, 20% jazz and 20% classical'.

[Back to Top](#the-music-library-generator)