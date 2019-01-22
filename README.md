# Keyboard-Layout-Script
Un petit script pour configurer plusieurs claviers avec des différents Disposition des touches sous un système Linux


# Contexte
Pour des Polyglots ainsi que des personnes qui travail dans un contexte international, c'est parfois utile de n'avoir pas un clavier avec plusieurs dispositions mais en fait avoir plusieurs claviers, chacun avec une disposition specifique. Encore plus quand il s'agit des langues qui n'ont pas le même alphabet.

Il existe une solution sous Windows, en utilisant un petit logiciel "Right Keyboard", qui change automatiquement la disposition dés qu'il y a de l'activité détecté par l'autre clavier. Cependant, il contient un bug : le premier touche se trompe.

Ce logiciel ne marche pas sous Linux. Heureusement il existe une programme setxkbmap qui permet de configurer une disposition par rapport à l'identification USB qu'il exploit (id). Or, l'id n'est pas stable. Il suffit de debrancher et rebrancher le clavier et l'id est changé (même si c'est rébranché au même port qu'avant.


# Ma Solution
Mon scripte contient une liste de claviers à configurer (à vous de les customiser), et pour chacun fait la suite:

	S'il y a pas de "id" fourni (False), le cherche avec xinput à partir du nom "name" fourni.

	Change la disposition du clavier à celle fournie.


# Usage
Dans un terminal BASH:

	$Python3 KeyboardSetLayouts.py [reset]

On ajoute la paramettre "reset" si on veut mettre tous les claviers à la disposition de défaut. Sinon il n'y a pas de paramettre à fournir


# Conclusion
Ce projet avait un but utile et pratique, mais ça m'a aussi permit d'approfondir mes conaissances en usage des scripts Python sous terminal BASH, avec des paramettres et visa-versa : faire des appels à des programmes externe depuis Python. 

Ce code est libre d'access à tout le monde. Faites ce que vous voulez avec.
Bonne journée
 
