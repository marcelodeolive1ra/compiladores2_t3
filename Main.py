import antlr4
from ANTLR.t3_cc2Lexer import *
from ANTLR.t3_cc2Parser import *
from ANTLR.t3_cc2Visitor import *
from GeradorDeCodigo import *
from ErrosSintaticosErrorListener import ErrosSintaticosErrorListener

import os
DIRETORIO_PROJETO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAMINHO_ARQUIVOS_ENTRADA = '/T3_CC2_Pycharm/arquivos_testes/entrada/'
CAMINHO_ARQUIVOS_SAIDA = '/T3_CC2_Pycharm/arquivos_testes/saida/'


CASO_DE_TESTE = 'teste01.txt'
with open(DIRETORIO_PROJETO + CAMINHO_ARQUIVOS_ENTRADA + CASO_DE_TESTE, encoding='utf-8') as f:
    programa = f.read()

input = antlr4.InputStream(programa)

lexer = t3_cc2Lexer(input=input)

lexer.removeErrorListeners()
erros_sintaticos = ErrosSintaticosErrorListener()
lexer.addErrorListener(erros_sintaticos)

try:
    tokens = antlr4.CommonTokenStream(lexer=lexer)
    parser = t3_cc2Parser(tokens)
    programa = parser.site()

    print(programa.getText())
    print(parser.literalNames)

    gerador_de_codigo = GeradorDeCodigo()
    gerador_de_codigo.visitSite(programa)

    codigo_gerado = gerador_de_codigo.getCodigo()

    arquivo_saida = open(DIRETORIO_PROJETO + CAMINHO_ARQUIVOS_SAIDA + 'teste01.html', 'w', encoding='utf-8')
    arquivo_saida.write(codigo_gerado)
    arquivo_saida.close()

    print('\n' + codigo_gerado)

except:
    if erros_sintaticos.getErrosSintaticos() != "":
        print(erros_sintaticos.getErrosSintaticos())
    else:
        print("Erros semânticos")
