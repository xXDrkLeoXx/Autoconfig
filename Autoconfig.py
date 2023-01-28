#! /usr/bin/env python3
import os.path

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

etherInt = [False, False, False, False, False, False, False, False]
YN =["OUI","NON",""]

def InputTxt(LSTRP, PROMPT):
    print(PROMPT)
    Inp = input(" -> ")
    if Inp.upper() not in LSTRP:
        print(f"{bcolors.FAIL}Valeurs non comprise{bcolors.ENDC}")
        return InputTxt(LSTRP, PROMPT)
    else:
        return Inp.upper()

def InputNum(RANGE):
    try:
        Num = int(input("-> "))
        if Num > RANGE:
            print(f"{bcolors.WARNING}Valeur trop grande{bcolors.ENDC}")
            return InputNum(RANGE)
        return Num
    except:
        print(f"{bcolors.FAIL}Valeur non numérique{bcolors.ENDC}")
        return InputNum(RANGE)

def ExMark(LIST, nbLigne): # bah c'est pour mettre plein de poin d'exclamation
    for i in range(nbLigne):
        LIST.append("!\n")

def trunkinginterface(LIST, vlan): # fonction appeler pour configuer une interface en mode trunk
    LIST.append(" switchport trunk allowed vlan " + str(vlan) + "\n")
    LIST.append(" switchport trunk encapsulation dot1q\n")
    LIST.append(" switchport mode trunk\n")
    LIST.append(" switchport nonegotiate\n")
    
def accessInterface(LIST, vlan): # fonction appeler pour configuer une interface en mode accès
    LIST.append(" switchport access vlan " + str(vlan) + "\n")
    LIST.append(" switchport mode access\n")
    LIST.append(" switchport nonegotiate\n")

def translation(str):
    match str:
        case "TR":
            return "en mode trunking"
        case "ETH":
            return "en liaison Etherchannel"
        case "AC":
            return "en mode accès"
        case _:
            return "non configuré"

def confInt(Interface, Tabconf):
    txt = "Mode de Configuration\nVous aver le choix entre :\n * tr pour Trunking\n * ac pour mode accès\n * eth pour Etherchannel"
    Resp = ["TR","AC","ETH"]
    mode = InputTxt(Resp,txt)
    
    match mode:
        case "TR":
            print("Interface mis en mode Trunk\n")
            Tabconf[Interface] = "TR"
        case "AC":
            print("Interface mis en mode accès\n")
            Tabconf[Interface] = "AC"
        case "ETH":
            print("Interface mis en mode Etherchannel\n")
            Tabconf[Interface] = "ETH"
        case _:
            print(f"{bcolors.WARNING}Configuration non reconnue, configuration de l'interface non modifiée\n{bcolors.ENDC}")
    return Tabconf
 
def GigabitEthernet(LIST, vlan):
    conf = True
    Tabconf = ["","","","","","","",""]
    
    while conf:
        print("Sélectionner l'interface que vous souhaiter modifier")
        print(" * Taper un nombre entre 1 et 8 pour configurer l'interface correspondante")
        print(" * taper 9 pour voir la configuration de chaque interface")
        print(" * taper 0 pour finir la configuration des interfaces")
        Interface = InputNum(9)
        
        match Interface:
            case 0:
                conf = False
                print("Fin de la configuration des interfaces\n")
            case 1:
                print("vous modifié l'interface "+ str(Interface))
                Tabconf = confInt(0, Tabconf)
            case 2:
                print("vous modifié l'interface "+ str(Interface))
                Tabconf = confInt(1, Tabconf)
            case 3:
                print("vous modifié l'interface "+ str(Interface))
                Tabconf = confInt(2, Tabconf)
            case 4:
                print("vous modifié l'interface "+ str(Interface))
                Tabconf = confInt(3, Tabconf)
            case 5:
                print("vous modifié l'interface "+ str(Interface))
                Tabconf = confInt(4, Tabconf)
            case 6:
                print("vous modifié l'interface "+ str(Interface))
                Tabconf = confInt(5, Tabconf)
            case 7:
                print("vous modifié l'interface "+ str(Interface))
                Tabconf = confInt(6, Tabconf)
            case 8:
                print("vous modifié l'interface "+ str(Interface))
                Tabconf = confInt(7, Tabconf)
            case 9:
                for i in range(8):
                    print("L'interface n°" + str(i+1) + " est " + translation(Tabconf[i]))
                print("")
            case _:
                print(f"{bcolors.WARNING}Nombre non valide{bcolors.ENDC}")
    if Tabconf.count("ETH") > 0:
        LIST.append("interface Port-channel1\n")
        trunkinginterface(LIST,vlan)
        ExMark(LIST,1)        
        
    for Interface in range(8):
        LIST.append("interface GigabitEthernet0/"+str(Interface+1) + "\n")
        match Tabconf[Interface]:
            case "TR":
                trunkinginterface(LIST, vlan)
            case "AC":
                accessInterface(LIST, vlan)
            case"ETH":
                trunkinginterface(LIST,vlan)
                LIST.append(" channel-group 1 mode active\n")
        ExMark(LIST,1)

