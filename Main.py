# UNIVERSIDADE FEDERAL DE SÃO CARLOS
# Construção de Compiladores 2 - 2016/2
# Trabalho 3

# Marcelo de Oliveira da Silva

import antlr4
import os
import sys
import argparse
from ANTLR.t3_cc2Lexer import *
from GeradorDeCodigo import *
from ErrosSintaticosErrorListener import ErrosSintaticosErrorListener
from AnalisadorSemantico import AnalisadorSemantico

DIRETORIO_PROJETO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SINTATICO = 'lexico-sintatico/'
SEMANTICO = 'semantico/'
GERACAO_DE_CODIGO = 'geracao-codigo/'

TESTE = SEMANTICO

CAMINHO_ARQUIVOS_ENTRADA = '/T3_CC2_Pycharm/casos_de_teste/entrada/'
CAMINHO_ARQUIVOS_SAIDA = '/T3_CC2_Pycharm/casos_de_teste/saida/'

EXECUCAO_CASOS_DE_TESTE = True


def casos_de_teste_sintatico():
    print('----------------------------------------------------------')
    print('CASOS DE TESTE DO ANALISADOR LÉXICO/SINTÁTICO - 44 CASOS')
    print('----------------------------------------------------------')
    for i in range(1, 45):
        with open(DIRETORIO_PROJETO + CAMINHO_ARQUIVOS_ENTRADA + SINTATICO + 'ct_sintatico_' + str(i) + '.txt',
                  encoding='utf-8') as caso_de_teste:
            programa = caso_de_teste.read()
            programa_input = antlr4.InputStream(programa)

            lexer = t3_cc2Lexer(input=programa_input)
            lexer.removeErrorListeners()
            tokens = antlr4.CommonTokenStream(lexer=lexer)

            parser = t3_cc2Parser(tokens)

            parser.removeErrorListeners()
            erros_sintaticos = ErrosSintaticosErrorListener()
            parser.addErrorListener(erros_sintaticos)
            try:
                parser.site()
                print('[CT' + str(i) + '] compilação finalizada.')
            except Exception as e:
                print('[CT' + str(i) + '_SINTATICO] ' + str(e), file=sys.stderr)
                pass


def casos_de_teste_semantico():
    print('----------------------------------------------------------')
    print('CASOS DE TESTE DO ANALISADOR SEMÂNTICO - 54 CASOS')
    print('----------------------------------------------------------')
    for i in range(1, 55):
        with open(DIRETORIO_PROJETO + CAMINHO_ARQUIVOS_ENTRADA + SEMANTICO + 'ct_semantico_' + str(i) + '.txt',
                  encoding='utf-8') as caso_de_teste:
            programa = caso_de_teste.read()
            programa_input = antlr4.InputStream(programa)

            lexer = t3_cc2Lexer(input=programa_input)
            lexer.removeErrorListeners()
            tokens = antlr4.CommonTokenStream(lexer=lexer)

            parser = t3_cc2Parser(tokens)

            parser.removeErrorListeners()
            erros_sintaticos = ErrosSintaticosErrorListener()
            parser.addErrorListener(erros_sintaticos)
            try:
                programa = parser.site()
                analisador_semantico = AnalisadorSemantico()
                analisador_semantico.visitSite(programa)

                warnings = analisador_semantico.get_warnings()
                print('[CT' + str(i) + '_SEMANTICO] Compilação finalizada' +
                      (' com warnings. ' if warnings != '' else '.'))
                if warnings != '':
                    print('\t' + warnings.replace('\n', '\n\t'), file=sys.stderr)
            except Exception as e:
                print('[CT' + str(i) + '_SEMANTICO] ' + str(e), file=sys.stderr)
                pass


