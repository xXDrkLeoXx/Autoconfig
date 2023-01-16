# Autoconfig
Un script python pour configurer automatiquement 3 switches Cisco

## Fonctionnalités
Le script permet de créer un fichier de configuration pour 3 switches Cisco en choisissant :
 - Quel Vlan utiliser
 - Pour chaque interface si elle est en mode trunk ou accès
 - Si les switches sont GigagabitEthernet ou Fastethernet
 - Si le switch à une adress IP
 - Si le switch à des interfaces en Etherchannel

## Comment l'utiliser

Lancer le script en étant dans le répertoire ou se situe le script :
 - En tapant la commande `./Autoconfig.py` (peut ne pas marcher selon la gestion des droits d'éxecution)
 - En tapant la commande `python Autoconfig.py`
 