def FastEthernet(LIST, vlan):
    conf = True
    Tabconf = ["","","","","","","",""]
    
    while conf:
        print("Sélectionner l'interface que vous souhaiter modifier")
        print(" * Taper un nombre entre 1 et 8 pour configurer l'interface correspondante")
        print(" * taper 9 pour voir la configuration de chaque interface")
        print(" * taper 0 pour finir la configuration des interfaces")
        Interface = InputNum()
        
        match Interface:
            case 0:
                conf = False
                print("Fin de la configuration des interfaces\n")
            case 1:
                print("vous modifié l'interface "+ str(Interface))
                Tabconf = confInt(0, Tabconf)
            case 2:
                print("vous modifié l'interface "+ str(Interface))
                Tabconf = confInt(1, Tabconf)
            case 3:
                print("vous modifié l'interface "+ str(Interface))
                Tabconf = confInt(2, Tabconf)
            case 4:
                print("vous modifié l'interface "+ str(Interface))
                Tabconf = confInt(3, Tabconf)
            case 5:
                print("vous modifié l'interface "+ str(Interface))
                Tabconf = confInt(4, Tabconf)
            case 6:
                print("vous modifié l'interface "+ str(Interface))
                Tabconf = confInt(5, Tabconf)
            case 7:
                print("vous modifié l'interface "+ str(Interface))
                Tabconf = confInt(6, Tabconf)
            case 8:
                print("vous modifié l'interface "+ str(Interface))
                Tabconf = confInt(7, Tabconf)
            case 9:
                for i in range(8):
                    print("L'interface n°" + str(i+1) + " est " + translation(Tabconf[i]))
                print("")
            case _:
                print(f"{bcolors.WARNING}Nombre non valide{bcolors.ENDC}")
    if Tabconf.count("ETH") > 0:
        LIST.append("interface Port-channel1\n")
        trunkinginterface(LIST,vlan)
        ExMark(LIST,1)        
        
    for Interface in range(8):
        LIST.append("interface FastEthernet0/"+str(Interface+1) + "\n")
        match Tabconf[Interface]:
            case "TR":
                trunkinginterface(LIST, vlan)
            case "AC":
                accessInterface(LIST, vlan)
            case"ETH":
                trunkinginterface(LIST,vlan)
                LIST.append(" channel-group 1 mode active\n")
        ExMark(LIST,1)
   
def ConfigSwitchIP(LIST):
    ip = input("Entrez l'adresse IP : ")
    print("Entez le masque en forme slash (par exemple pour /29, entrez 29)")
    masquePointe = InputNum(32)
    masque = slashtToPointe(masquePointe)
    LIST.append("interface vlan" + str(vlan) + "\n")
    LIST.append(" ip address " + ip + " " + masque + "\n")
    ExMark(LIST, 2)
    LIST.append("line vty 0 4\n")
    LIST.append(" password bonjour\n")
    LIST.append(" login\n")

def slashtToPointe(cidr): # trouver ici : https://stackoverflow.com/questions/33750233/convert-cidr-to-subnet-mask-in-python
  cidr = int(cidr)
  mask = (0xffffffff >> (32 - cidr)) << (32 - cidr)
  return (str( (0xff000000 & mask) >> 24)   + '.' +
          str( (0x00ff0000 & mask) >> 16)   + '.' +
          str( (0x0000ff00 & mask) >> 8)    + '.' +
          str( (0x000000ff & mask)))
  


