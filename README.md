# Autoconfig
Un script python pour configurer automatiquement 3 switches Cisco

## Fonctionnalités
Le script permet de créer un fichier de configuration pour 3 switches Cisco en choisissant :
 - Quel Vlan utiliser
 - Pour chaque interface si elle est en mode trunk ou accès ou
 - Si une interface fait partie d'une liaison Etherchannel
 - Si les switches sont GigabitEthernet ou FastEthernet
 - Si le switch à une adresse IP

## Comment l'utiliser

Télécharger le script sur cette page en allant dans les releases :
![Screen repo vers Release](https://github.com/xXDrkLeoXx/Autoconfig/blob/main/.readmefiles/github.png "Il faut cliquer sur Autoconfig")

![Screen Releases](https://github.com/xXDrkLeoXx/Autoconfig/blob/main/.readmefiles/release.png "Il faut cliquer sur Autoconfig.py")

Lancer le terminal et aller dans le dossier ou se situe votre fichier Autoconfig.py

Une fois dans le dossier, Pour lancer le scrit vous pouvez faire la commande :
 - `./Autoconfig.py` (peut ne pas marcher selon la gestion des droits d'éxecution)
 - Ou `python Autoconfig.py` (fonctionne tout le temps)

 Ensuite laissez vous guider par le dialogue avec le script

 A la fin vous obtener 3 fichiers texte à coller dans putty pour configurer chaque script