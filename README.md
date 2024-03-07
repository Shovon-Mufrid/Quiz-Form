# Survey Form
This is a survey form for client on their catering service


Virtual Environment Set Up

```
python -m venv venv
```
Virtual Activation[Linux]

```
source venv/bin/activate
```
Virtual Activation With Git Bash[Windows]

```
source venv/scripts/activate
```
Install Files

```
pip install -r requirements.txt
```
Migrate

```
python manage.py migrate
```

Migrations

```
python manage.py makemigrations
```

Create Superuser

```
python manage.py createsuperuser
```

Run Project

```
python manage.py runserver
```
To Check the dashboard

```
http://127.0.0.1:8000/surveys/dashboard/
```
To check survey

```
http://127.0.0.1:8000/surveys/
```

To Form Fill up the survey:
```
http://127.0.0.1:8000/surveys/{id}
```
