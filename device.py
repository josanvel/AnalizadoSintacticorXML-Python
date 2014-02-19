class Device:
    """Abstraccion de los objetos device."""
    def __init__(self, idD, user_agent, fall_back):
        self.idD = idD
        self.user_agent = user_agent
        self.fall_back = fall_back

    def setDevice(self, lista):
        idD, ug, fb, *listD = lista
        self.idD = idD
        self.user_agent = ug
        self.fall_back = fb
    
    def getIdDevice(self):
        return self.idD
    
    def setIdDevice(self, idD):
        self.idD = idD

    
    def getUserAgentDevice(self):
        return self.user_agent

    def setUserAgentDevice(self, user_agent):
        self.user_agent = user_agent


    def getFallBackDevice(self):
        return self.fall_back

    def setFallBackDevice(self, fall_back):
        self.fall_back = fall_back
