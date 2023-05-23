from barcode import EAN13
from barcode.writer import ImageWriter
from win32printing import win32print
from os import remove

class App():
    def __init__(self):            
        self.nome_arquivo = 'temp_code'
        self.w32 = win32print
        while True:
            # try:
            self.codigo = input("Bipe o código de barras do produto (ou 'sair' para encerrar): ")
            self.gerar_cod()
                # break
            # except:
                # print('Valor incorreto, Digite novamente!')   
    
    def gerar_cod(self):
        self.codigo_de_barras = EAN13(str(self.codigo), writer=ImageWriter())
        self.codigo_de_barras.save(self.nome_arquivo)
        self.imprimir()
        
    def imprimir(self):
        defp = win32print.GetDefaultPrinter()
        prt = win32print.OpenPrinter(defp)
        
        win32print.StartDocPrinter(prt, 1, (f'{self.nome_arquivo}.png', None, None))
        win32print.EndDocPrinter(prt)
        win32print.ClosePrinter(prt)
        
        remove(f'{self.nome_arquivo}.png')
        print('Imprimindo...')
        
App()   