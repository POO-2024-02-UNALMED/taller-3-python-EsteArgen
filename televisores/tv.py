class TV:

#definicion de atributos   
 
    numTV = 0
    def __init__ (self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.precio = 500
        self.volumen = 1
        self.control = None
        TV.numTV += 1

#Definicion de set y get para los atributos marca, canal, precio, volumen y control

    def setMarca(self,marca):
        self.marca = marca
    def getMarca(self):
        return self.marca
    def setCanal(self,canal):
        if (canal <= 120 and canal >= 1 and self.estado == True):
            self.canal = canal 
    def getCanal(self):
        return self.canal
    def setPrecio(self,precio):
        self.precio = precio
    def getPrecio(self):
        return self.precio
    def setVolumen(self,volumen):
        if (volumen <= 7 and volumen >= 0 and self.estado == True):
            self.volumen = volumen
    def getVolumen(self):
        return self.volumen
    def setControl(self,control):
        self.control = control
    def getControl(self):
        return self.control

#definicion de set y get para el atributo de clase numTV
    def setNumTV(numTV):
        TV.numTV = numTV
    def getNumTV():
        return TV.numTV

#definicion de turnOff y turnOn
    def turnOn(self):
        self.estado = True
    def turnOff(self):
        self.estado = False

#definicion de getEstado
    def getEstado(self):
        return self.estado

#definicion de canalUp y canalDown

    def canalUp(self):
        if self.canal < 120 and self.estado is True:
            self.canal += 1
    def canalDown(self):
        if self.canal > 1 and self.estado is True:
            self.canal -= 1

#definicion de volumenUp y volumenDown

    def volumenUp(self):
        if self.volumen < 7 and self.estado is True:
            self.volumen += 1
    def volumenDown(self):
        if self.volumen > 0 and self.estado is True:
            self.volumen -= 1
