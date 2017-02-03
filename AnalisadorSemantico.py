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
                raise Exception(self.erros_semanticos)
            if ctx.parametros().alinhamento() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "alinhamento"' + \
                                         self.getRegraDoErro(ctx.start)
                raise Exception(self.erros_semanticos)
            if ctx.parametros().tamanho() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "tamanho"' + \
                                         self.getRegraDoErro(ctx.start)
                raise Exception(self.erros_semanticos)
            if ctx.parametros().fundo() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "fundo"' + \
                                         self.getRegraDoErro(ctx.start)
                raise Exception(self.erros_semanticos)
            if ctx.parametros().titulo_site() is not None:
                titulo_site += 1
            if ctx.parametros().fonte() is not None:
                fonte += 1

            if ctx.parametros().mais_parametros() is not None:
                if ctx.parametros().mais_parametros().parametros().cor() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "cor"' + \
                                             self.getRegraDoErro(self.getRegraDoErro(ctx.start)) + '.'
                    raise Exception(self.erros_semanticos)
                if ctx.parametros().mais_parametros().parametros().alinhamento() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "alinhamento"' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)
                if ctx.parametros().mais_parametros().parametros().tamanho() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "tamanho"' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)
                if ctx.parametros().mais_parametros().parametros().fundo() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "fundo"' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)
                if ctx.parametros().mais_parametros().parametros().titulo_site() is not None:
                    titulo_site += 1
                if ctx.parametros().mais_parametros().parametros().fonte() is not None:
                    fonte += 1

                if ctx.parametros().mais_parametros().parametros().mais_parametros().parametros() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido mais que dois parâmetros' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)

        if fonte > 1:
            self.erros_semanticos += self.getLinhaDoErro(ctx.start) + 'parâmetro "fonte" repetido.'

        if titulo_site > 1:
            self.erros_semanticos += self.getLinhaDoErro(ctx.start) + 'parâmetro "titulo" repetido.'

        if self.erros_semanticos != '':
            raise Exception(self.erros_semanticos)

        if ctx.sidebar() is not None:
            if ctx.sidebar().getText() == 'sidebar=menu' and ctx.menu() is None:
                raise Exception(self.getLinhaDoErro(ctx.sidebar().start) +
                                'uso do comando "sidebar=menu" sem a declaração de um componente "menu".')

        if ctx.banner() is not None:
            self.visitBanner(ctx.banner())

        self.visitConteudo(ctx.conteudo())

        if ctx.rodape() is not None:
            self.visitRodape(ctx.rodape())
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
        if ctx is not None:
            if ctx.parametros() is not None:
                if ctx.parametros().cor() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "cor"' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)
                if ctx.parametros().alinhamento() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "alinhamento"' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)
                if ctx.parametros().tamanho() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "tamanho"' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)
                if ctx.parametros().fonte() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "fonte"' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)
                if ctx.parametros().titulo_site() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "titulo"' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)
                if ctx.parametros().mais_parametros().parametros() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido declarar mais de um parâmetro' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)

                ja_tem_parametro = False
                if ctx.parametros().fundo().imagem() is not None:
                    ja_tem_parametro = True
                    if ctx.parametros().fundo().imagem().parametros() is not None:
                        self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                                 'não é permitido declarar parâmetros para uma imagem de fundo' + \
                                                 self.getRegraDoErro(ctx.start)
                        raise Exception(self.erros_semanticos)
                if ctx.parametros().fundo().cor() is not None and ja_tem_parametro:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido declarar mais de um parâmetro' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)

        self.visitTexto(ctx.texto())
        return

    def visitConteudo(self, ctx: t3_cc2Parser.ConteudoContext):
        self.visitSecao(ctx.secao())
        self.visitMais_secoes(ctx.mais_secoes())
        return

    def visitSecao(self, ctx: t3_cc2Parser.SecaoContext):
        if ctx.texto() is not None:
            self.visitTexto(ctx.texto())
            if ctx.coluna() is not None:
                self.visitColuna(ctx.coluna())
            elif ctx.colunas() is not None:
                self.visitColunas(ctx.colunas())
        else:
            if ctx.coluna() is not None:
                self.visitColuna(ctx.coluna())
            elif ctx.colunas() is not None:
                self.visitColunas(ctx.colunas())
        return

    def visitMais_secoes(self, ctx: t3_cc2Parser.Mais_secoesContext):
        if ctx.secao() is not None:
            self.visitSecao(ctx.secao())
            self.visitMais_secoes(ctx.mais_secoes())
        return

    def visitColunas(self, ctx: t3_cc2Parser.ColunasContext):
        return

    def visitMais_colunas(self, ctx: t3_cc2Parser.Mais_colunasContext):
        return

    def visitColuna(self, ctx: t3_cc2Parser.ColunaContext):
        if ctx.parametros() is not None:
            if ctx.parametros().cor() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "cor"' + \
                                         self.getRegraDoErro(ctx.start)
                raise Exception(self.erros_semanticos)
            if ctx.parametros().tamanho() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "tamanho"' + \
                                         self.getRegraDoErro(ctx.start)
                raise Exception(self.erros_semanticos)
            if ctx.parametros().fonte() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "fonte"' + \
                                         self.getRegraDoErro(ctx.start)
                raise Exception(self.erros_semanticos)
            if ctx.parametros().titulo_site() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "titulo"' + \
                                         self.getRegraDoErro(ctx.start)
                raise Exception(self.erros_semanticos)
            if ctx.parametros().mais_parametros().parametros() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido declarar mais de um parâmetro' + \
                                         self.getRegraDoErro(ctx.start)
                raise Exception(self.erros_semanticos)
        return

    def visitTitulo(self, ctx: t3_cc2Parser.TituloContext):
        alinhamento = 0
        cor = 0

        if ctx.parametros() is not None:
            if ctx.parametros().tamanho() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "tamanho"' + \
                                         self.getRegraDoErro(ctx.start)
                raise Exception(self.erros_semanticos)
            if ctx.parametros().fundo() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "fundo"' + \
                                         self.getRegraDoErro(ctx.start)
                raise Exception(self.erros_semanticos)
            if ctx.parametros().titulo_site() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "titulo"' + \
                                         self.getRegraDoErro(ctx.start)
                raise Exception(self.erros_semanticos)
            if ctx.parametros().fonte() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "fonte"' + \
                                         self.getRegraDoErro(ctx.start)
                raise Exception(self.erros_semanticos)

            if ctx.parametros().alinhamento() is not None:
                alinhamento += 1
            if ctx.parametros().cor() is not None:
                cor += 1

            if ctx.parametros().mais_parametros().parametros() is not None:
                if ctx.parametros().mais_parametros().parametros().tamanho() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "tamanho"' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)
                if ctx.parametros().mais_parametros().parametros().fundo() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "fundo"' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)
                if ctx.parametros().mais_parametros().parametros().titulo_site() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "titulo"' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)
                if ctx.parametros().mais_parametros().parametros().fonte() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "fonte"' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)

                if ctx.parametros().mais_parametros().parametros().alinhamento() is not None:
                    alinhamento += 1
                if ctx.parametros().mais_parametros().parametros().cor() is not None:
                    cor += 1

                if ctx.parametros().mais_parametros().parametros().mais_parametros().parametros() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido mais que dois parâmetros' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)

        if alinhamento > 1:
            self.erros_semanticos += self.getLinhaDoErro(ctx.start) + 'parâmetro "alinhamento" repetido.'

        if cor > 1:
            self.erros_semanticos += self.getLinhaDoErro(ctx.start) + 'parâmetro "cor" repetido.'

        if self.erros_semanticos != '':
            raise Exception(self.erros_semanticos)

        return

    def visitSubtitulo(self, ctx: t3_cc2Parser.SubtituloContext):
        alinhamento = 0
        cor = 0

        if ctx.parametros() is not None:
            if ctx.parametros().tamanho() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "tamanho"' + \
                                         self.getRegraDoErro(ctx.start)
                raise Exception(self.erros_semanticos)
            if ctx.parametros().fundo() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "fundo"' + \
                                         self.getRegraDoErro(ctx.start)
                raise Exception(self.erros_semanticos)
            if ctx.parametros().titulo_site() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "titulo"' + \
                                         self.getRegraDoErro(ctx.start)
                raise Exception(self.erros_semanticos)
            if ctx.parametros().fonte() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "fonte"' + \
                                         self.getRegraDoErro(ctx.start)
                raise Exception(self.erros_semanticos)

            if ctx.parametros().alinhamento() is not None:
                alinhamento += 1
            if ctx.parametros().cor() is not None:
                cor += 1

            if ctx.parametros().mais_parametros().parametros() is not None:
                if ctx.parametros().mais_parametros().parametros().tamanho() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "tamanho"' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)
                if ctx.parametros().mais_parametros().parametros().fundo() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "fundo"' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)
                if ctx.parametros().mais_parametros().parametros().titulo_site() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "titulo"' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)
                if ctx.parametros().mais_parametros().parametros().fonte() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "fonte"' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)

                if ctx.parametros().mais_parametros().parametros().alinhamento() is not None:
                    alinhamento += 1
                if ctx.parametros().mais_parametros().parametros().cor() is not None:
                    cor += 1

                if ctx.parametros().mais_parametros().parametros().mais_parametros().parametros() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido mais que dois parâmetros' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)

        if alinhamento > 1:
            self.erros_semanticos += self.getLinhaDoErro(ctx.start) + 'parâmetro "alinhamento" repetido.'

        if cor > 1:
            self.erros_semanticos += self.getLinhaDoErro(ctx.start) + 'parâmetro "cor" repetido.'

        if self.erros_semanticos != '':
            raise Exception(self.erros_semanticos)
        return

    def visitTexto(self, ctx: t3_cc2Parser.TextoContext):
        self.visitConteudo_texto(ctx.conteudo_texto())
        return

    def visitConteudo_texto(self, ctx: t3_cc2Parser.Conteudo_textoContext):
        if ctx.titulo() is not None:
            self.visitTitulo(ctx.titulo())
        if ctx.subtitulo() is not None:
            self.visitSubtitulo(ctx.subtitulo())
        if ctx.paragrafo() is not None:
            self.visitParagrafo(ctx.paragrafo())
        if ctx.mais_conteudo_texto() is not None:
            self.visitMais_conteudo_texto(ctx.mais_conteudo_texto())
        return

    def visitMais_conteudo_texto(self, ctx: t3_cc2Parser.Mais_conteudo_textoContext):
        if ctx.conteudo_texto() is not None:
            self.visitConteudo_texto(ctx.conteudo_texto())
        if ctx.mais_conteudo_texto() is not None:
            self.visitMais_conteudo_texto(ctx.mais_conteudo_texto())
        return

    def visitParagrafo(self, ctx: t3_cc2Parser.ParagrafoContext):
        alinhamento = 0
        cor = 0

        if ctx.parametros() is not None:
            if ctx.parametros().tamanho() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "tamanho"' + \
                                         self.getRegraDoErro(ctx.start)
                raise Exception(self.erros_semanticos)
            if ctx.parametros().fundo() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "fundo"' + \
                                         self.getRegraDoErro(ctx.start)
                raise Exception(self.erros_semanticos)
            if ctx.parametros().titulo_site() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "titulo"' + \
                                         self.getRegraDoErro(ctx.start)
                raise Exception(self.erros_semanticos)
            if ctx.parametros().fonte() is not None:
                self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                         'não é permitido o parâmetro "fonte"' + \
                                         self.getRegraDoErro(ctx.start)
                raise Exception(self.erros_semanticos)

            if ctx.parametros().alinhamento() is not None:
                alinhamento += 1
            if ctx.parametros().cor() is not None:
                cor += 1

            if ctx.parametros().mais_parametros().parametros() is not None:
                if ctx.parametros().mais_parametros().parametros().tamanho() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "tamanho"' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)
                if ctx.parametros().mais_parametros().parametros().fundo() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "fundo"' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)
                if ctx.parametros().mais_parametros().parametros().titulo_site() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "titulo"' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)
                if ctx.parametros().mais_parametros().parametros().fonte() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido o parâmetro "fonte"' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)

                if ctx.parametros().mais_parametros().parametros().alinhamento() is not None:
                    alinhamento += 1
                if ctx.parametros().mais_parametros().parametros().cor() is not None:
                    cor += 1

                if ctx.parametros().mais_parametros().parametros().mais_parametros().parametros() is not None:
                    self.erros_semanticos += self.getLinhaDoErro(ctx.start) + \
                                             'não é permitido mais que dois parâmetros' + \
                                             self.getRegraDoErro(ctx.start)
                    raise Exception(self.erros_semanticos)

        if alinhamento > 1:
            self.erros_semanticos += self.getLinhaDoErro(ctx.start) + 'parâmetro "alinhamento" repetido.'

        if cor > 1:
            self.erros_semanticos += self.getLinhaDoErro(ctx.start) + 'parâmetro "cor" repetido.'

        if self.erros_semanticos != '':
            raise Exception(self.erros_semanticos)
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
