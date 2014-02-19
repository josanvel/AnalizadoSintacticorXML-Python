class Group:
    """Abstraccion de los objetos group."""
    def __init__(self, idG):
        self.idG = idG

    def setGroup(self, lista):
        idG, *list = lista
        self.idG = idG
    
    def getIdGroup(self):
        return self.idG
    
    def setIdGroup(self, idG):
        self.idG = idG
