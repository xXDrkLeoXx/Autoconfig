#! /usr/bin/env python3

def ExMark(file, nbLigne): # bah c'est pour mettre plein de poin d'exclamation
    for i in range(nbLigne):
        file.write("!\n")
        
def configSwitch(name):
        
    with open(name + ".txt", "w") as f:
        f.write("hostname " + name + "\n")
        ExMark(f,2)
        f.write("enable password bonjour\n")
        ExMark(f,3)
        f.write("no ip domain-lookup\n")
        ExMark(f,2)
        f.write("spanning-tree mode pvst\n")
        
        f.write("interface FastEthernet0/7\n")
        trunkinginterface(54)
        
        
configSwitch("S1")

def trunkinginterface(vlan):
    f.write(" switchport trunk allowed vlan " + str(vlan) + "\n")
    f.write(" switchport trunk encapsulation dot1q\n")
    f.write(" switchport mode trunk\n")
    
