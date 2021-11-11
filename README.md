# PITCH-HUB
11/11/2021
# By 
Valentino Junior
# Description
 Pitchhub is a web - based application that allows users to pitch ideas, comment on other pitches, and vote on them. To utilize some of the capabilities, such as adding a pitch, commenting, and voting, a new user must first register and login.
# Behavior Driven Development (BDD)
A new user:
User will be able to view other peoples comments
User will not be able to comment untill the user registers and logs in
User will not be able to create a pitch until user registers and logs in
User will not be able to either downvote or upvote untill the user registers and logs in

Current User:
User will login with same credentials used to register
User inputs wrong credentials will be alerted
User inputs correct credentials, user will be logged in
User will be able to create a pitch
User will be able to views other peoples pitches
User will be able to comment on other peoples pitches
User will be able to either downvote or upvote other peoples pitches



# Setup/Installation Requirements 
Prerequisites
python3.8
pip
virtualenv


In your terminal:

  $ git clone
  $ cd newsapi

 
Create the virtual environment

  $ python3.8 -m venv virtual
  $ source virtual/bin/env
  $ curl https://bootstrap.pypa.io/get-pip.py | python

Install Flask and other Modules

  $ python3.8 -m pip install Flask
  $ python3.8 -m pip install Flask-Bootstrap
  $ python3.8 -m pip install Flask-Script

  Run the application, in your terminal:

  $ chmod +x start.sh
  $ ./start.sh

# Technologies Used
 I utilised python flask,bootstrap, html and css to deisgn the PITCH-HUB APP
# Support and Contact Details
Incase you encounter any issue or have any questions or any idea to add to the code feel free to contact me via ojvalentine14@gmail.com
# License
<a href = "https://github.com/valentine-ochieng/Programming-portfolio/blob/main/LICENSE">MIT licence </a>