#! /usr/bin/env python3

etherInt = [False, False, False, False, False, False, False, False]


def ExMark(file, nbLigne): # bah c'est pour mettre plein de poin d'exclamation
    for i in range(nbLigne):
        file.write("!\n")

def EtherConfig(f, vlan): # Sert à configurer l'Etherchannel
    try:
        nbInt = int(input("Combien d'interfaces sont en Etherchannel ?"))
        for i in range(nbInt):
            try:
                inter = int(input("Interface n° ? : "))
                etherInt[inter-1] = True
            except:
                print("Le numéro de l'interface est incorrect")
                exit()
        f.write("interface Port-channel1\n")
        trunkinginterface(f, vlan)
        ExMark(f, 1)
    except:
        print("Erreur, Le nombre d'interface n'est pas compris n'est pas compris")
        exit()
    
def trunkinginterface(file, vlan): # fonction appeler pour configuer une interface en mode trunk
    file.write(" switchport trunk allowed vlan " + str(vlan) + "\n")
    file.write(" switchport trunk encapsulation dot1q\n")
    file.write(" switchport mode trunk\n")
    
def accessInterface(file,vlan): # fonction appeler pour configuer une interface en mode accès
    file.write(" switchport access vlan " + str(vlan) + "\n")
    file.write(" switchport mode access\n")
    file.write(" switchport nonegociate\n")
  
def GigabitEthernet(f, vlan):
    
    try:
        ether = input("Il y a t'il des interfaces en Etherchannel ?\nDe base non, ecrivez oui pour entre dans la configuration de l'Etherchannel : ")
    except:
        print("Considérez comme un non")
    if ether.upper() == "OUI":
        EtherConfig(f, vlan)
        
    for interface in range(8):
        f.write("interface GigabitEthernet0/" + str(interface+1) + "\n")
        if etherInt[interface]:
            print("\nL'interface n°" + str(interface+1) + " fait partie de l'Etherchannel et est donc automatiquement mit en trunking")
            trunkinginterface(f, vlan)
            f.write(" channel-group 1 mode active\n")
            ExMark(f, 1)
            
        else : 
            try:
                conf = input("\nConfiguration de l'interface n°" + str(interface+1) + " :\nAc pour mode accès, Tr pour trunk et vide pour laisser la configuration par default :\n")
            except:
                print("Je comprends pas")
            match conf.upper():
                case "AC":
                    accessInterface(f, vlan)
                    ExMark(f, 1)
                    print("Mode accès sélectionné pour l'interface " + str(interface))
                case "TR":
                    trunkinginterface(f, vlan)
                    print("Mode trunking sélectionné pour l'interface " + str(interface))
                    ExMark(f, 1)
                case _:
                    ExMark(f, 1)

def FastEthernet(f, vlan):
    try:
        ether = input("Il y a t'il des interfaces en Etherchannel ?\nDe base non, ecrivez oui pour entre dans la configuration de l'Etherchannel : ")
    except:
        print("Considérez comme un non")
    if ether.upper() == "OUI":
        EtherConfig(f, vlan)
        
    for interface in range(8):
        f.write("interface FastEthernet0/" + str(interface+1) + "\n")
        if etherInt[interface]:
            print("\nL'interface n°" + str(interface+1) + " fait partie de l'Etherchannel et est donc automatiquement mit en trunking")
            trunkinginterface(f, vlan)
            f.write(" channel-group 1 mode active\n")
            ExMark(f, 1)
            
        else : 
            try:
                conf = input("\nConfiguration de l'interface n°" + str(interface+1) + " :\nAc pour mode accès, Tr pour trunk et vide pour laisser la configuration par default :\n")
            except:
                print("Je comprends pas")
            match conf.upper():
                case "AC":
                    accessInterface(f, vlan)
                    ExMark(f, 1)
                    print("Mode accès sélectionné pour l'interface " + str(interface))
                case "TR":
                    trunkinginterface(f, vlan)
                    print("Mode trunking sélectionné pour l'interface " + str(interface))
                    ExMark(f, 1)
                case _:
                    ExMark(f, 1)
    
def configSwitch(name, vlan):
            
    with open(name + ".txt", "w") as f:
        f.write("hostname " + name + "\n")
        ExMark(f,2)
        f.write("enable password bonjour\n")
        ExMark(f,3)
        f.write("no ip domain-lookup\n")
        ExMark(f,2)
        f.write("spanning-tree mode pvst\n")
        print("Priorité du Switch " + name +"(soit 0/4096/8192/122288/16384/20480/24576/28672/32768/36864/40960/45056/49152/53248/57344/61440/65536/69632/73728/77824/81920)")
        try :
            prio = int(input("Priorité de base 32768 : "))
            f.write("spanning-tree vlan 1-4096 priority " + str(prio) + "\n")
        except:
            print("Valeur de base sélectionné\n")
            ExMark(f, 1)
        
        print("Switch GigabitEthernet (Gi) ou FastEthernet (Fa) ?")
        
        debi = "Gi"
        try:
            debi = input("Ecriver Gi ou Fa (de base Gi sélectionné) : ")
        except:
            print("Valeur de base sélectionné")
        
        match debi.upper():
            case "FA":
                print("Switch FastEthernet sélectionné\n")
                FastEthernet(f, vlan)
            case _:
                print("Switch GigabitEthernet sélectionné\n")
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
                print("Erreur dans la configuration de l'adresse IP")
        
        ExMark(f, 2)
        f.write("no cdp run\n")
        ExMark(f, 4)
        f.write("end\n")
                        
print("\nBienvenue dans ce script de configuration de 3 switches\n")
print("ce script vous donnera 3 fichiers de configuration à coller dans putty pour chaque switch")
print("-----------------------------------------------------------------------------------------------\n")
print("pour commencer, entrer le numéro du vlan que vous utiliserer pour connecter vos machines ?")
try:
    vlan = int(input("n° vlan : "))
    print("Le numéro du vlan choisis est "+ str(vlan) + "\n")
except:
    print("Le numéro de Vlan doit être un nombre entier")
    exit()
for switch in range(3):
    name = "Switch"+ str(switch+1)
    print("\nCONFIGURATION DU " + name.upper() +" : ")
    print("==============================================\n")
    
    configSwitch(name, vlan)

