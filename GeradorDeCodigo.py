from ANTLR.t3_cc2Visitor import *
from ANTLR.t3_cc2Parser import *

EXTRA_PEQUENO = 'extra-pequeno'
PEQUENO = 'pequeno'
NORMAL = 'medio'
GRANDE = 'grande'
EXTRA_GRANDE = 'extra-grande'

class GeradorDeCodigo(t3_cc2Visitor):
    codigo = """<!DOCTYPE html>
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
    #MENU
    #PUSHER_INICIO
    #SIDEBAR
    #BANNER
    #CONTEUDO
    #RODAPE
    #PUSHER_FIM
</body>
</html>
    """

    itens_menu = ''

    def visitSite(self, ctx: t3_cc2Parser.SiteContext):
        print("visitSite\n")
        self.codigo = self.codigo.replace("#TITULODOSITE", self.visitTitulo_site(ctx.titulo_site()))
        self.codigo = self.codigo.replace('#MENU', self.visitMenu(ctx.menu()))
        self.codigo = self.codigo.replace('#SIDEBAR', self.visitSidebar(ctx.sidebar()))
        self.codigo = self.codigo.replace('#BANNER', self.visitBanner(ctx.banner()))
        self.codigo = self.codigo.replace('#CONTEUDO', self.visitConteudo(ctx.conteudo()))
        self.codigo = self.codigo.replace('#RODAPE', self.visitRodape(ctx.rodape()))

        if ctx.sidebar() is not None:
            script_sidebar = """<script>
        $(document)
            .ready(function() {
                $('.ui.sidebar')
                    .sidebar('attach events', '.toc.item')
                ;
            })
        ;
    </script>"""

            self.codigo = self.codigo.replace("#SCRIPT_SIDEBAR", script_sidebar)
            self.codigo = self.codigo.replace("#PUSHER_INICIO", '<div class="pusher">')
            self.codigo = self.codigo.replace("#PUSHER_FIM", '</div>')

            botao_sidebar = """
                        <a class="toc item">
                            <i class="sidebar icon"></i>
                        </a>
                        """
            self.codigo = self.codigo.replace("#BOTAO_SIDEBAR", botao_sidebar)


    def visitCadeia(self, cadeia):
        return str(cadeia)[1:-1]

    def visitTitulo_site(self, ctx: t3_cc2Parser.Titulo_siteContext):
        print("visitTitulo_site\n")
        return self.visitCadeia(ctx.CADEIA()) if ctx.CADEIA() is not None else ''

    def visitMenu(self, ctx: t3_cc2Parser.MenuContext):
        print("visitMenu\n")
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

            menu = menu.replace('#ITEM', (self.visitItem(ctx.item()) if ctx.item() is not None else '') +
                                (self.visitMais_itens(ctx.mais_itens()) if ctx.mais_itens() is not None else ''))
            return menu

    def visitSidebar(self, ctx: t3_cc2Parser.SidebarContext):
        print("visitSidebar\n")

        if ctx is not None:

            sidebar = """
            <!-- Sidebar -->
            <div class="ui vertical inverted sidebar menu">
                #ITEM
            </div>
            """

            if ctx.getText() == 'sidebar=menu':
                sidebar = sidebar.replace('#ITEM', self.itens_menu)
            else:
                sidebar = sidebar.replace('#ITEM', (self.visitItem(ctx.item()) if ctx.item() is not None else '') +
                                          (self.visitMais_itens(ctx.mais_itens()) if ctx.mais_itens() is not None else ''))

            return sidebar
        else:
            return ''

    def visitItem(self, ctx: t3_cc2Parser.ItemContext):
        print("visitItem\n")
        if ctx is not None:
            item = '<a class="item" href="#LINK"#TARGET>#CADEIA</a>'

            item = item.replace("#CADEIA", self.visitCadeia(ctx.CADEIA()) if ctx.CADEIA() is not None else '')
            item = item.replace('#LINK', self.visitLink(ctx.link()))
            item = item.replace("#TARGET", self.visitNova_aba(ctx.link().nova_aba()))

            self.itens_menu += item + '\n'
            return item
        else:
            return ''

    def visitMais_itens(self, ctx: t3_cc2Parser.Mais_itensContext):
        print('visitMais_itens\n')
        itens = (self.visitItem(ctx.item()) if ctx.item() is not None else '') + \
                (self.visitMais_itens(ctx.mais_itens()) if ctx.mais_itens() is not None else '')

        return itens

    def visitLink(self, ctx: t3_cc2Parser.LinkContext):
        print('visitLink\n')
        return self.visitCadeia(ctx.CADEIA()) if ctx is not None and ctx.CADEIA() is not None else ''

    def visitNova_aba(self, ctx: t3_cc2Parser.Nova_abaContext):
        print('visitNova_aba\n')
        return ' target="_blank"' if ctx is not None else ''

    def visitBanner(self, ctx: t3_cc2Parser.BannerContext):
        print('visitBanner\n')
        banner = """
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

        #banner {
            display: -webkit-box;
            display: -webkit-flex;
            display: -ms-flexbox;
            display: flex;
            -webkit-box-align: center;
            -webkit-align-items: center;
            -ms-flex-align: center;
            align-items: center;
            text-align: center;
        }

        </style>
        <div class="ui inverted vertical masthead center aligned segment" id="banner">
            <div class="ui text container">
                #IMAGEM
                #TEXTO
            </div>
        </div>

        """

        banner = banner.replace('#IMAGEM', self.visitImagem(ctx.imagem()) if ctx.imagem() is not None else '')
        banner = banner.replace('#TEXTO', self.visitTexto(ctx.texto()) if ctx.texto() is not None else '').\
            replace("header", "inverted header")

        return banner

    def visitConteudo(self, ctx: t3_cc2Parser.ConteudoContext):
        secao = self.visitSecao(ctx.secao()) if ctx.secao() is not None else ''
        mais_secoes = self.visitMais_secoes(ctx.mais_secoes()) if ctx.mais_secoes() is not None else ''
        return secao + mais_secoes

    def visitSecao(self, ctx: t3_cc2Parser.SecaoContext):
        self.quantidade_colunas = 0

        secao = """
        <div class="ui vertical segment">
            <div class="ui equal width center aligned grid container">
            <div class="middle aligned row">
                #COLUNAS
            </div>
            </div>
        </div>
        """
        colunas = (self.visitColunas(ctx.colunas()) if ctx.colunas() is not None else '') +\
                  (self.visitColuna(ctx.coluna()) if ctx.coluna() is not None else '')

        secao = secao.replace('#COLUNAS', colunas)

        return secao

    def visitMais_secoes(self, ctx: t3_cc2Parser.Mais_secoesContext):
        mais_secoes = (self.visitSecao(ctx.secao()) if ctx.secao() is not None else '') +\
                      (self.visitMais_secoes(ctx.mais_secoes()) if ctx.mais_secoes() is not None else '')

        return mais_secoes

    def visitColunas(self, ctx: t3_cc2Parser.ColunasContext):
        colunas = (self.visitColuna(ctx.coluna()) if ctx.coluna() is not None else '') +\
                  (self.visitMais_colunas(ctx.mais_colunas()) if ctx.mais_colunas() is not None else '')

        return colunas

    def visitMais_colunas(self, ctx: t3_cc2Parser.Mais_colunasContext):
        return (self.visitColuna(ctx.coluna()) if ctx.coluna() is not None else '') +\
               (self.visitMais_colunas(ctx.mais_colunas()) if ctx.mais_colunas() is not None else '')

    def visitColuna(self, ctx: t3_cc2Parser.ColunaContext):
        self.quantidade_colunas += 1

        coluna = """
        <div class="#ALINHAMENTOcolumn">
                #CONTEUDO_COLUNA
        </div>
        """

        alinhamento = str(ctx.alinhamento().opcao_alinhamento().getText()) if ctx.alinhamento() is not None else ''

        alinhamento_semantic = ''
        if alinhamento == 'centralizado':
            alinhamento_semantic = 'center aligned '
        elif alinhamento == 'esquerda':
            alinhamento_semantic = 'left floated left aligned '
        elif alinhamento == 'direita':
            alinhamento_semantic = 'right floated right aligned '

        coluna = coluna.replace('#ALINHAMENTO', alinhamento_semantic)

        coluna = coluna.replace('#CONTEUDO_COLUNA',
                                (self.visitImagem(ctx.imagem()) if ctx.imagem() is not None else '') +
                                (self.visitTexto(ctx.texto()) if ctx.texto() is not None else ''))

        coluna = coluna.replace('#ALINHAMENTO_IMAGEM', (('<p align=' + alinhamento_semantic.split(' ')[0] + '>')
                                                        if alinhamento_semantic != '' else ''))
        coluna = coluna.replace('#FECHA_ALINHAMENTO_IMAGEM', '</p>' if alinhamento_semantic != '' else '')

        return coluna

    def visitTitulo(self, ctx: t3_cc2Parser.TituloContext):
        if ctx.parametro() is not None:
            self.codigo += "parametros("
            self.visitParametro(ctx.parametro())
            self.codigo += ")"
        return ('<h1 class="ui header">' + self.visitCadeia(ctx.CADEIA()) + '</h1>') if ctx.CADEIA() is not None else ''

    def visitSubtitulo(self, ctx: t3_cc2Parser.SubtituloContext):
        if ctx.parametro() is not None:
            self.codigo += "parametros("
            self.visitParametro(ctx.parametro())
            self.codigo += ")"
        return ('<h2 class="ui header">' + self.visitCadeia(ctx.CADEIA()) + '</h2>') if ctx.CADEIA() is not None else ''

    def visitTexto(self, ctx: t3_cc2Parser.TextoContext):
        try:
            if ctx.parametro() is not None:
                self.codigo += "parametros("
                self.visitParametro(ctx.parametro())
                self.codigo += ")"
        except:
            pass

        return self.visitConteudo_texto(ctx.conteudo_texto()) if ctx.conteudo_texto() is not None else ''

    def visitConteudo_texto(self, ctx: t3_cc2Parser.Conteudo_textoContext):
        return (self.visitTitulo(ctx.titulo()) if ctx.titulo() is not None else '')\
               + (self.visitSubtitulo(ctx.subtitulo()) if ctx.subtitulo() is not None else '')\
               + (self.visitParagrafo(ctx.paragrafo()) if ctx.paragrafo() is not None else '')\
               + (self.visitMais_conteudo_texto(ctx.mais_conteudo_texto())
                  if ctx.mais_conteudo_texto() is not None else '')

    def visitMais_conteudo_texto(self, ctx: t3_cc2Parser.Mais_conteudo_textoContext):
        return self.visitConteudo_texto(ctx.conteudo_texto()) if ctx.conteudo_texto() is not None else '' + \
               self.visitMais_conteudo_texto(ctx.mais_conteudo_texto()) if ctx.mais_conteudo_texto() is not None else ''

    def visitParagrafo(self, ctx: t3_cc2Parser.ParagrafoContext):
        if ctx.parametro() is not None:
            self.codigo += "parametros("
            self.visitParametro(ctx.parametro())
            self.codigo += ")"

        paragrafo = '#LINK' + ('<p>' + self.visitCadeia(ctx.CADEIA()) + '</p>#FECHALINK') \
            if ctx.CADEIA() is not None else ''

        link = '\n<a href="' + self.visitLink(ctx.link()) + '"' + self.visitNova_aba(ctx.link().nova_aba()) + '>\n' \
            if ctx.link() is not None else ''
        fecha_link = '\n</a>' if ctx.link() is not None else ''

        paragrafo = paragrafo.replace('#LINK', link).replace('#FECHALINK', fecha_link)

        return paragrafo

    def visitImagem(self, ctx: t3_cc2Parser.ImagemContext):
        imagem = '#ALINHAMENTO_IMAGEM#LINK<img src="' + self.visitCadeia(ctx.CADEIA()).replace('"', '') + \
                 '" class="ui #TAMANHO_IMAGEM image">#FECHALINK#FECHA_ALINHAMENTO_IMAGEM' if ctx.CADEIA() is not None else ''

        tamanho_imagem = self.visitTamanho(ctx.tamanho()) if ctx.tamanho() is not None else ''

        if tamanho_imagem == EXTRA_PEQUENO:
            tamanho_imagem = 'tiny'
        elif tamanho_imagem == PEQUENO:
            tamanho_imagem = 'small'
        elif tamanho_imagem == NORMAL:
            tamanho_imagem = 'medium'
        elif tamanho_imagem == GRANDE:
            tamanho_imagem = 'large'
        elif tamanho_imagem == EXTRA_GRANDE:
            tamanho_imagem = 'big'
        else:
            tamanho_imagem = 'medium'

        imagem = imagem.replace('#TAMANHO_IMAGEM', tamanho_imagem)

        link = self.visitLink(ctx.link()) if ctx.link() is not None else ''
        target = self.visitNova_aba(ctx.link().nova_aba()) if ctx.link() is not None else ''

        imagem = imagem.replace('#LINK', '<a href="' + link + '"' + target + '>\n').replace('#FECHALINK', '\n</a>')

        return imagem

    def visitRodape(self, ctx: t3_cc2Parser.RodapeContext):
        rodape = """
        <div class="ui inverted vertical footer segment">
            <div class="ui container">
                #RODAPE
            </div>
        </div>
        """

        rodape = rodape.replace('#RODAPE', self.visitTexto(ctx.texto())).replace('header', 'inverted header')
        rodape = rodape.replace('<h1', '<h3').replace('</h1>', '</h3>').replace('<h2', '<h4').replace('</h2>', '</h4>')
        return rodape

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
