# UNIVERSIDADE FEDERAL DE SÃO CARLOS
# Construção de Compiladores 2 - 2016/2
# Trabalho 3

# Marcelo de Oliveira da Silva

from ANTLR.t3_cc2Visitor import *
from ANTLR.t3_cc2Parser import *


# Constantes que definem os parâmetros da linguagem
ALINHAMENTO = 'alinhamento'
COR = 'cor'
FUNDO = 'fundo'
TITULO = 'titulo'
TAMANHO = 'tamanho'
FONTE = 'fonte'


class AnalisadorSemantico(t3_cc2Visitor):

    # O analisador semântico para a execução lançando uma exceção em caso de erros semânticos, entretanto, algumas
    # verificações adicionais são realizadas, que não impedem a geração de código, mas que são interessantes de serem
    # notificadas. Essas situações são armazenadas nessa variável warnings
    warnings = ''

    # Conjunto de estruturas utilizadas para indicar o warning de imagens com parâmetro de tamanho maior do que o
    # máximo que cabe no conjunto de colunas em que a imagem está inserida
    lista_de_imagens = []  # mapeia todas as imagens que foram utilizadas dentro de um bloco 'colunas'
    imagem_dentro_de_colunas = False  # utilizado para adicionar itens em lista_de_imagens
    quantidade_colunas = 0  # conta a quantidade de colunas dentro de um bloco 'colunas'
    colunas = []  # mapeia todas as colunas individuais que estão dentro de blocos 'colunas' do programa

    # Função para obter os warnings (a remoção do último elemento é para eliminar um \n)
    def get_warnings(self):
        return self.warnings[:-1]

    # Funções utilizadas para montar a mensagem de erro e lançar a exceção
    def get_linha_do_erro(self, dados_do_erro):
        return 'Erro semântico na linha ' + str(dados_do_erro).split(',')[3].split(':')[0] + ': '

    def get_linha_do_warning(self, dados_do_erro):
        return str(dados_do_erro).split(',')[3].split(':')[0]

    def get_regra_do_erro(self, dados_do_erro):
        return ' no comando ' + str(dados_do_erro).split(',')[1].split('=')[1] + '.'

    def get_erro_parametro_nao_permitido(self, dados_do_erro, parametro):
        erro = self.get_linha_do_erro(dados_do_erro) + 'não é permitido o parâmetro "' + parametro + '"' + \
               self.get_regra_do_erro(dados_do_erro)
        raise Exception(erro)

    def get_erro_parametro_repetido(self, dados_do_erro, parametro):
        erro = self.get_linha_do_erro(dados_do_erro) + 'parâmetro "' + parametro + '" repetido.'
        raise Exception(erro)

    def get_erro_proibido_mais_que_dois_parametros(self, dados_do_erro):
        erro = self.get_linha_do_erro(dados_do_erro) + 'não é permitido mais que dois parâmetros' + \
               self.get_regra_do_erro(dados_do_erro)
        raise Exception(erro)

    def get_erro_proibido_mais_que_um_parametro(self, dados_do_erro):
        erro = self.get_linha_do_erro(dados_do_erro) + 'não é permitido mais que um parâmetro' + \
               self.get_regra_do_erro(dados_do_erro)
        raise Exception(erro)

    # Início da verificação do programa
    def visitSite(self, ctx: t3_cc2Parser.SiteContext):
        titulo_site = 0
        fonte = 0

        # Verificação se o primeiro parâmetro (se existir) é valido para a regra 'site'
        if ctx.parametros() is not None:
            if ctx.parametros().cor() is not None:
                self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=COR)
            if ctx.parametros().alinhamento() is not None:
                self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=ALINHAMENTO)
            if ctx.parametros().tamanho() is not None:
                self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=TAMANHO)
            if ctx.parametros().fundo() is not None:
                self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=FUNDO)

            if ctx.parametros().titulo_site() is not None:
                titulo_site += 1
            if ctx.parametros().fonte() is not None:
                fonte += 1

            # Verificação se o segundo parâmetro (se existir) é valido para a regra 'site'
            if ctx.parametros().mais_parametros().parametros() is not None:
                if ctx.parametros().mais_parametros().parametros().cor() is not None:
                    self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=COR)
                if ctx.parametros().mais_parametros().parametros().alinhamento() is not None:
                    self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=ALINHAMENTO)
                if ctx.parametros().mais_parametros().parametros().tamanho() is not None:
                    self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=TAMANHO)
                if ctx.parametros().mais_parametros().parametros().fundo() is not None:
                    self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=FUNDO)

                if ctx.parametros().mais_parametros().parametros().titulo_site() is not None:
                    titulo_site += 1
                if ctx.parametros().mais_parametros().parametros().fonte() is not None:
                    fonte += 1

                # Verificação se existem mais que dois parâmetros
                if ctx.parametros().mais_parametros().parametros().mais_parametros().parametros() is not None:
                    self.get_erro_proibido_mais_que_dois_parametros(dados_do_erro=ctx.start)

        # Verificação se algum parâmetro foi repetido
        if fonte > 1:
            self.get_erro_parametro_repetido(dados_do_erro=ctx.start, parametro=FONTE)
        if titulo_site > 1:
            self.get_erro_parametro_repetido(dados_do_erro=ctx.start, parametro=TITULO)

        # Verificação do tipo de comando de sidebar (se existir) foi utilizado
        # Se utilizado 'sidebar=menu', verifica se existe um menu declarado
        if ctx.sidebar() is not None:
            if ctx.sidebar().getText() == 'sidebar=menu' and ctx.menu() is None:
                raise Exception(self.get_linha_do_erro(ctx.sidebar().start) +
                                'uso do comando "sidebar=menu" sem a declaração de um componente "menu".')

        # Chama a verificação para 'banner', se existir
        if ctx.banner() is not None:
            self.visitBanner(ctx.banner())

        # Visita a regra 'conteudo' sempre (pois esta é obrigatória na sintaxe)
        self.visitConteudo(ctx.conteudo())

        # Chama a verificação para 'rodape', se existir
        if ctx.rodape() is not None:
            self.visitRodape(ctx.rodape())

        # Verificação do warning de imagens com tamanho maior do que cabe nas colunas em que foram inseridas
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
        # Verificação se existe parâmetro, e se o mesmo é válido (único parâmetro válido para 'banner' é 'fundo')
        if ctx.parametros() is not None:
            if ctx.parametros().cor() is not None:
                self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=COR)
            if ctx.parametros().alinhamento() is not None:
                self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=ALINHAMENTO)
            if ctx.parametros().tamanho() is not None:
                self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=TAMANHO)
            if ctx.parametros().fonte() is not None:
                self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=FONTE)
            if ctx.parametros().titulo_site() is not None:
                self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=TITULO)

            # Verificação se existe mais que um parâmetro
            if ctx.parametros().mais_parametros().parametros() is not None:
                self.get_erro_proibido_mais_que_um_parametro(ctx.start)

            # Verificação do parâmetro (imagem ou cor) para o parâmetro 'fundo'
            ja_tem_parametro = False
            if ctx.parametros().fundo().imagem() is not None:
                ja_tem_parametro = True
                # E no caso do parâmetro ser 'imagem', esta não pode ter parâmetros adicionais no contexto de 'banner'
                if ctx.parametros().fundo().imagem().parametros() is not None:
                    raise Exception(self.get_linha_do_erro(ctx.start) +
                                    'não é permitido declarar parâmetros para uma imagem de fundo' +
                                    self.get_regra_do_erro(ctx.start))
                # E a imagem de fundo do banner não pode ter links
                if ctx.parametros().fundo().imagem().link() is not None:
                    raise Exception(self.get_linha_do_erro(ctx.start) +
                                    'não é permitido declarar links para uma imagem de fundo' +
                                    self.get_regra_do_erro(ctx.start))
            if ctx.parametros().fundo().cor() is not None and ja_tem_parametro:
                self.get_erro_proibido_mais_que_um_parametro(dados_do_erro=ctx.start)

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
            # Set de variáveis que auxiliam a verificação do warning a seguir
            self.imagem_dentro_de_colunas = True
            self.colunas.append(0)

            # Visitação das colunas
            self.visitColuna(ctx.coluna())
            self.visitMais_colunas(ctx.mais_colunas())

            # Verificação de um warning: programador declarou comando 'colunas' e colocou apenas um componente 'coluna'
            # Neste caso, poderia ter utilizado o componente 'coluna' diretamente
            if ctx.mais_colunas().coluna() is None:
                self.warnings += "Warning na linha " + self.get_linha_do_warning(ctx.start) + \
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
        self.quantidade_colunas += 1  # contagem das colunas para validação de warning

        # Verificação dos parâmetros de 'coluna', se existirem
        if ctx.parametros() is not None:
            if ctx.parametros().cor() is not None:
                self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=COR)
            if ctx.parametros().tamanho() is not None:
                self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=TAMANHO)
            if ctx.parametros().fonte() is not None:
                self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=FONTE)
            if ctx.parametros().titulo_site() is not None:
                self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=TITULO)

            if ctx.parametros().mais_parametros().parametros() is not None:
                self.get_erro_proibido_mais_que_um_parametro(dados_do_erro=ctx.start)

        if ctx.imagem() is not None:
            self.visitImagem(ctx.imagem())
        if ctx.texto() is not None:
            self.visitTexto(ctx.texto())
        return

    def visitTitulo(self, ctx):
        alinhamento = 0
        cor = 0

        # Verificação se o primeiro parâmetro (se existir) é valido para a regra 'titulo'
        if ctx.parametros() is not None:
            if ctx.parametros().tamanho() is not None:
                self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=TAMANHO)
            if ctx.parametros().fundo() is not None:
                self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=FUNDO)
            if ctx.parametros().titulo_site() is not None:
                self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=TITULO)
            if ctx.parametros().fonte() is not None:
                self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=FONTE)

            if ctx.parametros().alinhamento() is not None:
                alinhamento += 1
            if ctx.parametros().cor() is not None:
                cor += 1

                # Verificação se o segundo parâmetro (se existir) é valido para a regra 'titulo'
            if ctx.parametros().mais_parametros().parametros() is not None:
                if ctx.parametros().mais_parametros().parametros().tamanho() is not None:
                    self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=TAMANHO)
                if ctx.parametros().mais_parametros().parametros().fundo() is not None:
                    self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=FUNDO)
                if ctx.parametros().mais_parametros().parametros().titulo_site() is not None:
                    self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=TITULO)
                if ctx.parametros().mais_parametros().parametros().fonte() is not None:
                    self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=FONTE)

                if ctx.parametros().mais_parametros().parametros().alinhamento() is not None:
                    alinhamento += 1
                if ctx.parametros().mais_parametros().parametros().cor() is not None:
                    cor += 1

                # Verificação se existem mais que dois parâmetros
                if ctx.parametros().mais_parametros().parametros().mais_parametros().parametros() is not None:
                    self.get_erro_proibido_mais_que_dois_parametros(dados_do_erro=ctx.start)

        # Verificação se algum parâmetro foi repetido
        if alinhamento > 1:
            self.get_erro_parametro_repetido(dados_do_erro=ctx.start, parametro=ALINHAMENTO)
        if cor > 1:
            self.get_erro_parametro_repetido(dados_do_erro=ctx.start, parametro=COR)

        return

    def visitSubtitulo(self, ctx: t3_cc2Parser.SubtituloContext):
        # Caso interessante: os parâmetros da regra 'subtitulo' tem exatamente as mesmas propriedades da regra 'titulo'.
        # Para evitar repetição de código, foi removido o casting explícito da função visitTitulo
        # (ctx: t3_cc2Parser.TituloContext) e 'subtitulo' é verificado com essa regra
        self.visitTitulo(ctx)
        return

    def visitTexto(self, ctx: t3_cc2Parser.TextoContext):
        # Mesmo caso da função anterior. Evita repetição de código :-)
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

        # Verificação se o primeiro parâmetro (se existir) é valido para a regra 'imagem'
        if ctx.parametros() is not None:
            if ctx.parametros().cor() is not None:
                self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=COR)
            if ctx.parametros().fundo() is not None:
                self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=FUNDO)
            if ctx.parametros().titulo_site() is not None:
                self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=TITULO)
            if ctx.parametros().fonte() is not None:
                self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=FONTE)

            if ctx.parametros().tamanho() is not None:
                tamanho += 1
                opcao_tamanho = ctx.parametros().tamanho().opcao_tamanho().getText()
            if ctx.parametros().alinhamento() is not None:
                alinhamento += 1

            # Verificação se o segundo parâmetro (se existir) é valido para a regra 'imagem'
            if ctx.parametros().mais_parametros().parametros() is not None:
                if ctx.parametros().mais_parametros().parametros().cor() is not None:
                    self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=COR)
                if ctx.parametros().mais_parametros().parametros().fundo() is not None:
                    self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=FUNDO)
                if ctx.parametros().mais_parametros().parametros().titulo_site() is not None:
                    self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=TITULO)
                if ctx.parametros().mais_parametros().parametros().fonte() is not None:
                    self.get_erro_parametro_nao_permitido(dados_do_erro=ctx.start, parametro=FONTE)
                if ctx.parametros().mais_parametros().parametros().tamanho() is not None:
                    tamanho += 1
                    opcao_tamanho = ctx.parametros().tamanho().opcao_tamanho().getText()
                if ctx.parametros().mais_parametros().parametros().alinhamento() is not None:
                    alinhamento += 1

                # Verificação se existem mais que dois parâmetros
                if ctx.parametros().mais_parametros().parametros().mais_parametros().parametros() is not None:
                    self.get_erro_proibido_mais_que_dois_parametros(dados_do_erro=ctx.start)

        # Verificação se algum parâmetro foi repetido
        if tamanho > 1:
            self.get_erro_parametro_repetido(dados_do_erro=ctx.start, parametro=TAMANHO)
        if alinhamento > 1:
            self.get_erro_parametro_repetido(dados_do_erro=ctx.start, parametro=ALINHAMENTO)

        # Set de informações que serão utilizadas para validar o warning do tamanho das imagens dentro de colunas
        if self.imagem_dentro_de_colunas:
            imagem = {
                'linha': self.get_linha_do_warning(ctx.start),
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
