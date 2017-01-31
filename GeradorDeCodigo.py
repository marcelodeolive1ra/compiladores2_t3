from ANTLR.t3_cc2Visitor import *
from ANTLR.t3_cc2Parser import *


class GeradorDeCodigo(t3_cc2Visitor):
    codigo = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8" />
            <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">

            <title>#TITULODOSITE</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/semantic-ui/2.2.6/semantic.min.css">
            <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
            <script src="https://cdn.jsdelivr.net/semantic-ui/2.2.6/semantic.min.js"></script>
            #SCRIPT_SIDEBAR
        </head>
        <body>
            #PUSHER_INICIO
            #MENU
            #SIDEBAR
            #BANNER
            #CONTEUDO
            #RODAPE
            #PUSHER_FIM
        </body>
        </html>
    """

    def visitSite(self, ctx: t3_cc2Parser.SiteContext):
        self.codigo = self.codigo.replace("#TITULODOSITE", self.visitTitulo_site(ctx.titulo_site()))
        self.visitMenu(ctx.menu())
        self.visitSidebar(ctx.sidebar())
        self.visitBanner(ctx.banner())
        self.visitConteudo(ctx.conteudo())
        self.visitRodape(ctx.rodape())
        self.codigo += """
        </div>
        </body>
        </html>
        """

    def visitTitulo_site(self, ctx: t3_cc2Parser.Titulo_siteContext):
        return str(ctx.CADEIA())

    def visitMenu(self, ctx: t3_cc2Parser.MenuContext):
        if ctx is not None:
            menu = """
            <!-- Menu principal -->
            <div class="ui large top fixed menu">
                <div class="ui container">
                    #BOTAO_SIDEBAR
                    #ITEM
                </div>
            </div>
            """

            self.codigo = self.codigo.replace("#MENU", menu)
            self.visitItem(ctx.item())
            self.visitMais_itens(ctx.mais_itens())
            self.codigo = self.codigo.replace("#ITEM", "")

    def visitSidebar(self, ctx: t3_cc2Parser.SidebarContext):
        if ctx is not None:
            sidebar = """
            <!-- Sidebar -->
            <div class="ui vertical inverted sidebar menu">
                #ITEM
            </div>
            """
            self.codigo = self.codigo.replace("#SIDEBAR", sidebar)
            self.visitItem(ctx.item())
            self.visitMais_itens(ctx.mais_itens())
            self.codigo = self.codigo.replace("#ITEM", "")

            script_sidebar = """
            <script>
                $(document)
                    .ready(function() {
                        $('.ui.sidebar')
                            .sidebar('attach events', '.toc.item')
                        ;
                    })
                ;
            </script>
            """

            self.codigo = self.codigo.replace("#SCRIPT_SIDEBAR", script_sidebar)
            self.codigo = self.codigo.replace("#PUSHER_INICIO", '<div class="pusher">')
            self.codigo = self.codigo.replace("#PUSHER_FIM", '</div>')

            botao_sidebar = """
            <a class="toc item">
                <i class="sidebar icon"></i>
            </a>
            """

            self.codigo = self.codigo.replace("#BOTAO_SIDEBAR", botao_sidebar)
        else:
            # tratar caso SIDEBAR = MENU
            self.codigo = self.codigo.replace("PUSHER_INICIO", "")
            self.codigo = self.codigo.replace("PUSHER_FIM", "")
            self.codigo = self.codigo.replace("BOTAO_SIDEBAR", "")

    def visitItem(self, ctx: t3_cc2Parser.ItemContext):
        if ctx is not None:
            item = '<a class="item" href=#LINK#TARGET>#CADEIA</a>\n'

            item = item.replace("#CADEIA", str(ctx.CADEIA()))
            item = item.replace('#LINK', self.visitLink(ctx.link()))
            item = item.replace("#TARGET", self.visitNova_aba(ctx.link().nova_aba()))

            self.codigo = self.codigo.replace("#ITEM", item + "#ITEM")

    def visitMais_itens(self, ctx: t3_cc2Parser.Mais_itensContext):
        for item in ctx.item():
            self.visitItem(item)

    def visitLink(self, ctx: t3_cc2Parser.LinkContext):
        return str(ctx.CADEIA()) if ctx is not None and ctx.CADEIA() is not None else ""

    def visitNova_aba(self, ctx: t3_cc2Parser.Nova_abaContext):
        return ' target="_blank"' if ctx is not None else ""

    def visitBanner(self, ctx: t3_cc2Parser.BannerContext):
        self.codigo = self.codigo.replace("#BANNER", """


    <style>
        .masthead.segment {
            min-height: 700px;
            padding: 1em 0em;
        }
        .masthead .logo.item img {
            margin-right: 1em;
        }
        .masthead .ui.menu .ui.button {
            margin-left: 0.5em;
        }
        .masthead h1.ui.header {
            margin-top: 3em;
            margin-bottom: 0em;
            font-size: 4em;
            font-weight: normal;
        }
        .masthead h2 {
            font-size: 1.7em;
            font-weight: normal;
        }

        .ui.vertical.stripe {
            padding: 8em 0em;
        }
        .ui.vertical.stripe h3 {
            font-size: 2em;
        }
        .ui.vertical.stripe .button + h3,
        .ui.vertical.stripe p + h3 {
            margin-top: 3em;
        }
        .ui.vertical.stripe .floated.image {
            clear: both;
        }
        .ui.vertical.stripe p {
            font-size: 1.33em;
        }
        .ui.vertical.stripe .horizontal.divider {
            margin: 3em 0em;
        }
        </style>
        <div class="ui inverted vertical masthead center aligned segment">


        <div class="ui text container">
            #IMAGEM
            #TEXTO
        </div>

      </div>
    </div>


        """)

        self.codigo = self.codigo.replace('#IMAGEM', self.visitImagem(ctx.imagem()))
        self.codigo = self.codigo.replace("#TEXTO", self.visitTexto(ctx.texto()).replace("header", "inverted header"))

    def visitConteudo(self, ctx: t3_cc2Parser.ConteudoContext):
        if ctx is not None:
            self.visitSecao(ctx.secao())

            if ctx.mais_secoes() is not None:
                self.visitMais_secoes(ctx.mais_secoes())

    def visitSecao(self, ctx: t3_cc2Parser.SecaoContext):
        try:
            if ctx.colunas() is not None:
                self.visitColunas(ctx.colunas())
        except:
            pass

    def visitMais_secoes(self, ctx: t3_cc2Parser.Mais_secoesContext):
        self.visitSecao(ctx.secao())

    def visitColunas(self, ctx: t3_cc2Parser.ColunasContext):
        if ctx is not None:
            self.visitColuna(ctx.coluna())

            if ctx.mais_colunas() is not None:
                self.visitMais_colunas(ctx.mais_colunas())

    def visitMais_colunas(self, ctx: t3_cc2Parser.Mais_colunasContext):
        self.visitColuna(ctx.coluna())

    def visitColuna(self, ctx: t3_cc2Parser.ColunaContext):
        try:
            if ctx.imagem() is not None:
                self.codigo += "COLUNA (" + self.visitImagem(ctx.imagem()) + ")\n"

                self.codigo += """
                <div class="ui sixteen wide column">
                    #TEXTO_ESCOPO_COLUNA
                    #IMAGEM_ESCOPO_COLUNA
                </div>
                """

                self.codigo = self.codigo.replace('#TEXTO_ESCOPO_COLUNA', self.visitTexto(ctx.texto()))
                self.codigo = self.codigo.replace('#IMAGEM_ESCOPO_COLUNA', self.visitImagem(ctx.imagem()))
        except:
            pass

        try:
            if ctx.texto() is not None:
                # self.codigo += "COLUNA ("
                # self.visitTexto(ctx.texto())
                # self.codigo += ")\n"

                self.codigo = self.codigo.replace('#TEXTO_ESCOPO_COLUNA', self.visitTexto(ctx.texto()))
        except:
            pass

    def visitTitulo(self, ctx: t3_cc2Parser.TituloContext):
        if ctx.parametro() is not None:
            self.codigo += "parametros("
            self.visitParametro(ctx.parametro())
            self.codigo += ")"
        return '<h1 class="ui header">' + (
        str(ctx.CADEIA()) if ctx is not None and str(ctx.CADEIA()) is not None else "") + '</h1>'

    def visitSubtitulo(self, ctx: t3_cc2Parser.SubtituloContext):
        if ctx.parametro() is not None:
            self.codigo += "parametros("
            self.visitParametro(ctx.parametro())
            self.codigo += ")"
        return '<h2 class="ui header">' + (
        str(ctx.CADEIA()) if ctx is not None and str(ctx.CADEIA()) is not None else "") + '</h2>'

    def visitTexto(self, ctx: t3_cc2Parser.TextoContext):
        try:
            if ctx.parametro() is not None:
                self.codigo += "parametros("
                self.visitParametro(ctx.parametro())
                self.codigo += ")"
        except:
            pass

        conteudo_texto = self.visitConteudo_texto(ctx.conteudo_texto()) if ctx.conteudo_texto() is not None else ""
        mais_conteudo_texto = self.visitMais_conteudo_texto(ctx.mais_conteudo_texto()) if ctx.mais_conteudo_texto() is not None else ""

        return conteudo_texto + mais_conteudo_texto

    def visitConteudo_texto(self, ctx: t3_cc2Parser.Conteudo_textoContext):
        return (self.visitTitulo(ctx.titulo()) if ctx.titulo() is not None else "")\
               + (self.visitSubtitulo(ctx.subtitulo()) if ctx.subtitulo() is not None else "")\
               + (self.visitParagrafo(ctx.paragrafo()) if ctx.paragrafo() is not None else "")

    def visitMais_conteudo_texto(self, ctx: t3_cc2Parser.Mais_conteudo_textoContext):
        return self.visitConteudo_texto(ctx.conteudo_texto()) if ctx.conteudo_texto() is not None else ""

    def visitParagrafo(self, ctx: t3_cc2Parser.ParagrafoContext):
        if ctx.parametro() is not None:
            self.codigo += "parametros("
            self.visitParametro(ctx.parametro())
            self.codigo += ")"

        return '<p>' + (str(ctx.CADEIA()) if ctx is not None and ctx.CADEIA() is not None else "") + '</p>'

    def visitImagem(self, ctx: t3_cc2Parser.ImagemContext):
        return ('<img src="' + str(ctx.CADEIA()).replace('"', '') + '">') if ctx is not None and ctx.CADEIA() is not None else ""

    def visitRodape(self, ctx: t3_cc2Parser.RodapeContext):
        self.codigo += "RODAPE ("
        self.visitTexto(ctx.texto())
        self.codigo += ")"

        self.codigo += """
