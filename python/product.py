from typing_extensions import Self


class Product:
    def __init__(self,code,name,price) -> None:
        self._code = code
        self._price = price 
        self._name = name

    @property
    def code(self):
        return self._code 

    @code.setter 
    def code(self,cod):
        if not isinstance(cod,str):
            print('The code is wrong, try again!')
            return
        self._code = cod

    @property
    def price(self):
        return self._price

    @price.setter 
    def price(self,price_in):
        if not isinstance(price_in,float):
            print('The price is wrong, try again!')
            return
        self._price = price_in
    
    @property
    def name(self):
        return self._name

    @name.setter 
    def name(self,name_in):
        if not isinstance(name_in,str):
            print('The name is wrong, try again!')
            return
        self._name = name_in

