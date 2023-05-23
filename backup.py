import barcode
from barcode.writer import ImageWriter
import win32print
from PIL import Image

def imprimir_ticket(codigo):
    # Gerar código de barras
    ean = barcode.get_barcode_class('ean13')
    codigo_de_barras = ean(str(codigo), writer=ImageWriter())

    # Salvar código de barras em um arquivo temporário
    nome_arquivo = 'temp_code.png'
    codigo_de_barras.save(nome_arquivo)

    # Carregar a imagem da logo da empresa
    logo_empresa = Image.open('logo_empresa.png')

    # Criar uma nova imagem para combinar a logo e o código de barras
    ticket = Image.new('RGB', (300, 300), (255, 255, 255))
    ticket.paste(logo_empresa, (50, 50))
    ticket.paste(codigo_de_barras, (50, 150))

    # Imprimir ticket
    win32print.SetDefaultPrinter(win32print.GetDefaultPrinter())
    win32print.StartDocPrinter(win32print.GetDefaultPrinter(), 1, ("Ticket de Produto", None, "RAW"))
    win32print.StartPagePrinter(win32print.GetDefaultPrinter())

    # Configurações do ticket
    mensagem = "Obrigado pela compra!"

    # Imprimir mensagem
    win32print.WritePrinter(win32print.GetDefaultPrinter(), mensagem.encode('utf-8'))
    win32print.WritePrinter(win32print.GetDefaultPrinter(), b'\n\n')  # Duas quebras de linha

    # Imprimir ticket
    ticket.save('temp_ticket.png')
    with open('temp_ticket.png', 'rb') as f:
        win32print.WritePrinter(win32print.GetDefaultPrinter(), f.read())

    win32print.EndPagePrinter(win32print.GetDefaultPrinter())
    win32print.EndDocPrinter(win32print.GetDefaultPrinter())

    # Remover arquivos temporários
    os.remove(nome_arquivo)
    os.remove('temp_ticket.png')

# Exemplo de uso
while True:
    codigo = input("Bipe o código de barras do produto (ou 'sair' para encerrar): ")
    if codigo.lower() == 'sair':
        break
    imprimir_ticket(codigo)