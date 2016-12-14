from ANTLR.t3_cc2Visitor import *
from ANTLR.t3_cc2Parser import *

class Intepretador(t3_cc2Visitor):

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
            item = item.replace("#LINK", self.visitLink(ctx.link()))
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
        self.codigo += "BANNER ("
        self.codigo += "Imagem de fundo: " + self.visitImagem(ctx.imagem()) + ", "
        self.codigo += "TEXTO ("
        self.visitTexto(ctx.texto())
        self.codigo += "))\n"

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
        except:
            pass

        try:
            if ctx.texto() is not None:
                self.codigo += "COLUNA ("
                self.visitTexto(ctx.texto())
                self.codigo += ")\n"
        except:
            pass

    def visitTitulo(self, ctx: t3_cc2Parser.TituloContext):
        return str(ctx.CADEIA()) if ctx is not None and ctx.CADEIA() is not None else ""

    def visitSubtitulo(self, ctx: t3_cc2Parser.SubtituloContext):
        return str(ctx.CADEIA()) if ctx is not None and ctx.CADEIA() is not None else ""

    def visitTexto(self, ctx: t3_cc2Parser.TextoContext):
        try:
            if ctx.conteudo_texto() is not None:
                self.visitConteudo_texto(ctx.conteudo_texto())
        except:
            pass

    def visitConteudo_texto(self, ctx: t3_cc2Parser.Conteudo_textoContext):
        if ctx.paragrafo() is not None:
            self.codigo += "PARAGRAFO (" + self.visitParagrafo(ctx.paragrafo()) + "), "
        elif ctx.titulo() is not None:
            self.codigo += "TITULO (" + self.visitTitulo(ctx.titulo()) + "), "
        elif ctx.subtitulo() is not None:
            self.codigo += "SUBTITULO (" + self.visitSubtitulo(ctx.subtitulo()) + "), "

        if ctx.mais_conteudo_texto() is not None:
            self.visitMais_conteudo_texto(ctx.mais_conteudo_texto())

    def visitParagrafo(self, ctx: t3_cc2Parser.ParagrafoContext):
        return str(ctx.CADEIA()) if ctx is not None and ctx.CADEIA() is not None else ""

    def visitImagem(self, ctx: t3_cc2Parser.ImagemContext):
        return str(ctx.CADEIA()) if ctx is not None and ctx.CADEIA() is not None else ""

    def visitRodape(self, ctx: t3_cc2Parser.RodapeContext):
        self.codigo += "RODAPE ("
        self.visitTexto(ctx.texto())
        self.codigo += ")"

    def getCodigo(self):
        return self.codigo
