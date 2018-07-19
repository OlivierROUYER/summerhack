#SET UP L'APPLIPCATION


Toutes les commandes doivent se faire dans un terminal et le script marche seulement sur ubuntu et mac (a part le apt-get) ubuntu
Pour l'installation des composants:
```
pip install -r requirement.txt
```

Afin de lancer l'application il est necessaire de set-up les databases:
```
python manage.py makemigrations accounts
python manage.py sqlmigrate accounts 0001
python manage.py migrate
```

Et enfin de créer un user:<br />
```
python manage.py createuser
```
<br />
On rempli les options pour le super User

Enfin on lance le serveur:
```
python manage.py runserver
```

Ou sinon lancer le script:
```
 sh script.sh
 ```
 
 
Et allez a l'adresse ci-dessou:
```
http://127.0.0.1:8000
```

Pour ce qui n'a pas été fait:
Formulaire complet du User
Test unitaires