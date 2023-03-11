# B8ZS-Encoding
## Comment exécuter l’application
L’application a un serveur et des clients en `Python > 3.10` . Il est essentiel d’avoir les librairies dans le fichier `requirements.txt` .
### Créer un environnement (optionnel):
Pour installer `Python 3.10`, il faut faire
```console
$ sudo apt-get install python3.10
```
Pour installer `Python 3.10 venv`, il faut faire
```console
$ sudo apt-get install python3.10-venv
```
Ensuite, il faut cd dans le projet et executer
```console
$ python3.10 -m venv myEnv
```
Pour créer un nouvel environnement et 
```console
$ source myEnv/bin/activate
```
Pour activer l'environnement
### Installer les dependencies
Ensuite, on installe tous les packages dans l’environnement en faisant
```console
$ pip install -r requirements.txt
```
### Exécuter le Serveur
Ouvrir un terminal et activer l’environnement
```console
$ source myEnv/bin/activate
```
Ensuite lancer le serveur
```console
$ python server.py
```
### Exécuter le client
Ouvrir un terminal et activer l’environnement
```console
$ source myEnv/bin/activate
```
Ensuite lancer le client
```console
$ python client.py
```
