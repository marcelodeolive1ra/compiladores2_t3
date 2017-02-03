import antlr4
import sys
from ANTLR.t3_cc2Lexer import *
from GeradorDeCodigo import *
from ErrosSintaticosErrorListener import ErrosSintaticosErrorListener

import os
DIRETORIO_PROJETO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SINTATICO = 'sintatico/'
SEMANTICO = 'semantico/'
GERACAO_DE_CODIGO = 'geracao-codigo/'

TESTE = SEMANTICO

CAMINHO_ARQUIVOS_ENTRADA = '/T3_CC2_Pycharm/casos_de_teste/entrada/' + TESTE
CAMINHO_ARQUIVOS_SAIDA = '/T3_CC2_Pycharm/casos_de_teste/saida/' + TESTE


CASO_DE_TESTE = 'teste01.txt'
with open(DIRETORIO_PROJETO + CAMINHO_ARQUIVOS_ENTRADA + CASO_DE_TESTE, encoding='utf-8') as f:
    programa = f.read()

try:
    input = antlr4.InputStream(programa)
    lexer = t3_cc2Lexer(input=input)
    tokens = antlr4.CommonTokenStream(lexer=lexer)

    parser = t3_cc2Parser(tokens)
    parser.removeErrorListeners()
    erros_sintaticos = ErrosSintaticosErrorListener()
    parser.addErrorListener(erros_sintaticos)

    programa = parser.site()

    gerador_de_codigo = GeradorDeCodigo()
    gerador_de_codigo.visitSite(programa)

    codigo_gerado = gerador_de_codigo.getCodigo()

    arquivo_saida = open(DIRETORIO_PROJETO + CAMINHO_ARQUIVOS_SAIDA + 'teste01.html', 'w', encoding='utf-8')
    arquivo_saida.write(codigo_gerado)
    arquivo_saida.close()

    print('\n' + codigo_gerado)

except Exception as e:
    print(e, file=sys.stderr)
    # print(e.with_traceback())
