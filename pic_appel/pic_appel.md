# Pic appel

Programme qui lit une liste d'appels sur l’entrée standard et renvoie la valeur du pic d'appels simultannés.

Les appels sont entrés sous forme de liste `start:end` où `start` et `end` sont les valeurs timestamp de début et de fin de l'appel. Les appels sont classés par ordre croissants de `start`.

## Exemple d'entrée acceptée :

``` Bash
1385718405:1385718491
1385718407:1385718409
1385718408:1385718452
1385718408:1385718464
1385718413:1385718452
```

## Initialisation

``` bash
$ chmod +x ./pic_appel.py
```

## Exemple d'utilisation :

``` bash
$ cat calls.txt | ./pic_appel.py
```
