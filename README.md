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
`python manage.py sqlmigrate cinemaccs_project XXXX` --optional with XXXX the id of the migration created
`python manage.py migrate`

To revert a migration to a given one:
`python manage.py migrate cinemaccs_project XXXX` -- XXXX = the id of the given migration you want to go back
