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

## **Technologies Used** 

* [Python](https://www.python.org/) - Usedto create the entirety of the program.
* [Heroku](https://dashboard.heroku.com/login) - Used to deploy the program.
* [Gitpod](https://www.gitpod.io/#get-started) - Used to code and edit the program.
* [Github](https://github.com/) - Used to store the repositry.
* [Google Sheets](https://www.google.com/sheets/about/) - Used to store and access data.

[Back to Top](#the-music-library-generator)

## **Testing** 
The site has been extensively tested on both the Gitpod terminal and the Heroku terminal, and found to have minimal to no errors in its structure, styling, and functionality. 

### • **Code Validation**
All code has been run through the [PEP8 python checker](https://www.pythonchecker.com/).

* The check came back with a 100% success rate.

PEP8 validation result: 
![Screenshot of PEP8 validation result](/README_media/validation.png)


### • **Bugs** 
#### **Fixed Bugs** 
During the creation of this program few bugs were encountered, and they are listed below:

* Issue with input while loop within the menu function. The loop would continue even after the user had submitted valid input. This bug was solved by moving the 'break' keyword to the correct position within the code.

#### **Unfixed Bugs**
There are no unfixed bugs within the program.

## **Deployment** 
This is a guide on how to deploy a project via Heroku.
Credit for this explanation goes to [Matthew Hurrel](https://github.com/Matthew-Hurrell/labyrinth-of-riddles)

* Type "pip3 freeze > requirements.txt" into your terminals command line to create a list of dependencies. These will be in the requirements.txt file for heroku to intall before starting the application.
* Push these changes up to GitHub.
* Open Heroku on the web browser and login or create an account.
* Once the account is open/created, click the "New" button in the top right hand corner and then click "Create new app" from the dropdown menu.
* Enter an app name (this has to be unique on Heroku) and choose the local region in the dropdown box below. 
* Click the "Create app" button.
* When the app dashboard is open go to "Settings" in the menu bar. Find the "Config Vars" section and click the "Reveal Config Vars" button. Any sensitive information not sent to GitHub, that is required for the running of the app, must be entered manually in this section. Any protected .json files need to be entered here. Go back to the project and copy all the data in the .json file. Paste the data into the "Value" field. In the "Key" field enter "CREDS" in all capitals. Then click the "Add" button.
* For projects using the Code Institute terminal, another Config Var needs to be added into this section. Enter "PORT" in all capitals into the "Key" field and "8000" into the "Value" field and click the "Add" button.
* For projects using Python, scroll down to the "Buildpacks" section below. Click the "Add buildpack" button and select the "Python" option from the pop up window. Click the "Save Changes" button to exit the window.
* For projects that use the Code Insitute terminal, repeat the process and click the "Add buildpack" button again and select the "Nodejs" option from the pop-up window. Click the "Save Changes" button to exit the window.
* Check the order of the buildpacks in the buildpacks section. Ensure that Python is above Nodejs. If it isn't, click and drag the Python bar using the three-line icons until it is top of the list.
* Scroll up to the top of the page and click the "Deploy" tab on the main app menu.
* When the deployment page opens, scroll down to the "Deployment method" section and click and select the "GitHub" option to connect Heroku to the repository on GitHub. Scroll down and click the "Connect to GitHub" button. Log into GitHub in the pop-up window if required, otherwise this should be done automatically.
* In the "Connect to GitHub" section enter the repository name into the repo-name field and click the "Search" button. The repository name should appear below the field. Click the "Connect" button to connect the GitHub repository to Heroku.
* If the last step was successful the "Deploy" page should change. Scroll down the page to the "Automatic deploys" and "Manual deploy" sections. To enable automatic deploys with each new GitHub push click the "Enable Automatic Deploys" button. To manually deploy click the "Deploy branch" button in the "Manual deploy" section. Ensure the "main"/"master" branch is selected from the drop down menus for both of these options if that is the latest branch of the project.
* If deployment is successful a prompt should appear with a "View" button to view the deployed app. Click the button to view the app deployment.

#### **Fork this repository**
To fork this repository follow the instructions below:

* Log-in to GitHub and locate this repository.
* On the top right of the page is a button called 'Fork', click on the button to create a copy of this repository in your GitHub Account.

#### **Clone this project** 
To make a local clone of this project follow these steps:

* On the repository page, click the **Code** tab.
* In the HTTPS section, click on the clipboard to copy the sites URL.
* In your own personal IDE, open **Git Bash**.
* Type in 'git clone' and paste in the URL copied from this repository.
* Click enter and your clone will be created!

[Back to Top](#the-music-library-generator)

## **Credits**
In this section all code that was referenced from external sources will be credited.
#### • **Code**

* Code connecting the google sheets API to the run.py file was referenced from the [Code Institute](https://codeinstitute.net/se/) Love Sandwiches Project
* Code to clear the screen was sourced from [this website[](https://teamtreehouse.com/community/using-a-clearscreen-in-pycharm)
* Typeography for the heading was sourced from [this website](http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=The%20music%0Alibrary%0Agenerator%0A)

[Back to Top](#the-music-library-generator)

## **Acknowledgements**
The site was completed as a portfolio project for the Full Stack Software Developer Diploma at [Code Institute](https://codeinstitute.net/se/). 

I would like to thank all those who were involved in supporting me through this project and guiding me along the way:

* My [Code Institute](https://codeinstitute.net/se/) mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/).
* The [Code Institute](https://codeinstitute.net/se/) Slack community.

Christy Peacocke 2022.

[Back to Top](#the-music-library-generator)