from barcode import EAN13
from barcode.writer import ImageWriter
import win32print
from os import remove
from sys import exit

class App():
    def __init__(self):
        self.nome_arquivo = 'temp_code'
        while True:
            try:
                self.gerar_cod()
                self.imprimir()
            except:
                if self.codigo.lower() == 'sair':exit()
                print('Valor incorreto, Digite novamente!')   

    def gerar_cod(self):
        self.codigo = input("Bipe o código de barras do produto [Sair] : ")
        self.codigo_de_barras = EAN13(str(self.codigo), writer = ImageWriter())
        self.codigo_de_barras.save(self.nome_arquivo)
          
    def imprimir(self):
        impressora_definida = win32print.GetDefaultPrinter()# Definido imp padrão2
        impressora = win32print.OpenPrinter(impressora_definida)# Inicializando a impressora
        win32print.StartDocPrinter(impressora, 1, (f'{self.nome_arquivo}.png', None, None))# Definindo o arquivo
        win32print.EndDocPrinter(impressora)
        win32print.ClosePrinter(impressora)
        remove(f"{self.nome_arquivo}.png")
        print('Imprimindo...')

App()