#! /usr/bin/env python3
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

def InputNum():
    try:
        Num = int(input("-> "))
        return Num
    except:
        print(f"{bcolors.FAIL}Valeur non numérique{bcolors.ENDC}")
        return InputNum()


def ExMark(file, nbLigne): # bah c'est pour mettre plein de poin d'exclamation
    for i in range(nbLigne):
        file.write("!\n")

def trunkinginterface(file, vlan): # fonction appeler pour configuer une interface en mode trunk
    file.write(" switchport trunk allowed vlan " + str(vlan) + "\n")
    file.write(" switchport trunk encapsulation dot1q\n")
    file.write(" switchport mode trunk\n")
    file.write(" switchport nonegotiate\n")
    
def accessInterface(file,vlan): # fonction appeler pour configuer une interface en mode accès
    file.write(" switchport access vlan " + str(vlan) + "\n")
    file.write(" switchport mode access\n")
    file.write(" switchport nonegoiate\n")

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
    mode = input("Mode de Configuration\nVous aver le choix entre :\n * tr pour Trunking\n * ac pour mode accès\n * eth pour Etherchannel\n-> ")
    
    match mode.upper():
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
 
def GigabitEthernet(f, vlan):
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
                print("vous modifié l'iterface "+ str(Interface))
                Tabconf = confInt(0, Tabconf)
            case 2:
                print("vous modifié l'iterface "+ str(Interface))
                Tabconf = confInt(1, Tabconf)
            case 3:
                print("vous modifié l'iterface "+ str(Interface))
                Tabconf = confInt(2, Tabconf)
            case 4:
                print("vous modifié l'iterface "+ str(Interface))
                Tabconf = confInt(3, Tabconf)
            case 5:
                print("vous modifié l'iterface "+ str(Interface))
                Tabconf = confInt(4, Tabconf)
            case 6:
                print("vous modifié l'iterface "+ str(Interface))
                Tabconf = confInt(5, Tabconf)
            case 7:
                print("vous modifié l'iterface "+ str(Interface))
                Tabconf = confInt(6, Tabconf)
            case 8:
                print("vous modifié l'iterface "+ str(Interface))
                Tabconf = confInt(7, Tabconf)
            case 9:
                for i in range(8):
                    print("L'interface n°" + str(i+1) + " est " + translation(Tabconf[i]))
                print("")
            case _:
                print(f"{bcolors.WARNING}Nombre non valide{bcolors.ENDC}")
    if Tabconf.count("ETH") > 0:
        f.write("interface Port-channel1\n")
        trunkinginterface(f,vlan)
        ExMark(f,1)        
        
    for Interface in range(8):
        f.write("interface GigabiEthernet0/"+str(Interface+1) + "\n")
        match Tabconf[Interface]:
            case "TR":
                trunkinginterface(f, vlan)
            case "AC":
                accessInterface(f, vlan)
            case"ETH":
                trunkinginterface(f,vlan)
                f.write(" channel-group 1 mode active\n")
        ExMark(f,1)

def FastEthernet(f, vlan):
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
                print("vous modifié l'iterface "+ str(Interface))
                Tabconf = confInt(0, Tabconf)
            case 2:
                print("vous modifié l'iterface "+ str(Interface))
                Tabconf = confInt(1, Tabconf)
            case 3:
                print("vous modifié l'iterface "+ str(Interface))
                Tabconf = confInt(2, Tabconf)
            case 4:
                print("vous modifié l'iterface "+ str(Interface))
                Tabconf = confInt(3, Tabconf)
            case 5:
                print("vous modifié l'iterface "+ str(Interface))
                Tabconf = confInt(4, Tabconf)
            case 6:
                print("vous modifié l'iterface "+ str(Interface))
                Tabconf = confInt(5, Tabconf)
            case 7:
                print("vous modifié l'iterface "+ str(Interface))
                Tabconf = confInt(6, Tabconf)
            case 8:
                print("vous modifié l'iterface "+ str(Interface))
                Tabconf = confInt(7, Tabconf)
            case 9:
                for i in range(8):
                    print("L'interface n°" + str(i+1) + " est " + translation(Tabconf[i]))
                print("")
            case _:
                print(f"{bcolors.WARNING}Nombre non valide{bcolors.ENDC}")
    if Tabconf.count("ETH") > 0:
        f.write("interface Port-channel1\n")
        trunkinginterface(f,vlan)
        ExMark(f,1)        
        
    for Interface in range(8):
        f.write("interface FastEthernet0/"+str(Interface+1) + "\n")
        match Tabconf[Interface]:
            case "TR":
                trunkinginterface(f, vlan)
            case "AC":
                accessInterface(f, vlan)
            case"ETH":
                trunkinginterface(f,vlan)
                f.write(" channel-group 1 mode active\n")
        ExMark(f,1)
   
    
