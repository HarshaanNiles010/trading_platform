# trading_platform
Below are the instructions on how to install and run the project on a local server
1) install conda for virtual environment.
  follow the guide on the official documentation page [conda installation](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)
2) verify the installation by running
  ``` 
  conda info
  ```
  and then run updates on conda
  ```
  conda update conda
  ```
3) Create a virtual environment
  ```
  conda create --name Name_of_the_environment python=3.9
  ```
  Using python 3.9 because aws has support for python 3.9 but not for v3.11

4) Activate the environment 
  ```
  source activate Name_of_the_environment
  ```
  and since we are using conda we can also use 
  ```
  conda activate Name_of_the_ennvironment
  ```
5) git clone the project
  ```
  git clone https://github.com/HarshaanNiles010/trading_platform.git
  ```
6) run the command
  ```
  pip3 install -r requirements.txt
  ```
  add the required packages to requirements.txt and then run the command given above again to install them in one go
When done with the project please use the following command to terminate the environment
  ```
  source deactivate
  ```
Similarly here we can also use
  ```
  conda deactivate
  ```
To deactivate the current environment
# Your Environment is ready for use
# Running the Django app
1) Go to the directory containing **manage.py**
2) run the following command
  ```
  python3 manage.py runserver
  ```
  This will start a local server and can be visited to have a look at the site in progress

3) To close the server just use Ctrl + c

Side Note: During development enable the virtual environment and then when work on the current project is done close the virtual environment

# Structure of Django app
1) The main control flow for the django app to my current level of understanding is the following:
  1) The views **views.py** in any app folder is the one which handles what is shown on the screen. It is where one can collect all the data from the user
  2) The urls **urls.py** in any app folder is where you can define your route and which view file can be used to get the neccessary data displayed
  3) The urls **urls.py** in the main app is where you have to include your path so that it can be used to navigate to the specific page of your choice
  4) The settings **settings.py** in the main app is where you have to declare your apps for them to be called upon later 

# Implementing Real time charts
1) To implement Real Time charts, below is a list of packages to be installed to use it successfully
  ```
  pip3 install -U 'channels[daphne]'
  ```
2) Then put the name **daphne** in **settings.py** under **INSTALLED_APPS**