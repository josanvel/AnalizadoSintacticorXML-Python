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

def removeLines (file):
    head, *tail = file
    if ("<devices" in head):
        nameCapability = input("\nIngrese todas los Capability que desee consultar en el Device: ")
        listC = listCapability (nameCapability)
    else: removeLines(tail)

def listCapability (nameCapability):
    if (nameCapability == ""): return []
    else: return removeEmpty(my_split([nameCapability], [","," ",";","\""]))

def removeEmpty (listSplit):
    listFile = []
    for elem in listSplit:
        if(elem != ""):
            listFile.append(elem)
    return listFile
    
def my_split(text_list, delimiters):
    for delim in delimiters:
        split_result = []
        for chain in text_list:
            split_result += chain.split(delim)
        text_list = split_result
    return text_list
