from ANTLR.t3_cc2Visitor import *
from ANTLR.t3_cc2Parser import *

ALINHAMENTO = 'alinhamento'
COR = 'cor'
FUNDO = 'fundo'
TITULO = 'titulo'
TAMANHO = 'tamanho'
FONTE = 'fonte'


class AnalisadorSemantico(t3_cc2Visitor):
    warnings = ''

    lista_de_imagens = []
    quantidade_colunas = 0
    colunas = []
    imagem_dentro_de_colunas = False

    def getWarnings(self):
        return self.warnings[:-1]

    def getLinhaDoErro(self, dados_do_erro):
        return 'Erro semântico na linha ' + str(dados_do_erro).split(',')[3].split(':')[0] + ': '

    def getLinhaDoWarning(self, dados_do_erro):
        return str(dados_do_erro).split(',')[3].split(':')[0]

    def getRegraDoErro(self, dados_do_erro):
        return ' no comando ' + str(dados_do_erro).split(',')[1].split('=')[1] + '.'

    def getErroParametroNaoPermitido(self, dados_do_erro, parametro):
        erro = self.getLinhaDoErro(dados_do_erro) + 'não é permitido o parâmetro "' + parametro + '"' + \
               self.getRegraDoErro(dados_do_erro)
        raise Exception(erro)

    def getErroParametroRepetido(self, dados_do_erro, parametro):
        erro = self.getLinhaDoErro(dados_do_erro) + 'parâmetro "' + parametro + '" repetido.'
        raise Exception(erro)

    def getErroProibidoMaisQueDoisParametros(self, dados_do_erro):
        erro = self.getLinhaDoErro(dados_do_erro) + 'não é permitido mais que dois parâmetros' + \
               self.getRegraDoErro(dados_do_erro)
        raise Exception(erro)

    def getErroProibidoMaisQueUmParametro(self, dados_do_erro):
        erro = self.getLinhaDoErro(dados_do_erro) + 'não é permitido mais que um parâmetro' + \
               self.getRegraDoErro(dados_do_erro)
        raise Exception(erro)

    def visitSite(self, ctx: t3_cc2Parser.SiteContext):
        titulo_site = 0
        fonte = 0

        if ctx.parametros() is not None:
            if ctx.parametros().cor() is not None:
                self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=COR)
            if ctx.parametros().alinhamento() is not None:
                self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=ALINHAMENTO)
            if ctx.parametros().tamanho() is not None:
                self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=TAMANHO)
            if ctx.parametros().fundo() is not None:
                self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=FUNDO)

            if ctx.parametros().titulo_site() is not None:
                titulo_site += 1
            if ctx.parametros().fonte() is not None:
                fonte += 1

            if ctx.parametros().mais_parametros().parametros() is not None:
                if ctx.parametros().mais_parametros().parametros().cor() is not None:
                    self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=COR)
                if ctx.parametros().mais_parametros().parametros().alinhamento() is not None:
                    self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=ALINHAMENTO)
                if ctx.parametros().mais_parametros().parametros().tamanho() is not None:
                    self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=TAMANHO)
                if ctx.parametros().mais_parametros().parametros().fundo() is not None:
                    self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=FUNDO)

                if ctx.parametros().mais_parametros().parametros().titulo_site() is not None:
                    titulo_site += 1
                if ctx.parametros().mais_parametros().parametros().fonte() is not None:
                    fonte += 1

                if ctx.parametros().mais_parametros().parametros().mais_parametros().parametros() is not None:
                    self.getErroProibidoMaisQueDoisParametros(dados_do_erro=ctx.start)

        if fonte > 1:
            self.getErroParametroRepetido(dados_do_erro=ctx.start, parametro=FONTE)
        if titulo_site > 1:
            self.getErroParametroRepetido(dados_do_erro=ctx.start, parametro=TITULO)

        if ctx.sidebar() is not None:
            if ctx.sidebar().getText() == 'sidebar=menu' and ctx.menu() is None:
                raise Exception(self.getLinhaDoErro(ctx.sidebar().start) +
                                'uso do comando "sidebar=menu" sem a declaração de um componente "menu".')

        if ctx.banner() is not None:
            self.visitBanner(ctx.banner())

        self.visitConteudo(ctx.conteudo())

        if ctx.rodape() is not None:
            self.visitRodape(ctx.rodape())

        for imagem in self.lista_de_imagens:
            opcao_tamanho = imagem['tamanho']
            colunas = self.colunas[imagem['indice_coluna']]

            if (((opcao_tamanho == 'grande' or opcao_tamanho == 'extra-grande') and colunas > 2) or
                    ((opcao_tamanho == 'medio' or opcao_tamanho == '') and colunas > 4) or
                    (opcao_tamanho == 'pequeno' and colunas > 7) or
                    (opcao_tamanho == 'extra-pequeno' and colunas > 11)):

                if opcao_tamanho != '':
                    self.warnings += 'Warning na linha ' + imagem['linha'] + \
                                     ': imagem muito grande para o tamanho da coluna. A imagem será redimensionada.\n'
                elif opcao_tamanho == '':
                    self.warnings += 'Warning na linha ' + imagem['linha'] + \
                                     ': imagem muito grande (tamanho inferido = médio) para o tamanho da coluna. ' \
                                     'A imagem será redimensionada.\n'

        return

    def visitBanner(self, ctx: t3_cc2Parser.BannerContext):
        if ctx is not None:
            if ctx.parametros() is not None:
                if ctx.parametros().cor() is not None:
                    self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=COR)
                if ctx.parametros().alinhamento() is not None:
                    self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=ALINHAMENTO)
                if ctx.parametros().tamanho() is not None:
                    self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=TAMANHO)
                if ctx.parametros().fonte() is not None:
                    self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=FONTE)
                if ctx.parametros().titulo_site() is not None:
                    self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=TITULO)

                if ctx.parametros().mais_parametros().parametros() is not None:
                    self.getErroProibidoMaisQueUmParametro(ctx.start)

                ja_tem_parametro = False
                if ctx.parametros().fundo().imagem() is not None:
                    ja_tem_parametro = True
                    if ctx.parametros().fundo().imagem().parametros() is not None:
                        raise Exception(self.getLinhaDoErro(ctx.start) + \
                                                 'não é permitido declarar parâmetros para uma imagem de fundo' + \
                                                 self.getRegraDoErro(ctx.start))
                if ctx.parametros().fundo().cor() is not None and ja_tem_parametro:
                    self.getErroProibidoMaisQueUmParametro(dados_do_erro=ctx.start)

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
        self.quantidade_colunas = 0
        if ctx.coluna() is not None:
            self.imagem_dentro_de_colunas = True
            self.colunas.append(0)
            self.visitColuna(ctx.coluna())
            self.visitMais_colunas(ctx.mais_colunas())

            if ctx.mais_colunas().coluna() is None:
                self.warnings += "Warning na linha " + self.getLinhaDoWarning(ctx.start) + \
                                 ": componente 'colunas' sendo utilizado com apenas uma coluna. Use o comando " \
                                 "'coluna' neste caso para maior desempenho do compilador.\n"
            self.colunas[-1] += self.quantidade_colunas
        self.imagem_dentro_de_colunas = False
        return

    def visitMais_colunas(self, ctx: t3_cc2Parser.Mais_colunasContext):
        if ctx.coluna() is not None:
            self.visitColuna(ctx.coluna())
            self.visitMais_colunas(ctx.mais_colunas())
        return

    def visitColuna(self, ctx: t3_cc2Parser.ColunaContext):
        self.quantidade_colunas += 1
        if ctx.parametros() is not None:
            if ctx.parametros().cor() is not None:
                self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=COR)
            if ctx.parametros().tamanho() is not None:
                self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=TAMANHO)
            if ctx.parametros().fonte() is not None:
                self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=FONTE)
            if ctx.parametros().titulo_site() is not None:
                self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=TITULO)

            if ctx.parametros().mais_parametros().parametros() is not None:
                self.getErroProibidoMaisQueUmParametro(dados_do_erro=ctx.start)

        if ctx.imagem() is not None:
            self.visitImagem(ctx.imagem())
        if ctx.texto() is not None:
            self.visitTexto(ctx.texto())
        return

    def visitTitulo(self, ctx):
        alinhamento = 0
        cor = 0

        if ctx.parametros() is not None:
            if ctx.parametros().tamanho() is not None:
                self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=TAMANHO)
            if ctx.parametros().fundo() is not None:
                self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=FUNDO)
            if ctx.parametros().titulo_site() is not None:
                self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=TITULO)
            if ctx.parametros().fonte() is not None:
                self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=FONTE)

            if ctx.parametros().alinhamento() is not None:
                alinhamento += 1
            if ctx.parametros().cor() is not None:
                cor += 1

            if ctx.parametros().mais_parametros().parametros() is not None:
                if ctx.parametros().mais_parametros().parametros().tamanho() is not None:
                    self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=TAMANHO)
                if ctx.parametros().mais_parametros().parametros().fundo() is not None:
                    self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=FUNDO)
                if ctx.parametros().mais_parametros().parametros().titulo_site() is not None:
                    self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=TITULO)
                if ctx.parametros().mais_parametros().parametros().fonte() is not None:
                    self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=FONTE)

                if ctx.parametros().mais_parametros().parametros().alinhamento() is not None:
                    alinhamento += 1
                if ctx.parametros().mais_parametros().parametros().cor() is not None:
                    cor += 1

                if ctx.parametros().mais_parametros().parametros().mais_parametros().parametros() is not None:
                    self.getErroProibidoMaisQueDoisParametros(dados_do_erro=ctx.start)

        if alinhamento > 1:
            self.getErroParametroRepetido(dados_do_erro=ctx.start, parametro=ALINHAMENTO)
        if cor > 1:
            self.getErroParametroRepetido(dados_do_erro=ctx.start, parametro=COR)

        return

    def visitSubtitulo(self, ctx: t3_cc2Parser.SubtituloContext):
        self.visitTitulo(ctx)
        return

    def visitTexto(self, ctx: t3_cc2Parser.TextoContext):
        self.visitConteudo_texto(ctx.conteudo_texto())
        return

    def visitConteudo_texto(self, ctx: t3_cc2Parser.Conteudo_textoContext):
        if ctx is not None:
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
            self.visitMais_conteudo_texto(ctx.mais_conteudo_texto())
        return

    def visitParagrafo(self, ctx: t3_cc2Parser.ParagrafoContext):
        self.visitTitulo(ctx)
        return

    def visitImagem(self, ctx: t3_cc2Parser.ImagemContext):
        tamanho = 0
        alinhamento = 0
        opcao_tamanho = ''

        if ctx.parametros() is not None:
            if ctx.parametros().cor() is not None:
                self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=COR)
            if ctx.parametros().fundo() is not None:
                self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=FUNDO)
            if ctx.parametros().titulo_site() is not None:
                self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=TITULO)
            if ctx.parametros().fonte() is not None:
                self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=FONTE)

            if ctx.parametros().tamanho() is not None:
                tamanho += 1
                opcao_tamanho = ctx.parametros().tamanho().opcao_tamanho().getText()
            if ctx.parametros().alinhamento() is not None:
                alinhamento += 1

            if ctx.parametros().mais_parametros().parametros() is not None:
                if ctx.parametros().mais_parametros().parametros().cor() is not None:
                    self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=COR)
                if ctx.parametros().mais_parametros().parametros().fundo() is not None:
                    self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=FUNDO)
                if ctx.parametros().mais_parametros().parametros().titulo_site() is not None:
                    self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=TITULO)
                if ctx.parametros().mais_parametros().parametros().fonte() is not None:
                    self.getErroParametroNaoPermitido(dados_do_erro=ctx.start, parametro=FONTE)
                if ctx.parametros().mais_parametros().parametros().tamanho() is not None:
                    tamanho += 1
                    opcao_tamanho = ctx.parametros().tamanho().opcao_tamanho().getText()
                if ctx.parametros().mais_parametros().parametros().alinhamento() is not None:
                    alinhamento += 1

                if ctx.parametros().mais_parametros().parametros().mais_parametros().parametros() is not None:
                    self.getErroProibidoMaisQueDoisParametros(dados_do_erro=ctx.start)

        if tamanho > 1:
            self.getErroParametroRepetido(dados_do_erro=ctx.start, parametro=TAMANHO)
        if alinhamento > 1:
            self.getErroParametroRepetido(dados_do_erro=ctx.start, parametro=ALINHAMENTO)

        if self.imagem_dentro_de_colunas:
            imagem = {
                'linha': self.getLinhaDoWarning(ctx.start),
                'tamanho': opcao_tamanho,
                'indice_coluna': len(self.colunas) - 1
            }
            self.lista_de_imagens.append(imagem)

        return

    def visitRodape(self, ctx: t3_cc2Parser.RodapeContext):
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
