#! /usr/bin/env python3

def ExMark(file, nbLigne): # bah c'est pour mettre plein de poin d'exclamation
    for i in range(nbLigne):
        file.write("!\n")

def trunkinginterface(file, vlan):
    file.write(" switchport trunk allowed vlan " + str(vlan) + "\n")
    file.write(" switchport trunk encapsulation dot1q\n")
    file.write(" switchport mode trunk\n")
    
def accessInterface(file,vlan):
    file.write(" switchport access vlan " + str(vlan) + "\n")
    file.write(" switchport mode access\n")
    file.write(" switchport nonegociate\n")
  
def GigabitEthernet(f, vlan):
      print("GigabitEthernet")
      
def FastEthernet(f, vlan):
    print("FastEthernet")
def configSwitch(name):
            
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
            debi = input("Ecriver Gi ou Fa (de base Gi sélectionné)")
        except:
            print("Valeur de base sélectionné")
        
        match debi:
            case "Fa":
                FastEthernet(f, 45)
            case "Gi":
                GigabitEthernet(f, 46)
            case _:
                print("G pa Compris")
        
configSwitch("S1")

