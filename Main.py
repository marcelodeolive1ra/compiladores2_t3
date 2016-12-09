import antlr4
from ANTLR.t3_cc2Lexer import *
from ANTLR.t3_cc2Parser import *
from ANTLR.t3_cc2Visitor import *
from Interpretador import *

programa_exemplo = """
site { "Linguagem para desenvolvimento de sites" } {
    menu {
        "Home" link:"http://google.com.br"
        "Página 2"
        "Página 3"
    }
    sidebar {
        "Home"
        "Página 2"
        "Página 3"
    }
    banner {
        imagem { "Link da imagem" }
        titulo { "Título"}
        subtitulo { "Subtítulo" }
    }
}
"""

input = antlr4.InputStream(programa_exemplo)

lexer = t3_cc2Lexer(input=input)
tokens = antlr4.CommonTokenStream(lexer=lexer)
parser = t3_cc2Parser(tokens)

programa = parser.site()

interpretador = Intepretador()

interpretador.visitSite(programa)

print(parser.literalNames)

print(interpretador.getCodigo())
