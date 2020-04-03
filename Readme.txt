you can check out the outcome from this project at https://sudokubyblessing.herokuapp.com/
do not, and i can not stress this enough, get your hopes up.

if you want a good laugh just have a read through of the code.
you can tell it was made by someone who has no idea how to code

the algorithm is custom made (by someone who doesnt even know how to play the game)
which means it only works for the most basic puzzles 

i got all there of my puzzles from 
http://lipas.uwasa.fi/~timan/sudoku/
i took all the puzzles that my algarithm could solve (the three easiest)
and used those. 
in the future i would like to make a new search  algorithm and add it in.
also i wanna see if i can do anything about how is doesnt look the way i want it to in safari

below is all the commands that i run in the terminal to get the final result.
#################################################################
my plan
ok i needs a step by step on how to set up my ven
how to set up flask and all the depedancies 
and set up a basic web 
i need to aslo plan how i am going to show the numbers on screan

##################################################################
step by step on how to set up my working enviroment
make a folder
open terminal in folder
>>>> pip install virtualenv
>>>> virtualenv env (makes the vertual folder)
>>>> env\Scripts\activate
>>>>FLASK_ENV=development (sets the debugger mode on)
>>>> pip install flask flask-sqlalchemy 

make the app.py file
write basic app flask

//python app.py
this didnt work for me so instead u used theses commands
>>>> set flask = app.py
>>>> flask run
this worked

make database 
>>>>python
>>>> from app import db
>>>> db.create_all()
git commands that i sued

i also used heroku
(i had to restart the cmd )
heroku commands

heroku login
pip install gunicorn
pip freeze > requirements.txt
touch Procfile 
git init 
git add .
git commit -m "early access Sudoku solver"
 

heroku create sudoku
touch Procfile (web: gunicorn app:app)
git remote -v (shows where we pushing to )
git push heroku master
