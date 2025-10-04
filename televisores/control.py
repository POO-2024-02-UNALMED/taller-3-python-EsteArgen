from televisores.tv import TV

class Control:

    #definicion de atributo tv

    def __init__ (self):
        self.tv = None

#definicion de set y get del atributo Tv

    def getTv(self):
        return self.tv
    def setTv(self,tv):
        self.tv = tv

#definicion de metodos turnOn y turnOff

    def turnOn(self):
        self.tv.turnOn()
    def turnOff(self):
        self.tv.turnOff()
    
#definicion de metodos canalUp y canalDown

    def canalUp(self):
        self.tv.canalUp()
    def canalDown(self):
        self.tv.canalDown()
    
#definicion de metodos volumenUp y volumenDown

    def volumenUp(self):
        self.tv.volumenUp()
    def volumenDown(self):
        self.tv.volumenDown()

#definicion de metodos setCanal y setVolumen

    def setCanal(self,canal):
        self.tv.setCanal(canal)
    def setVolumen(self,volumen):
        self.tv.setVolumen(volumen)

#definicion de metodo enlazar

    def enlazar(self,tv):
        self.tv = tv
        self.tv.setControl(self)
