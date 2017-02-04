# UNIVERSIDADE FEDERAL DE SÃO CARLOS
# Construção de Compiladores 2 - 2016/2
# Trabalho 3

# Marcelo de Oliveira da Silva

from antlr4.error.ErrorListener import ErrorListener


class ErrosSintaticosErrorListener(ErrorListener):

    # Tradução das mensagens de erro do analisador sintático e lançamento de exceção interrompendo a compilação
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception('Linha ' + str(line) + ': erro sintático próximo a \'' + offendingSymbol.text + '\'.')

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        return

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        return

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        return