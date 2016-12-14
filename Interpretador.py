from ANTLR.t3_cc2Visitor import *
from ANTLR.t3_cc2Parser import *

class Intepretador(t3_cc2Visitor):

    codigo = ""

    def visitSite(self, ctx: t3_cc2Parser.SiteContext):
        self.codigo += "SITE (" + self.visitTitulo_site(ctx.titulo_site()) + ")\n"
        self.visitBanner(ctx.banner())
        self.visitMenu(ctx.menu())
        self.visitSidebar(ctx.sidebar())
        self.visitConteudo(ctx.conteudo())
        self.visitRodape(ctx.rodape())

    def visitTitulo_site(self, ctx: t3_cc2Parser.Titulo_siteContext):
        return str(ctx.CADEIA())

    def visitMenu(self, ctx: t3_cc2Parser.MenuContext):
        self.codigo += "MENU ("
        self.visitItem(ctx.item())
        self.codigo += ")"

    def visitSidebar(self, ctx: t3_cc2Parser.SidebarContext):
        if ctx.item() is not None:
            self.codigo += "\nSIDEBAR ("
            self.visitItem(ctx.item())
            self.codigo += ")\n"
        else:
            self.codigo += "\nSIDEBAR = MENU"

    def visitItem(self, ctx: t3_cc2Parser.ItemContext):
        if ctx is not None:
            self.codigo += str(ctx.CADEIA()) + "->" + self.visitLink(ctx.link()) + ", "

            if ctx.mais_itens() is not None:
                self.visitMais_itens(ctx.mais_itens())

    def visitMais_itens(self, ctx: t3_cc2Parser.Mais_itensContext):
        self.visitItem(ctx.item())

    def visitLink(self, ctx: t3_cc2Parser.LinkContext):

        nova_aba = " -> nova_aba" if ctx.nova_aba() is not None else ""

        return str(ctx.CADEIA()) + nova_aba if ctx is not None and ctx.CADEIA() is not None else ""

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
