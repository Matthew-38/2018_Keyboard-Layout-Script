# Keyboard-Layout-Script
A little script to configure several keyboards with different layouts on a Linux system

[Version Française en bas]

# Background
For many polyglots, as well as people who work in an international context, it is sometimes useful to not have one keyboard with several layouts, but in fact to have several keyboards, each with a dedicated keyboard. It is all the more important when we speak of languages with very different alphabets (such as Russian).

There already exists a solution for Windows - using a little program called "Right Keyboard" (see link at the end), which changes automatically the layout once it detects activity on the other keyboard. However there is latency and the first button pressed on the new keyboard is with the layout of the former. 

My little script only works on Linux. Fortunately there already exists a command line program called setxkbmap which allows us to assign a layout to a specific USB device which it uses (with an ID number). But the ID number is not stable. If you unplug and replug the keyboard, the ID changes (even if you plug it into the same port as before).

# My Solution
My script contains a list of keyboards to configure (you can modify this to suit your case), and for each one it does the following:

1. If there is not an "ID" supplied (False), it looks for it by calling xinput searching for the [name] supplied.

2. Changes the layour of the keyboard corresponding to this ID to the layout supplied.
	
# Usage
In a BASH terminal: 

	$Python3 KeyboardSetLayouts.py [reset]

You can add the parameter "reset" if you want to set all the keyboards to the default (supplied constant in the file). Otherwise there are no paramaters here. 

# Conclusion

This project had a practical and useful aim, but it also deepened my understanding of the usage of Python scripts in BASH and calling BASH programs from Python, with or without parameters in both cases. 

The code is open access for anyone. Do what you want with it.

Have a nice day!

#########################################################################################################
# Version Française

# Keyboard-Layout-Script
Un petit script pour configurer plusieurs claviers avec des différents Disposition des touches sous un système Linux


# Contexte
Pour des Polyglots ainsi que des personnes qui travail dans un contexte international, c'est parfois utile de n'avoir pas un clavier avec plusieurs dispositions mais en fait avoir plusieurs claviers, chacun avec une disposition specifique. Encore plus quand il s'agit des langues qui n'ont pas le même alphabet.

Il existe une solution sous Windows, en utilisant un petit logiciel "Right Keyboard", qui change automatiquement la disposition dés qu'il y a de l'activité détecté par l'autre clavier. Cependant, il contient un bug : le premier touche se trompe.

Ce logiciel ne marche pas sous Linux. Heureusement il existe une programme setxkbmap qui permet de configurer une disposition par rapport à l'identification USB qu'il exploit (id). Or, l'id n'est pas stable. Il suffit de debrancher et rebrancher le clavier et l'id est changé (même si c'est rébranché au même port qu'avant.


# Ma Solution
Mon scripte contient une liste de claviers à configurer (à vous de les customiser), et pour chacun fait la suite:

1. S'il y a pas de "id" fourni (False), le cherche avec xinput à partir du nom "name" fourni.

2. Change la disposition du clavier à celle fournie.


# Usage
Dans un terminal BASH:

	$Python3 KeyboardSetLayouts.py [reset]

On ajoute la paramettre "reset" si on veut mettre tous les claviers à la disposition de défaut. Sinon il n'y a pas de paramettre à fournir


# Conclusion
Ce projet avait un but utile et pratique, mais ça m'a aussi permit d'approfondir mes conaissances en usage des scripts Python sous terminal BASH, avec des paramettres et visa-versa : faire des appels à des programmes externe depuis Python. 

Ce code est libre d'access à tout le monde. Faites ce que vous voulez avec.
Bonne journée
 
###############################
RightKeyboard: https://www.codeproject.com/Articles/20994/Using-multiple-keyboards-with-different-layouts-on