def casos_de_teste_gerador():
    print('----------------------------------------------------------')
    print('CASOS DE TESTE DO GERADOR DE CÓDIGO - 20 CASOS')
    print('----------------------------------------------------------')
    for i in range(1, 21):
        with open(DIRETORIO_PROJETO + CAMINHO_ARQUIVOS_ENTRADA + GERACAO_DE_CODIGO + 'ct_gerador_' + str(i) + '.txt',
                  encoding='utf-8') as caso_de_teste:
            programa = caso_de_teste.read()
            programa_input = antlr4.InputStream(programa)

            lexer = t3_cc2Lexer(input=programa_input)
            lexer.removeErrorListeners()
            tokens = antlr4.CommonTokenStream(lexer=lexer)

            parser = t3_cc2Parser(tokens)

            parser.removeErrorListeners()
            erros_sintaticos = ErrosSintaticosErrorListener()
            parser.addErrorListener(erros_sintaticos)
            try:
                programa = parser.site()
                analisador_semantico = AnalisadorSemantico()
                analisador_semantico.visitSite(programa)

                warnings = analisador_semantico.get_warnings()

                if warnings != '':
                    print('\t' + warnings.replace('\n', '\n\t'), file=sys.stderr)

                gerador_de_codigo = GeradorDeCodigo()
                gerador_de_codigo.visitSite(programa)

                codigo_gerado = gerador_de_codigo.getCodigo()

                arquivo = DIRETORIO_PROJETO + CAMINHO_ARQUIVOS_SAIDA + GERACAO_DE_CODIGO + 'ct_gerador_' + \
                          str(i) + '.html'

                arquivo_saida = open(arquivo, 'w', encoding='utf-8')
                arquivo_saida.write(codigo_gerado)
                arquivo_saida.close()

                print('[CT' + str(i) + '_GERADOR] Compilação finalizada' +
                      (' com warnings. ' if warnings != '' else ' sem erros.'))
            except Exception as e:
                print('[CT' + str(i) + '_GERADOR] ' + str(e), file=sys.stderr)
                pass
    print('\nArquivos compilados com sucesso geraram arquivos .html em:')
    print(DIRETORIO_PROJETO + CAMINHO_ARQUIVOS_SAIDA + GERACAO_DE_CODIGO + '\n')


def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("-t", "--testes",
                                 help="Executar casos de teste. Opções: sintatico, semantico, gerador ou todos")
    argument_parser.add_argument("-e", "--entrada", help="caminho para o arquivo de entrada para o compilador")
    argument_parser.add_argument("-s", "--saida", help="arquivo de saida (.html)")
    args = argument_parser.parse_args()

    print('-----------------------------------------------')
    print('Compiladores 2 - T3')
    print('-----------------------------------------------')

    if not args.testes:
        if args.entrada and args.saida:
            try:
                with open(args.entrada, encoding='utf-8') as f:
                    programa = f.read()

                print('Compilando...')

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

                analisador_semantico = AnalisadorSemantico()
                analisador_semantico.visitSite(programa)

                gerador_de_codigo = GeradorDeCodigo()
                gerador_de_codigo.visitSite(programa)

                codigo_gerado = gerador_de_codigo.getCodigo()

                arquivo_saida = open(args.saida, 'w', encoding='utf-8')
                arquivo_saida.write(codigo_gerado)
                arquivo_saida.close()

                print("Compilação finalizada" +
                      (' com warnings. ' if analisador_semantico.get_warnings() != '' else '.'))

            except Exception as e:
                print(e, file=sys.stderr)
        else:
            print('-----------------------------------------------')

            if not args.entrada:
                print('Erro: arquivo de entrada não informado.', file=sys.stderr)
            if not args.saida:
                print('Erro: arquivo de saída não informado.', file=sys.stderr)

            if not args.entrada or not args.saida:
                print('\nSintaxe de uso do compilador:')
                print('./Main.py -e PATH/arquivo_de_entrada.txt -s PATH/arquivo_de_saida.html')
                print('\nSintaxe para rodar os casos de teste:')
                print('./Main.py -t [sintatico | semantico | gerador | todos]\n')

            print('-----------------------------------------------')
    else:
        if args.testes == 'sintatico':
            casos_de_teste_sintatico()
        elif args.testes == 'semantico':
            casos_de_teste_semantico()
        elif args.testes == 'gerador':
            casos_de_teste_gerador()
        elif args.testes == 'todos':
            casos_de_teste_sintatico()
            casos_de_teste_semantico()
            casos_de_teste_gerador()
        else:
            print('***PARÂMETROS INVÁLIDOS***')
            print('\nSintaxe de uso do compilador:')
            print('./Main.py -e PATH/arquivo_de_entrada.txt -s PATH/arquivo_de_saida.html')
            print('\nSintaxe para rodar os casos de teste:')
            print('./Main.py -t [sintatico | semantico | gerador | todos]\n')

if __name__ == '__main__':
    main()
