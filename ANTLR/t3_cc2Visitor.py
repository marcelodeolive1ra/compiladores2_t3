# Generated from /Users/marcelodeoliveiradasilva/PycharmProjects/T3_CC2_PyCharm/t3_cc2.g4 by ANTLR 4.6
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


    # Visit a parse tree produced by t3_cc2Parser#nova_aba.
    def visitNova_aba(self, ctx:t3_cc2Parser.Nova_abaContext):
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


    # Visit a parse tree produced by t3_cc2Parser#colunas.
    def visitColunas(self, ctx:t3_cc2Parser.ColunasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#coluna.
    def visitColuna(self, ctx:t3_cc2Parser.ColunaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#mais_colunas.
    def visitMais_colunas(self, ctx:t3_cc2Parser.Mais_colunasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#texto.
    def visitTexto(self, ctx:t3_cc2Parser.TextoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#conteudo_texto.
    def visitConteudo_texto(self, ctx:t3_cc2Parser.Conteudo_textoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#mais_conteudo_texto.
    def visitMais_conteudo_texto(self, ctx:t3_cc2Parser.Mais_conteudo_textoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#paragrafo.
    def visitParagrafo(self, ctx:t3_cc2Parser.ParagrafoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#imagem.
    def visitImagem(self, ctx:t3_cc2Parser.ImagemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#parametros.
    def visitParametros(self, ctx:t3_cc2Parser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#mais_parametros.
    def visitMais_parametros(self, ctx:t3_cc2Parser.Mais_parametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#tamanho.
    def visitTamanho(self, ctx:t3_cc2Parser.TamanhoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#opcao_tamanho.
    def visitOpcao_tamanho(self, ctx:t3_cc2Parser.Opcao_tamanhoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#fonte.
    def visitFonte(self, ctx:t3_cc2Parser.FonteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#opcao_fonte.
    def visitOpcao_fonte(self, ctx:t3_cc2Parser.Opcao_fonteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#cor.
    def visitCor(self, ctx:t3_cc2Parser.CorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#opcao_cor.
    def visitOpcao_cor(self, ctx:t3_cc2Parser.Opcao_corContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#fundo.
    def visitFundo(self, ctx:t3_cc2Parser.FundoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#alinhamento.
    def visitAlinhamento(self, ctx:t3_cc2Parser.AlinhamentoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by t3_cc2Parser#opcao_alinhamento.
    def visitOpcao_alinhamento(self, ctx:t3_cc2Parser.Opcao_alinhamentoContext):
        return self.visitChildren(ctx)



del t3_cc2Parser