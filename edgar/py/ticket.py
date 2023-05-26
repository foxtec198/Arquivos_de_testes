from barcode import EAN13
from win32printing import win32print
from os import remove
from sys import exit
import aspose.words as aw

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
        self.codigo_de_barras = EAN13(str(self.codigo))
        self.codigo_de_barras.save(self.nome_arquivo)
        # Converte de SVG to PNG
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        svg = builder.insert_image(f"{self.nome_arquivo}.svg")
        svg.image_data.save(f"{self.nome_arquivo}.png")
        
        
        
    def imprimir(self):
        impressora_definida = win32print.GetDefaultPrinter()# Definido imp padrão2
        impressora = win32print.OpenPrinter(impressora_definida)# Inicializando a impressora
        win32print.StartDocPrinter(impressora, 1, (f'{self.nome_arquivo}.png', None, None))# Definindo o arquivo
        win32print.EndDocPrinter(impressora)
        win32print.ClosePrinter(impressora)
        remove(f"{self.nome_arquivo}.svg")
        remove(f"{self.nome_arquivo}.png")
        print('Imprimindo...')

App()