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
            self.codigo += str(ctx.CADEIA()) + ", "

            if ctx.mais_itens() is not None:
                self.visitMais_itens(ctx.mais_itens())

    def visitMais_itens(self, ctx: t3_cc2Parser.Mais_itensContext):
        self.visitItem(ctx.item())

    def visitBanner(self, ctx: t3_cc2Parser.BannerContext):
        self.codigo += "BANNER (Título: " + self.visitTitulo(ctx.titulo()) + ", "
        self.codigo += "Subtítulo: " + self.visitSubtitulo(ctx.subtitulo()) + ", "
        self.codigo += "Imagem de fundo: " + self.visitImagem(ctx.imagem()) + ")\n"


    def visitConteudo(self, ctx: t3_cc2Parser.ConteudoContext):
        if ctx is not None:
            self.visitSecao(ctx.secao())

            if ctx.mais_secoes() is not None:
                self.visitMais_secoes(ctx.mais_secoes())


    def visitSecao(self, ctx: t3_cc2Parser.SecaoContext):
        self.visitColunas(ctx.colunas())

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
        if ctx.imagem() is not None:
            self.codigo += "COLUNA (" + self.visitImagem(ctx.imagem()) + ")\n"
        else:
            self.codigo += "COLUNA (" + self.visitTitulo(ctx.titulo()) + " " + self.visitSubtitulo(ctx.subtitulo()) + \
                           " " + self.visitTexto(ctx.texto()) + ")\n"

    def visitTitulo(self, ctx: t3_cc2Parser.TituloContext):
        return str(ctx.CADEIA()) if ctx is not None and ctx.CADEIA() is not None else ""

    def visitSubtitulo(self, ctx: t3_cc2Parser.SubtituloContext):
        return str(ctx.CADEIA()) if ctx is not None and ctx.CADEIA() is not None else ""

    def visitTexto(self, ctx: t3_cc2Parser.TextoContext):
        return str(ctx.CADEIA()) if ctx is not None and ctx.CADEIA() is not None else ""

    def visitImagem(self, ctx: t3_cc2Parser.ImagemContext):
        return str(ctx.CADEIA()) if ctx is not None and ctx.CADEIA() is not None else ""

    def visitRodape(self, ctx: t3_cc2Parser.RodapeContext):
        self.codigo += "RODAPE (Titulo: " + self.visitTitulo(ctx.titulo()) + ", "
        self.codigo += "Subtítulo: " + self.visitSubtitulo(ctx.subtitulo()) + ")"

    def getCodigo(self):
        return self.codigo
