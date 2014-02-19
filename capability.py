class Capability:
    """Abstraccion de los objetos capability."""
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def setCapability(self, listaC):
        name, value,*list = listaC
        self.name = name
        self.value = value
    
    def getNameCapability(self):
        return self.name
    
    def setNameCapability(self, name):
        self.name = name


    def getValueCapability(self):
        return self.value
    
    def setValueCapability(self, value):
        self.value = value
