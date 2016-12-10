import antlr4
from ANTLR.t3_cc2Lexer import *
from ANTLR.t3_cc2Parser import *
from ANTLR.t3_cc2Visitor import *
from Interpretador import *

programa_exemplo = """
// Comentário

site("Título da Página") {
    menu {
        item("Home") -> "http://google.com.br"
        item("Página 2") -> "Link2"
        item("Página 3") -> "Link3"
    }
    sidebar {
        item("Home") -> "Link1"
        item("Página 2") -> "Link2"
        item("Página 3") -> "Link3"
    }
    banner {
        imagem("link para a imagem") -> "link opcional da imagem"
        titulo("Título")
        subtitulo("Subtítulo")
    }
    conteudo {
        duas_colunas {
            coluna {
                titulo("Título")
                subtitulo("Subtítulo")
                texto("Texto")
            }
            coluna {
                imagem("link para a imagem") -> "link oprcional da imagem"
            }
        }
        duas_colunas {
            coluna {
                titulo("Título")
                subtitulo("Subtitulo")
            }
            coluna {
                titulo("Título")
                subtitulo("Subtítulo")
            }
        }
        linha {
            titulo("Título")
            subtitulo("Subtitulo")
        }
    }
    rodape {
        titulo("Copyright 2016")
        subtitulo("Construção de Compiladores 2")
    }
}
"""

input = antlr4.InputStream(programa_exemplo)

lexer = t3_cc2Lexer(input=input)
tokens = antlr4.CommonTokenStream(lexer=lexer)
parser = t3_cc2Parser(tokens)

programa = parser.site()

print(programa.getText())

interpretador = Intepretador()

interpretador.visitSite(programa)

print(parser.literalNames)

print(interpretador.getCodigo())
