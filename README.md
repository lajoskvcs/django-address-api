# Back-end assignment

[My assignment](ASSIGNMENT.md)
[My assumptions](ASSUMPTIONS.md)

## Usage
Use python 3 and pip. (On macOS it can be `python3` and `pip3`)

Intsall the dependencies:
```shell
pip install -r requirements.txt
```

Migrate the database:
```shell
python manage.py migrate
```

Add a superuser to the database
```shell
python manage.py createsuperuser
```

Run the server:
```shell
python manage.py runserver
```

You can reach the application on `http://127.0.0.1:8000`

The administration panel is on `http://127.0.0.1:8000/admin`

## API Docs
* [Swagger UI](`http://127.0.0.1:8000/swagger`)
* [Redoc](`http://127.0.0.1:8000/redoc`)
