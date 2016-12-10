# Generated from /Users/marcelodeoliveiradasilva/PycharmProjects/T3_CC2_PyCharm/t3_cc2.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .t3_cc2Parser import t3_cc2Parser
else:
    from t3_cc2Parser import t3_cc2Parser

# This class defines a complete generic visitor for a parse tree produced by t3_cc2Parser.

class t3_cc2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by t3_cc2Parser#site.
    def visitSite(self, ctx:t3_cc2Parser.SiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#titulo_site.
    def visitTitulo_site(self, ctx:t3_cc2Parser.Titulo_siteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#titulo.
    def visitTitulo(self, ctx:t3_cc2Parser.TituloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#menu.
    def visitMenu(self, ctx:t3_cc2Parser.MenuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#item.
    def visitItem(self, ctx:t3_cc2Parser.ItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#link.
    def visitLink(self, ctx:t3_cc2Parser.LinkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#mais_itens.
    def visitMais_itens(self, ctx:t3_cc2Parser.Mais_itensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#sidebar.
    def visitSidebar(self, ctx:t3_cc2Parser.SidebarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#banner.
    def visitBanner(self, ctx:t3_cc2Parser.BannerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#subtitulo.
    def visitSubtitulo(self, ctx:t3_cc2Parser.SubtituloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#rodape.
    def visitRodape(self, ctx:t3_cc2Parser.RodapeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#conteudo.
    def visitConteudo(self, ctx:t3_cc2Parser.ConteudoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#secao.
    def visitSecao(self, ctx:t3_cc2Parser.SecaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#mais_secoes.
    def visitMais_secoes(self, ctx:t3_cc2Parser.Mais_secoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#uma_coluna.
    def visitUma_coluna(self, ctx:t3_cc2Parser.Uma_colunaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#duas_colunas.
    def visitDuas_colunas(self, ctx:t3_cc2Parser.Duas_colunasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#tres_colunas.
    def visitTres_colunas(self, ctx:t3_cc2Parser.Tres_colunasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#coluna.
    def visitColuna(self, ctx:t3_cc2Parser.ColunaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#linha.
    def visitLinha(self, ctx:t3_cc2Parser.LinhaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#texto.
    def visitTexto(self, ctx:t3_cc2Parser.TextoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#imagem.
    def visitImagem(self, ctx:t3_cc2Parser.ImagemContext):
        return self.visitChildren(ctx)



del t3_cc2Parser