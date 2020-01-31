base de données : disquaire
user : postgres
mot de passe : admin


myvenv\Scripts\activate
python manage.py runserver

python manage.py makemigrations disquaire_project
python manage.py migrate
