# Comptage mots

Programme permettant de classer par nombre d’occurrences les
mots d’un texte capturé sur l’entrée standard.

## Initialisation

``` bash
$ chmod +x ./comptage_mot.py
```


## Exemples d'utilisation :

``` bash
$ echo "foo bar baz foo" | ./comptage_mot.py
```

``` bash
$ cat comptage_mot.py | ./comptage_mot.py
```

``` bash
$ cat /etc/services | ./comptage_mot.py
```