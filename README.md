# CareOrg
A web service which aggregates charities and helps increase their outreach

## Running for the first time

1) clone the repository
2) delete db.sqllite file inside app folder
3) open terminal with working directory set at the newly downloaded folder
4) run "docker build ."
5) run "docker-compose build"
6) open docker image cli - from Docker desktop
7) run "python manage.py makemigrations" or "python3 manage.py makemigrations"
8) run "python manage.py migrate"

	The project should be running now with an empty db, 
	Note: you can also follow the same steps to clear the database (skip steps 1,4,5)