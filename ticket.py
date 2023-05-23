from barcode import EAN13
from barcode.writer import ImageWriter
from win32printing import win32print
from os import remove

class App():
    def __init__(self):            
        self.nome_arquivo = 'temp_code'
        self.w32 = win32print
        while True:
            try:
                self.codigo = input("Bipe o código de barras do produto (ou 'sair' para encerrar): ")
                self.gerar_cod()
                break
            except:
                print('Valor incorreto, Digite novamente!')   
    
    def gerar_cod(self):
        self.codigo_de_barras = EAN13(str(self.codigo), writer=ImageWriter())
        self.codigo_de_barras.save(self.nome_arquivo)
        self.imprimir()
        
    def imprimir(self):
        lista_impressoras = self.w32.EnumPrinters(2)
        #print(lista_impressoras)
        impressora = lista_impressoras[5]
        impressora = impressora[2]
        self.w32.SetDefaultPrinter(impressora)
        
        # Imprimir Titulo
        #nome_empresa = str("RCHLO")
        #self.w32.WritePrinter(impressora, nome_empresa)
        #self.w32.WritePrinter(self.w32.GetDefaultPrinter(), b'\n')

        # Imprimir mensagem
        #mensagem = "Cumpom não fiscal!"
        #self.w32.WritePrinter(self.w32.GetDefaultPrinter(), mensagem.encode('utf-8'))
        #self.w32.WritePrinter(self.w32.GetDefaultPrinter(), b'\n\n')
        
        # Finalização
        with open(f'{self.nome_arquivo}.png', 'rb') as f:
            self.w32.WritePrinter(self.w32.GetDefaultPrinter(), f.read())
            
        self.w32.EndPagePrinter(self.w32.GetDefaultPrinter())
        self.w32.EndDocPrinter(self.w32.GetDefaultPrinter())

        # Remover arquivos
        remove(f'{self.nome_arquivo}.png')
App()   