def configSwitch(name, vlan):
            
    with open(name + ".txt", "w") as f:
        f.write("hostname " + name + "\n")
        ExMark(f,2)
        f.write("enable password bonjour\n")
        ExMark(f,3)
        f.write("no ip domain-lookup\n")
        ExMark(f,2)
        f.write("spanning-tree mode pvst\n")
        try:
            BoolPrio = input("Souhaiter vous modifier la priorite du switch \nde base non, écriver oui si vous souhaitez la modifier :\n -> ")
            
            if BoolPrio.upper() == "OUI":
                print("Le numéro de priorité doit être un multiple de 4096 (soit 0/4096/8192/122288/16384/20480/24576/28672/32768/36864/40960/45056/49152/53248/57344/61440/65536/69632/73728/77824/81920)")
                prio = InputNum()
                f.write("spanning-tree vlan 1-4096 priority " + str(prio) + "\n")
        except:
            print("Priorité non modifiée\n")
        ExMark(f, 5)
        
        print("\nSwitch GigabitEthernet (Gi) ou FastEthernet (Fa) ?")
        
        debi = input("Ecriver Gi ou Fa (de base Gi sélectionné) :\n -> ")
        
        match debi.upper():
            case "FA":
                print("Switch FastEthernet sélectionné\n")
                FastEthernet(f, vlan)
            case "GI":
                print("Switch GigabitEthernet sélectionné\n")
                GigabitEthernet(f, vlan)
            case _:
                print(f"{bcolors.WARNING}Switch GigabitEthernet automatiquement sélectionné\n{bcolors.ENDC}")
                GigabitEthernet(f, vlan)
        
        BoolIp = input("Le switch " + name + " à t'il une adresse IP pour se connecter en telnet ou ssh ?\ntaper oui pour configurer l'adresse IP, sinon laisser vide : ")
        if BoolIp.upper() == "OUI":
            try:
                ip = input("Entrez l'adresse IP : ")
                masque = input("Entrez le masque de l'adresse IP sous la forme décimal (255.255.255.0 par exemple) : ")
                f.write("interface vlan" + str(vlan) + "\n")
                f.write(" ip address " + ip + " " + masque + "\n")
                ExMark(f, 2)
                f.write("line vty 0 4\n")
                f.write(" password bonjour\n")
                f.write(" login\n")
        
            except:
                print(f"{bcolors.FAIL}Erreur dans la configuration de l'adresse IP{bcolors.ENDC}")
        
        ExMark(f, 2)
        f.write("no cdp run\n")
        ExMark(f, 4)
        f.write("end\n")
                        

if __name__ == "__main__":
    print("\nBienvenue dans ce script de configuration de 3 switches\n")
    print("ce script vous donnera 3 fichiers de configuration à coller dans putty pour chaque switch")
    print("-----------------------------------------------------------------------------------------------\n")
    print("pour commencer, entrer le numéro du vlan que vous utiliserer pour connecter vos machines :")

    vlan = InputNum()
    print("Le numéro du vlan choisis est "+ str(vlan) + "\n")

    for switch in range(3):
        name = "Switch"+ str(switch+1)
        print("\n           CONFIGURATION DU " + name.upper() +" : ")
        print("=================================================\n")
        
        configSwitch(name, vlan)
