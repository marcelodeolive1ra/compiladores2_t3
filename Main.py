import antlr4
from ANTLR.t3_cc2Lexer import *
from ANTLR.t3_cc2Parser import *
from ANTLR.t3_cc2Visitor import *
from GeradorDeCodigo import *
from ErrosSintaticosErrorListener import ErrosSintaticosErrorListener

programa_exemplo = """
// Comentário

site("Título da Página") {
    menu {
        item("Home") -> "http://google.com.br"
        item("Página 2") -> "Link2"
        item("Página 3") -> "Link3"
    }
    //sidebar = menu
    sidebar {
        item("Home") -> "Link1"
        item("Página 2") ->+ "Link2 para abrir em nova aba"
        item("Página 3") -> "Link3"
    }
    banner {
        imagem("link para a imagem") -> "link opcional da imagem"
        texto (cor=azul) {
            titulo("Título")
            subtitulo("Subtítulo")
        }
    }
    conteudo {
        secao {
            colunas {
                coluna {
                    texto {
                        titulo("Título")
                        subtitulo("Subtítulo")
                        paragrafo("Texto")
                    }
                }
                coluna {
                    imagem("link para a imagem") -> "link opcional da imagem"
                }
            }
        }
        secao {
            colunas {
                coluna {
                    texto {
                        titulo("Título")
                        subtitulo("Subtitulo")
                    }
                }
                coluna {
                    texto {
                        titulo("Título")
                        subtitulo("Subtítulo")
                    }
                }
            }
        }
    }
    rodape {
        texto {
            titulo("Copyright 2016")
            subtitulo("Construção de Compiladores 2")
        }
    }
}
"""

input = antlr4.InputStream(programa_exemplo)

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

    print('\n' + gerador_de_codigo.getCodigo())

except:
    if erros_sintaticos.getErrosSintaticos() != "":
        print(erros_sintaticos.getErrosSintaticos())
    else:
        print("Erros semânticos")
