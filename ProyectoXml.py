from device import *
from group import *
from capability import *
import sys

def deviceFunction(listLine):
    listDevice = []
    for elem in listLine:
        if(elem == "id"):
            listDevice.append(listLine[2])
        elif(elem == "user_agent"):
            if(listLine[4] == "fall_back"):
                listDevice.append("")
            else:
                listDevice.append(listLine[4])
        elif(elem == "fall_back"):
            listDevice.append(listLine[listLine.index("fall_back")+1])
    return listDevice

def menu():
    print("\t\t\t**************************************")
    print( "\t\t\t     ANALIZADOR SEMANTICO")
    print( "\t\t\t  José Antonio Vélez Gómez")
    print( "\t\t\t  Leonel Fernando Ramirez  Gonzalez")
    print( "\t\t\t  Kevin Guillermo Campuzano Castillo")
    print( "\t\t\t**************************************")

    contentFile = "wurfl-2.3.xml"
    file = lineFile(contentFile)
    removeLines(file)

def lineFile(contentFile):
    listFile = []
    with open(contentFile) as f:
      for line in f:
          listFile.append(line)
    return listFile

def removeEmpty (listSplit):
    listFile = []
    for elem in listSplit:
        if(elem != ""):
            listFile.append(elem)
    return listFile

def menuPrincipal(listD, nameCapability):
    if(listD == []): print ("\t\t\tNo exixten Devices con esa Capability")

    print( "\n\t\t\t\tINGRESE LA OPCION")
    print( "\t\t1) Cuantos Devices tienen la Capability ingresada")
    print( "\t\t2) Cuales Devices tienen la Capability ingresada")
    print( "\t\t3) Desea SALIR")
    number = input ("\t\tIngrese su opcion: ")

    if(number == "1"):
        print ("Existen ",len(listD)," Device")
    elif(number == "2"):
        print ("\n\tLos Devices que tienen la Capability : "+nameCapability+"\n",listD)
    elif(number == "3"):
        sys.exit()
    else:
        menuPrincipal(listD, nameCapability)


def removeLines (file):
    head, *tail = file
    if ("<devices" in head):
        nameCapability = input("\nIngrese todas los Capability que desee consultar en el Device: ")
        listC = listCapability (nameCapability)
    else: removeLines(tail)

def listCapability (nameCapability):
    if (nameCapability == ""): return []
    else: return removeEmpty(my_split([nameCapability], [","," ",";","\""]))
    
def my_split(text_list, delimiters):
    for delim in delimiters:
        split_result = []
        for chain in text_list:
            split_result += chain.split(delim)
        text_list = split_result
    return text_list

def listDevice(listFile, device, group, capabilityUser, fall_back, listFallBack, n1, n2):
    lD = []
    for elem in listFile:
        listSplit = my_split([elem], ["<",">","="," ","\t","\n","\"","\\"])
        list1 = removeEmpty (listSplit)
        headList1, *tailList = list1

        nameDevice = device.getIdDevice()
        f_bDevice = device.getFallBackDevice()

        if(headList1 == "device"):
            device.setDevice(deviceFunction(list1))
            idDevice = device.getIdDevice()

            if(idDevice == f_bDevice):
                listFallBack = listFallBack+[nameDevice]
            else: listFallBack = []
            n1 = n2
        elif(headList1 == "group"):
            group.setGroup(groupFunction(list1))
        elif(headList1 == "capability"):
            capability = Capability("","")
            capability.setCapability(capabilityFunction(list1))
            nameCapability = capability.getNameCapability()
            idDevice = device.getIdDevice()
            if(nameCapability in capabilityUser):
                if(n1 <= 1):
                    lD.append(listFallBack+[idDevice])
                    listFallBack = []
                    n1 = n2
                else: n1 = (n1-1)
    return lD
