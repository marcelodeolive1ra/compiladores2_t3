from antlr4.error.ErrorListener import ErrorListener

class ErrosSintaticosErrorListener(ErrorListener):

    erros_sintaticos = ""

    def getErrosSintaticos(self):
        return self.erros_sintaticos

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        simbolo = msg.replace("token recognition error at: ", "")
        self.erros_sintaticos += "Linha " + str(line) + ": erro sintático próximo a " + simbolo

        raise Exception("Erro sintático")

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        return

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        return

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        return
