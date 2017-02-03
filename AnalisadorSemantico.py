from ANTLR.t3_cc2Visitor import *
from ANTLR.t3_cc2Parser import *


class AnalisadorSemantico(t3_cc2Visitor):
    erros_semanticos = ''

    def getErrosSemanticos(self):
        return self.erros_semanticos

    def getLinhaDoErro(self, dados_do_erro):
        return 'Erro semântico na linha ' + str(dados_do_erro).split(',')[3].split(':')[0] + ': '

    def getRegraDoErro(self, dados_do_erro):
        return ' no comando ' + str(dados_do_erro).split(',')[1].split('=')[1] + '.'

    def visitSite(self, ctx: t3_cc2Parser.SiteContext):
        titulo_site = 0
        fonte = 0

        if ctx.parametros() is not None:
            if ctx.parametros().cor() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "cor"' + \
                                         self.getRegraDoErro(ctx.start)
                return
            if ctx.parametros().alinhamento() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "alinhamento"' + \
                                         self.getRegraDoErro(ctx.start)
                return
            if ctx.parametros().tamanho() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "tamanho"' + \
                                         self.getRegraDoErro(ctx.start)
                return
            if ctx.parametros().fundo() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "fundo"' + \
                                         self.getRegraDoErro(ctx.start)
                return
            if ctx.parametros().titulo_site() is not None:
                titulo_site += 1
            if ctx.parametros().fonte() is not None:
                fonte += 1

            if ctx.parametros().mais_parametros() is not None:
                if ctx.parametros().mais_parametros().parametros().cor() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "cor"' + \
                                             self.getRegraDoErro(self.getRegraDoErro(ctx.start)) + '.'
                    return
                if ctx.parametros().mais_parametros().parametros().alinhamento() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "alinhamento"' + \
                                             self.getRegraDoErro(ctx.start)
                    return
                if ctx.parametros().mais_parametros().parametros().tamanho() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "tamanho"' + \
                                             self.getRegraDoErro(ctx.start)
                    return
                if ctx.parametros().mais_parametros().parametros().fundo() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "fundo"' + \
                                             self.getRegraDoErro(ctx.start)
                    return
                if ctx.parametros().mais_parametros().parametros().titulo_site() is not None:
                    titulo_site += 1
                if ctx.parametros().mais_parametros().parametros().fonte() is not None:
                    fonte += 1

        if fonte > 1:
            self.erros_semanticos += self.getLinhaDoErro(ctx.start) + 'parâmetro "fonte" repetido.'

        if titulo_site > 1:
            self.erros_semanticos += self.getLinhaDoErro(ctx.start) + 'parâmetro "titulo" repetido.'

        if self.erros_semanticos != '':
            raise Exception(self.erros_semanticos)

        return

    def visitTitulo_site(self, ctx: t3_cc2Parser.Titulo_siteContext):
        return

    def visitMenu(self, ctx: t3_cc2Parser.MenuContext):
        return

    def visitSidebar(self, ctx: t3_cc2Parser.SidebarContext):
        return

    def visitItem(self, ctx: t3_cc2Parser.ItemContext):
        return

    def visitMais_itens(self, ctx: t3_cc2Parser.Mais_itensContext):
        return

    def visitLink(self, ctx: t3_cc2Parser.LinkContext):
        return

    def visitNova_aba(self, ctx: t3_cc2Parser.Nova_abaContext):
        return

    def visitBanner(self, ctx: t3_cc2Parser.BannerContext):
        return

    def visitConteudo(self, ctx: t3_cc2Parser.ConteudoContext):
        return

    def visitSecao(self, ctx: t3_cc2Parser.SecaoContext):
        return

    def visitMais_secoes(self, ctx: t3_cc2Parser.Mais_secoesContext):
        return

    def visitColunas(self, ctx: t3_cc2Parser.ColunasContext):
        return

    def visitMais_colunas(self, ctx: t3_cc2Parser.Mais_colunasContext):
        return

    def visitColuna(self, ctx: t3_cc2Parser.ColunaContext):
        return

    def visitTitulo(self, ctx: t3_cc2Parser.TituloContext):
        return

    def visitSubtitulo(self, ctx: t3_cc2Parser.SubtituloContext):
        return

    def visitTexto(self, ctx: t3_cc2Parser.TextoContext):
        return

    def visitConteudo_texto(self, ctx: t3_cc2Parser.Conteudo_textoContext):
        return

    def visitMais_conteudo_texto(self, ctx: t3_cc2Parser.Mais_conteudo_textoContext):
        return

    def visitParagrafo(self, ctx: t3_cc2Parser.ParagrafoContext):
        return

    def visitImagem(self, ctx: t3_cc2Parser.ImagemContext):
        return

    def visitRodape(self, ctx: t3_cc2Parser.RodapeContext):
        return

    def visitFonte(self, ctx: t3_cc2Parser.FonteContext):
        return

    def visitOpcao_fonte(self, ctx: t3_cc2Parser.Opcao_fonteContext):
        return

    def visitCor(self, ctx: t3_cc2Parser.CorContext):
        return

    def visitOpcao_cor(self, ctx: t3_cc2Parser.Opcao_corContext):
        return

    def visitTamanho(self, ctx: t3_cc2Parser.TamanhoContext):
        return

    def visitOpcao_tamanho(self, ctx: t3_cc2Parser.Opcao_tamanhoContext):
        return

    def visitAlinhamento(self, ctx: t3_cc2Parser.AlinhamentoContext):
        return

    def visitOpcao_alinhamento(self, ctx: t3_cc2Parser.Opcao_alinhamentoContext):
        return
