# UNIVERSIDADE FEDERAL DE SÃO CARLOS
# Construção de Compiladores 2 - 2016/2
# Trabalho 3

# Marcelo de Oliveira da Silva

import antlr4
import os
import sys
from ANTLR.t3_cc2Lexer import *
from GeradorDeCodigo import *
from ErrosSintaticosErrorListener import ErrosSintaticosErrorListener
from AnalisadorSemantico import AnalisadorSemantico

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
    # Conversão do arquivo de entrada para um input stream do ANTLR
    programa_input = antlr4.InputStream(programa)

    # Análise léxica
    lexer = t3_cc2Lexer(input=programa_input)
    # Remoção do ErrorListener do léxico, pois os erros serão tratados no ErrorListener customizado do sintático
    lexer.removeErrorListeners()
    tokens = antlr4.CommonTokenStream(lexer=lexer)

    parser = t3_cc2Parser(tokens)

    # Remoção do ErrorListerner do parser e adição do ErrorListener customizado
    parser.removeErrorListeners()
    erros_sintaticos = ErrosSintaticosErrorListener()
    parser.addErrorListener(erros_sintaticos)

    # Início da compilação
    programa = parser.site()

    if TESTE == SEMANTICO:
        analisador_semantico = AnalisadorSemantico()
        analisador_semantico.visitSite(programa)
        print("Compilação finalizada" + (' com warnings. ' if analisador_semantico.get_warnings() != '' else ''))
        print(analisador_semantico.get_warnings())

    elif TESTE == GERACAO_DE_CODIGO:
        gerador_de_codigo = GeradorDeCodigo()
        gerador_de_codigo.visitSite(programa)

        codigo_gerado = gerador_de_codigo.getCodigo()

        arquivo_saida = open(DIRETORIO_PROJETO + CAMINHO_ARQUIVOS_SAIDA + 'teste01.html', 'w', encoding='utf-8')
        arquivo_saida.write(codigo_gerado)
        arquivo_saida.close()

        print('\n' + codigo_gerado)
        print("Compilação OK")



except Exception as e:
    print(e, file=sys.stderr)
    # print(e.with_traceback())
