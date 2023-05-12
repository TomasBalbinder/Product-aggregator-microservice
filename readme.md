# Product-aggregator-microservice


Microservice that enables users to browse a product catalog and automatically updates prices from the offer service provided by the company Applifting.


## How to install on local:
tested on Windows 10
#### It all works on Django Ninja and PostgreSQL
Don't forget to install your virtual environment and activate it before you install others things.
After downloading your clone from the repository, it will install all the dependencies for you.
```bash
py -3 -m venv venv 
pip install -r requirements.txt
```
and then install your DB client, I chose PostgreSQL with [pgAdmin 4](https://www.pgadmin.org/download/pgadmin-4-windows/).

You have to go to settings.py and set up your DB, before you run the application!

Then do the migrations:
```bash
python manage.py makemigrations
python manage.py migrate 
``` 

## Usage
#### Start the Django server
```python
python manage.py runserver     
```
then you can visit your endpoints and work with them
```python
http://localhost:8000/api/docs#/   
```
#### If you want to run the microservice at the same time, you need to open a second command line and be in the same directory as manage.py
```python
python manage.py update_prices   
```
#### stop it ctrl + C

## License

without a license