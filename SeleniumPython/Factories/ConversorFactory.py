from enum import Enum

class Extensao(Enum):
    msg = 'msg'
    html = 'html'
    htm = 'htm'
    tiff = 'tiff'
    tif = 'tif'
    pdf = 'pdf'
    doc = 'doc'
    docx = 'docx'

class Conversor:
    pass

class ConversorMsgParaHtml(Conversor):
    pass

class ConversorHtmlParaPdf(Conversor):
    pass

class ConversorTiffParaPdf(Conversor):
    pass

class ConversorPdfParaPdfa(Conversor):
    pass

class ConversorWordParaPdf(Conversor):
    pass

class ConversorFactory:
    def criar(self, extensao: Extensao) -> Conversor:
        if extensao == Extensao.msg:
            return ConversorMsgParaHtml()

        elif extensao in {Extensao.html, Extensao.htm}:
            return ConversorHtmlParaPdf()

        elif extensao in {Extensao.tiff, Extensao.tif}:
            return ConversorTiffParaPdf()

        elif extensao == Extensao.pdf:
            return ConversorPdfParaPdfa()

        elif extensao in {Extensao.doc, Extensao.docx}:
            return ConversorWordParaPdf()

        else:
            raise Exception(f"Verifique se a extensão do arquivo desejado para conversão está correto. Extensão indicada: {extensao}")

# Exemplo de uso
factory = ConversorFactory()
conversor = factory.criar(Extensao.pdf)