<div class="ui inverted vertical footer segment">
    <div class="ui container">
      <div class="ui stackable inverted divided equal height stackable grid">
        #RODAPE
    </div>
  </div>

        """

        self.codigo = self.codigo.replace('#RODAPE', self.visitTexto(ctx.texto()))

    def visitParametro(self, ctx: t3_cc2Parser.ParametroContext):
        if ctx is not None:
            if ctx.getText().startswith("fonte"):
                self.codigo += "fonte = " + self.visitFonte(ctx.fonte())
            elif ctx.getText().startswith("tamanho"):
                self.codigo += "tamanho = " + self.visitTamanho(ctx.tamanho())
            elif ctx.getText().startswith("cor"):
                self.codigo += "cor = " + self.visitCor(ctx.cor())

        if ctx.mais_parametros() is not None:
            self.codigo += ", "
            self.visitMais_parametros(ctx.mais_parametros())

    def visitMais_parametros(self, ctx: t3_cc2Parser.Mais_parametrosContext):
        self.visitParametro(ctx.parametro())

    def visitFonte(self, ctx: t3_cc2Parser.FonteContext):
        return self.visitOpcao_fonte(ctx.opcao_fonte())

    def visitOpcao_fonte(self, ctx: t3_cc2Parser.Opcao_fonteContext):
        return ctx.getText()

    def visitCor(self, ctx: t3_cc2Parser.CorContext):
        return self.visitOpcao_cor(ctx.opcao_cor())

    def visitOpcao_cor(self, ctx: t3_cc2Parser.Opcao_corContext):
        return ctx.getText()

    def visitTamanho(self, ctx: t3_cc2Parser.TamanhoContext):
        return self.visitOpcao_tamanho(ctx.opcao_tamanho())

    def visitOpcao_tamanho(self, ctx: t3_cc2Parser.Opcao_tamanhoContext):
        return ctx.getText()

    def getCodigo(self):
        return self.codigo
