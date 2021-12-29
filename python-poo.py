class complexo():
    def __init__(self,checker) -> None:
        while type(checker) is not int:
            try:
                checker = int(checker)
                print("Inteiro detectado!!!  ",checker)
            except:
                checker = input('Digite um valor válido: ')
        print('verificado!')
    def printar(self):
        print('mika')
    def __del__(self):
        print('Destruindo objeto')
moka = complexo('mika')
moka.printar()
del moka