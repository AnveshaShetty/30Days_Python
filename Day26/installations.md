Code to run in terminal inorder to build an application using react:

pip install virtualenv         (incase if vistual environment has not been installed)
python -m pip show virtualenv  (double check)

mkdir python_for_web
cd python_for_web/

*activate virtual environment*
python -m virtualenv venv    --- Windows
virtualenv venv              --- MacOS/Linus

.\venv\Scripts\Activate.ps1    --- Windows
source venv/bin/activate       --- MacOS/Linux

pip freeze      
pip install Flask
pip freeze     (all the files present after installation of flask are visible)

*Created a project director named python_for_web. Inside the project, I created a virtual environment venv which could be any name but I prefer to call it venv. Then activated the virtual environment. I used pip freeze to check the installed packages in the project directory. The result of pip freeze was empty because a package was not installed yet.*
