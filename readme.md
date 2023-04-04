# Le problème du sac à dos



# I. Quelques bases d'algo

> Petit crash course d'algorithmie simplifié pour montrer l'enjeu de l'exercice. Ce n'est pas essentiel pour répondre à l'exercice, mais ce sont des notions intéressantes à avoir.

## 1. Structure de données

Moyen d'organiser & stocker des données pour qu'elles puissent être traitées efficacement par un algorithme. Il existe différentes structures de données usuelles, qui ont chacune leur cas d'usage usuel.


Quelques structures de données usuelles:

* Pile / Stack (Last In First Out)
* Queue (First In First Out)
* Tableau
* Liste
* Dictionnaire / Map
* Graph, Tree et bien d'autres


Chaque structure de données a ses caractéristiques propres:
* les opérations supportées. Par exemple, une liste permet l'ajout et la suppression d'éléments, la recherche d'un élément et le tri des éléments. En comparaison, une pile ne permet que d'interagir avec la dernière valeur insérée. La recherche d'un élément dans une pile n'est pas possible sans en changer l'état (en dépilant tous éléments jusqu'à trouver la valeur cherchée)
    > Fonctionnellement, chaque structure de données a ses cas d'usage propres.
* L'implémentation sous-jacente. En gros, à quoi ça ressemble en mémoire. Par exemples, 2 manières d'implémenter une liste:
    * ArrayList: un tableau, soit un espace contigu en mémoire alloué lors de la création de la liste avec une taille donnée, qu'on agrandit lorsque le besoin se présente.
    * LinkedList: une chaîne d'objets alloués en mémoire contenant chacun une valeur, ainsi qu'une référence sur le maillon suivant de la chaîne

    > Lorsqu'on manie une structure de données en algo, c'est une abstraction au dessus d'une implémentation bas-niveau concrète


* L'exécution des opérations.
  * Par exemple, prenons l'opération "Accéder à un élément d'une liste par un indice". La manière dont cette opération est menée changera en fonction de l'implémentation sous-jacente: 
    * Si j'utilise un ArrayList, qui est en réalité fonctionnellement similaire à un tableau, je peux accéder aux éléments par indice en temps constant (random access). On parle de **complexité** O(1): l'action se fait en instantané, quel que soit la taille de la liste.
    * Si j'utilise une LinkedList, et que je veux accéder au 7ème élément, je dois parcourir les 6 premiers maillons avant de l'atteindre. On parle de complexité O(n): dans le pire cas (accès au dernier élément), il faudra parcourir les n éléments de la liste avant de l'atteindre.
  * Autre exemple : "chercher un objet par sa valeur". 
    * Si j'utilise une Liste, je dois parcourir les éléments jusqu'à trouver celui que je cherche. Encore une fois, complexité O(n).
    * Si j'utilise une Map, j'accède à l'emplacement en mémoire de mon objet en utilisant le hash de la valeur que je cherche: complexité O(1)
    

    > Le choix d'une structure de données plutôt qu'une autre aura donc un effet sur la **complexité** des opérations que je ferais sur mes structures de données.


> Mais au fait, c'est quoi la **complexité** ?


## 2. Complexité Algorithmique

> Par simplicité, on abordera ici que la [complexité temporelle](https://fr.wikipedia.org/wiki/Complexit%C3%A9_en_temps#:~:text=En%20algorithmique%2C%20la%20complexit%C3%A9%20en,d'arriver%20%C3%A0%20un%20r%C3%A9sultat.). Gardez cependant en tête que ce n'est qu'une partie du problème, et qu'il faudrait aussi prendre en compte la [complexité spatiale](https://fr.wikipedia.org/wiki/Complexit%C3%A9_en_espace)

Une chose qui rassemble toutes les structures de données : elle contiennent un ensemble d'éléments dénombrables. On note `N` le note nombre d'éléments dans notre collection.

Du point de vue d'un CPU, un algorithme peut être vu comme un ensemble d'opérations `X` à effectuer. Chacune de ces opérations représente un temps d'exécution (le temps que les transistors interagissent entre eux), l'enjeu de l'optimisation du temps d'exécution est donc de maintenir `X` aussi bas que possible.


Empiriquement, on remarque que dans la plupart des algorithmes effectués sur des structures de données, `X` croît proportionnellement avec `N`.

Par exemple: si je cherche une valeur dans une liste de `N` entiers non-triés, je vais commencer par regarder si le premier entier de la liste est celui que je cherche. Si oui, je le retourne. Si non, je passe au suivant. Dans le pire cas (l'élément que je cherche est le dernier de la liste) je dois donc parcourir les `N` entiers avant de trouver celui que je cherche. On dit alors que la recherche d'une valeur dans une liste non-triée a une complexité O(`N`) : dans le pire cas, cet algorithme représente `N` opérations pour mon processeur.

< montrer un exemple d'un algorithme avec une complexité quadratique / exponentielle>

//Il est difficile de donner le temps exact nécessaire à chaque opération (dépendant de l'architecture du CPU ainsi que de la nature de l'opération). Une bonne estimation est de dire qu'un CPU ayant une _clock speed_ de 3.0 GHz pourra effectuer environ 3 milliards d'opération par seconde. 



# II. Problème

### Vous êtes en train de braquer une banque, vous venez d'ouvrir la serrure du coffre fort et vous en découvrez le contenu:

`N` objets ayant une valeur `V` et une masse `W`

Naturellement, vous souhaitez maximiser les bénéfices de votre _opération_. Cependant, vous ne pouvez pas prendre tous les objets avec vous.

Vous ne disposez que d'un sac à dos, pouvant supporter une masse `WMax`.


### question: pour quelle combinaison d'objets je maximise la valeur de mon butin, tout en restant dans la limite `WMax` ?