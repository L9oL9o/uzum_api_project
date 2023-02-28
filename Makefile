mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

r:
	python3 manage.py runserver 9009

rq:
	pip freeze >requirements.txt

