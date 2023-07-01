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
  conda create --name Name_of_the_environment python=3.xx
  ```
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

