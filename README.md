# cinemaccs

Main repo of the opensource webapp

## Local Setup

```
cp .env.example .env
docker compose build
docker compose up -d
```

Enter api container with `docker exec -it cinemaccs_api bash`
Then:

```
python manage.py migrate
python manage.py createsuperuser --email toto@example.com --username toto
```

To create a migration, enter container and run
`python manage.py makemigrations cinemaccs_project`
`python manage.py sqlmigrate cinemaccs_project XXXXX`
`python manage.py migrate`