def ConfInt(LIST,vlan):
    txt = "\nInterfaces GigabitEthernet (Gi) ou FastEthernet (Fa) ?\nEcriver Gi ou Fa :" 
    debi = InputTxt(["GI","FA",""],txt)
    
    match debi:
        case "FA":
            print("Switch FastEthernet sélectionné\n")
            FastEthernet(LIST, vlan)
        case "GI":
            print("Switch GigabitEthernet sélectionné\n")
            GigabitEthernet(LIST, vlan)
        case _:
            print(f"{bcolors.WARNING}Switch GigabitEthernet automatiquement sélectionné\n{bcolors.ENDC}")
            GigabitEthernet(LIST, vlan)
    

def configSwitch(name, vlan):
    DEBUT = []
    CONFINT = []
    FIN = []
    mdp = "bonjour"
    prio = 32768
    
    if os.path.isfile(name + ".txt"):
        print(f"{bcolors.WARNING}Un fichier {name}.txt existe déja, vouler vous le remplacer ?{bcolors.ENDC}")
        txt = "Entrez Non pour passer à la configuration du switch suivant, laisser vide pour continer la configuration de ce switch\n"
        val = InputTxt(YN, txt)
        if val == "NON":
            return None
        else:
            print(f"{bcolors.WARNING}Fichier {name}.txt écrasé{bcolors.ENDC}\n")

    ConfMode = True
    while ConfMode:
        txt = "Configuration du switch :\n * NAME pour changer le nom du switch (actuellement " + name + ")\n * MDP pour mettre un mdp (actuellement " + mdp + ")\n * PRIO pour changer la prioriter (actuellement " + str(prio) + ")\n * INT pour configurer les interfaces\n * IP pour donner une adresse IP au switch\n * 0 pour quitter\n"
        
        ConfModes = ["0","INT","PRIO","IP","NAME","MDP"]
        SelecConf = InputTxt(ConfModes, txt)
        match SelecConf:
            case "NAME":
                print("\nEntrez le nouveau nom du switch :")
                name = input(" -> ")
            case "MDP":
                print("\nEntrez le nouveau mot de passe du switch :")
                mdp = input(" -> ")
            case "PRIO":
                print("Le numéro de priorité doit être un multiple de 4096 (soit 0/4096/8192/122288/16384/20480/24576/28672/32768/36864/40960/45056/49152/53248/57344/61440/65536/69632/73728/77824/81920)")
                prio = InputNum(81920)
            case "IP":
                ConfigSwitchIP(FIN)
            
            case "INT":
                ConfInt(CONFINT,vlan)
            case "0":
                ConfMode = False
                
    DEBUT.append("hostname " + name + "\n")
    ExMark(DEBUT,2)
    DEBUT.append("enable password " + mdp + "\n")
    ExMark(DEBUT,3)
    DEBUT.append("no ip domain-lookup\n")
    ExMark(DEBUT,2)
    DEBUT.append("spanning-tree mode pvst\n")
    DEBUT.append("spanning-tree vlan 1-4096 priority " + str(prio) + "\n")
    ExMark(DEBUT,5)
    
    FIN.append("exit\n")
    ExMark(FIN, 2)
    FIN.append("no cdp run\n")
    ExMark(FIN, 4)
    FIN.append("end\n")

    with open(name + ".txt", "w") as f:
        for line in DEBUT:
            f.write(line)
        for line in CONFINT:
            f.write(line)
        for line in FIN:
            f.write(line)
                        

if __name__ == "__main__":
    print("\nBienvenue dans ce script de configuration de 3 switches\n")
    print("ce script vous donnera 3 fichiers de configuration à coller dans putty pour chaque switch")
    print("-----------------------------------------------------------------------------------------------\n")
    print("pour commencer, entrer le numéro du vlan que vous utiliserer pour connecter vos machines :")

    vlan = InputNum(4096)
    print("Le numéro du vlan choisis est "+ str(vlan) + "\n")

    for switch in range(3):
        name = "Switch"+ str(switch+1)
        print("\n           CONFIGURATION DU " + name.upper() +" : ")
        print("=================================================\n")
        
        configSwitch(name, vlan)
