from ANTLR.t3_cc2Visitor import *
from ANTLR.t3_cc2Parser import *

EXTRA_PEQUENO = 'extra-pequeno'
PEQUENO = 'pequeno'
NORMAL = 'medio'
GRANDE = 'grande'
EXTRA_GRANDE = 'extra-grande'

ROBOTO = '<link href="https://fonts.googleapis.com/css?family=Roboto:400,400i,700,700i" rel="stylesheet">'
OPEN_SANS = '<link href="https://fonts.googleapis.com/css?family=Open+Sans:400,400i,700,700i" rel="stylesheet">'

FONTES = {
    'Roboto': ROBOTO,
    'Open Sans': OPEN_SANS,
    'Arial': '',
    'Times New Roman': '',
    'Helvetica': '',
    'Lato': ''
}


def getColor(cor):
    if cor == 'azul':
        return '#0000FF'
    elif cor == 'azul-claro':
        return '#00BFFF'
    elif cor == 'verde':
        return '#32CD32'
    elif cor == 'amarelo':
        return '#FD7000'
    elif cor == 'branco':
        return '#FFFFFF'
    elif cor == 'preto':
        return '#000000'
    elif cor == 'vermelho':
        return '#FF0000'
    elif cor == 'laranja':
        return '#FF8C00'
    elif cor == 'roxo':
        return '#A020F0'
    elif cor == 'rosa':
        return '#FF1493'
    elif cor == 'cinza':
        return '#8B8989'
    elif cor == 'marrom':
        return '#8B4513'
    else:
        return ''

class GeradorDeCodigo(t3_cc2Visitor):
    codigo = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">

    <title>#TITULODOSITE</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/semantic-ui/2.2.6/semantic.min.css">
    #LINK_FONTE
    <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/semantic-ui/2.2.6/semantic.min.js"></script>
    #SCRIPT_SIDEBAR
    <style>
        #FONTE
        p {
            font-size: 1.1em;
        }

        .ui.header.azul, p.azul {
            color: #0000FF;
        }

        .ui.header.azul-claro, p.azul-claro {
            color: #00BFFF;
        }

        .ui.header.verde, p.verde {
            color: #32CD32;
        }

        .ui.header.amarelo, p.amarelo {
            color: #FFD700;
        }

        .ui.header.branco, p.branco {
            color: #FFFFFF;
        }

        .ui.header.preto, p.preto {
            color: #000000;
        }

        .ui.header.vermelho, p.vermelho {
            color: #FF0000;
        }

        .ui.header.laranja, p.laranja {
            color: #FF8C00;
        }

        .ui.header.roxo, p.roxo {
            color: #A020F0;
        }

        .ui.header.rosa, p.rosa {
            color: #FF1493;
        }

        .ui.header.cinza, p.cinza {
            color: #8B8989;
        }

        .ui.header.marrom, p.marrom {
            color: #8B4513;
        }

    </style>
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
        titulo_site = ''
        fonte = ''

        if ctx.parametros() is not None:
            titulo_site = self.visitTitulo_site(ctx.parametros().titulo_site()) \
                if ctx.parametros().titulo_site() is not None else ''
            fonte = self.visitFonte(ctx.parametros().fonte()) if ctx.parametros().fonte() is not None else ''

            if ctx.parametros().mais_parametros() is not None:
                if ctx.parametros().mais_parametros().parametros() is not None:
                    if titulo_site == '':
                        titulo_site = \
                            self.visitTitulo_site(ctx.parametros().mais_parametros().parametros().titulo_site()) \
                                if ctx.parametros().mais_parametros().parametros().titulo_site() is not None else ''
                    if fonte == '':
                        fonte = self.visitFonte(ctx.parametros().mais_parametros().parametros().fonte()) \
                            if ctx.parametros().mais_parametros().parametros().fonte() is not None else ''

        self.codigo = self.codigo.replace('#TITULODOSITE', titulo_site)
        self.codigo = self.codigo.replace('#FONTE',
                                          ('p, .ui.header, a {\n\tfont-family: \'' + fonte + '\', sans-serif;\n}')
                                          if fonte != '' else '')
        self.codigo = self.codigo.replace('#LINK_FONTE', FONTES[fonte] if fonte != '' else '')
        self.codigo = self.codigo.replace('#MENU', self.visitMenu(ctx.menu()) if ctx.menu() is not None else '')
        self.codigo = self.codigo.replace('#SIDEBAR',
                                          self.visitSidebar(ctx.sidebar()) if ctx.sidebar() is not None else '')
        self.codigo = self.codigo.replace('#BANNER',
                                          self.visitBanner(ctx.banner())
                                          if ctx.banner() is not None else
                                          ('<p><br><br></p>' if ctx.menu() is not None else ''))

        self.codigo = self.codigo.replace('#CONTEUDO',
                                          self.visitConteudo(ctx.conteudo()) if ctx.conteudo() is not None else '')
        self.codigo = self.codigo.replace('#RODAPE', self.visitRodape(ctx.rodape()) if ctx.rodape() is not None else '')

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
        return self.visitCadeia(ctx.CADEIA()) if ctx is not None and ctx.CADEIA() is not None else ''

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
                sidebar = sidebar.replace('#ITEM',
                                          (self.visitItem(ctx.item()) if ctx.item() is not None else '') +
                                          (self.visitMais_itens(ctx.mais_itens())
                                           if ctx.mais_itens() is not None else ''))

            return sidebar
        else:
            return ''

    def visitItem(self, ctx: t3_cc2Parser.ItemContext):
        print("visitItem\n")
        if ctx is not None:
            item = '<a class="item" href="#LINK"#TARGET>#CADEIA</a>'

            item = item.replace("#CADEIA", self.visitCadeia(ctx.CADEIA()) if ctx.CADEIA() is not None else '')
            item = item.replace('#LINK', self.visitLink(ctx.link()))
            item = item.replace("#TARGET", self.visitNova_aba(ctx.link().nova_aba()) if ctx.link() is not None else '')

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
            #BACKGROUND
        }

        #titulo_banner {
            font-size: 3.5em;
        }

        #subtitulo_banner {
            font-size: 1.7em;
        }

    </style>

    <div class="ui inverted vertical masthead center aligned segment" id="banner">
        <div class="ui text container">
            #TEXTO
        </div>
    </div>
        """
        banner = banner.replace('#TEXTO', self.visitTexto(ctx.texto()) if ctx.texto() is not None else '').\
            replace('<h1 class="ui header', '<h1 id="titulo_banner" class="ui inverted header')
        banner = banner.replace('<h2 class="ui header">', '<h2 id="subtitulo_banner" class="ui inverted header">')

        background = ''
        if ctx.parametros() is not None:
            if ctx.parametros().fundo() is not None:

                background = ('background: url(' + str(ctx.parametros().fundo().imagem().CADEIA()) +
                              ');\nbackground-size: cover;background-position: center center;')\
                    if ctx.parametros().fundo().imagem() is not None else ''

                if background == '':
                    background = ('background-color: ' +
                                  getColor(self.visitCor(ctx.parametros().fundo().cor())[1:]) + ';') \
                        if ctx.parametros().fundo().cor() is not None else ''

        banner = banner.replace('#BACKGROUND', background)

        return banner

    def visitConteudo(self, ctx: t3_cc2Parser.ConteudoContext):
        secao = self.visitSecao(ctx.secao()) if ctx.secao() is not None else ''
        mais_secoes = self.visitMais_secoes(ctx.mais_secoes()) if ctx.mais_secoes() is not None else ''
        return secao + mais_secoes

    def visitSecao(self, ctx: t3_cc2Parser.SecaoContext):
        secao = """
        <div class="ui vertical segment">
            <div class="ui stackable equal width center aligned grid container">
            #TEXTO
            #COLUNAS
            </div>
        </div>
        """

        novas_colunas = """<div class="middle aligned row">
                #COLUNAS
            </div>"""

        colunas = (self.visitColunas(ctx.colunas()) if ctx.colunas() is not None else '') +\
                  (self.visitColuna(ctx.coluna()) if ctx.coluna() is not None else '')

        if colunas != '':
            secao = secao.replace('#COLUNAS', novas_colunas.replace('#COLUNAS', colunas))
        else:
            secao = secao.replace('#COLUNAS', '')

        nova_linha = """<div class="middle aligned row">
                <div class="column">
                    #TEXTO
                </div>
            </div>
        """

        texto = self.visitTexto(ctx.texto()) if ctx.texto() is not None else ''

        if texto != '':
            secao = secao.replace('#TEXTO', nova_linha.replace('#TEXTO', texto))
        else:
            secao = secao.replace('#TEXTO', '')

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
        coluna = """
        <div class="#ALINHAMENTOcolumn">
                #CONTEUDO_COLUNA
        </div>
        """

        alinhamento = ''

        if ctx.parametros() is not None:
            alinhamento = str(ctx.parametros().alinhamento().opcao_alinhamento().getText()) \
                if ctx.parametros().alinhamento() is not None else ''

            alinhamento_semantic = ''
            if alinhamento == 'centralizado':
                alinhamento_semantic = 'center aligned '
            elif alinhamento == 'esquerda':
                alinhamento_semantic = 'left floated left aligned '
            elif alinhamento == 'direita':
                alinhamento_semantic = 'right floated right aligned '

            alinhamento = alinhamento_semantic

        coluna = coluna.replace('#ALINHAMENTO', alinhamento)

        coluna = coluna.replace('#CONTEUDO_COLUNA',
                                (self.visitImagem(ctx.imagem()) if ctx.imagem() is not None else '') +
                                (self.visitTexto(ctx.texto()) if ctx.texto() is not None else ''))

        coluna = coluna.replace('#ALINHAMENTO_IMAGEM', (('<p align=' + alinhamento.split(' ')[0] + '>')
                                                        if alinhamento != '' else ''))
        coluna = coluna.replace('#FECHA_ALINHAMENTO_IMAGEM', '</p>' if alinhamento != '' else '')

        return coluna

    def visitTitulo(self, ctx: t3_cc2Parser.TituloContext):
        cor = ''
        alinhamento = ''

        if ctx.parametros() is not None:
            cor = self.visitCor(ctx.parametros().cor()) if ctx.parametros().cor() is not None else ''
            alinhamento = (' align="' + self.visitAlinhamento(ctx.parametros().alinhamento()) + '" ') \
                if ctx.parametros().alinhamento() is not None else ''

            if ctx.parametros().mais_parametros() is not None:
                if ctx.parametros().mais_parametros().parametros() is not None:
                    if cor == '':
                        cor = self.visitCor(ctx.parametros().mais_parametros().parametros().cor()) \
                            if ctx.parametros().mais_parametros().parametros().cor() is not None else ''
                    if alinhamento == '':
                        alinhamento = (' align="' +
                                       self.visitAlinhamento(ctx.parametros().mais_parametros().parametros().alinhamento())
                                       + '" ') if ctx.parametros().mais_parametros().parametros().alinhamento() \
                                                  is not None else ''

        titulo = ('<h1 #ALINHAMENTOclass="ui header#COR">' + self.visitCadeia(ctx.CADEIA()) + '</h1>\n') \
            if ctx.CADEIA() is not None else ''
        titulo = titulo.replace('#COR', cor)
        titulo = titulo.replace('#ALINHAMENTO', alinhamento)
        return titulo

    def visitSubtitulo(self, ctx: t3_cc2Parser.SubtituloContext):
        cor = ''
        alinhamento = ''

        if ctx.parametros() is not None:
            cor = self.visitCor(ctx.parametros().cor()) if ctx.parametros().cor() is not None else ''
            alinhamento = (' align="' + self.visitAlinhamento(ctx.parametros().alinhamento()) + '" ') \
                if ctx.parametros().alinhamento() is not None else ''

            if ctx.parametros().mais_parametros() is not None:
                if ctx.parametros().mais_parametros().parametros() is not None:
                    if cor == '':
                        cor = self.visitCor(ctx.parametros().mais_parametros().parametros().cor()) \
                            if ctx.parametros().mais_parametros().parametros().cor() is not None else ''
                    if alinhamento == '':
                        alinhamento = (' align="' +
                                       self.visitAlinhamento(ctx.parametros().mais_parametros().parametros().alinhamento())
                                       + '" ') if ctx.parametros().mais_parametros().parametros().alinhamento() \
                                                  is not None else ''

        subtitulo = ('<h2 #ALINHAMENTOclass="ui header#COR">' + self.visitCadeia(ctx.CADEIA()) + '</h2>') \
            if ctx.CADEIA() is not None else ''
        subtitulo = subtitulo.replace('#COR', cor)
        subtitulo = subtitulo.replace('#ALINHAMENTO', alinhamento)
        return subtitulo

    def visitTexto(self, ctx: t3_cc2Parser.TextoContext):
        return self.visitConteudo_texto(ctx.conteudo_texto()) \
            if ctx is not None and ctx.conteudo_texto() is not None else ''

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
        cor = ''
        alinhamento = ''

        if ctx.parametros() is not None:
            cor = (' class="' + self.visitCor(ctx.parametros().cor())[1:] + '"')\
                if ctx.parametros().cor() is not None else ''
            alinhamento = (' align="' + self.visitAlinhamento(ctx.parametros().alinhamento()) + '" ') \
                if ctx.parametros().alinhamento() is not None else ''

            if ctx.parametros().mais_parametros() is not None:
                if ctx.parametros().mais_parametros().parametros() is not None:
                    if cor == '':
                        cor = (' class="' + self.visitCor(ctx.parametros().mais_parametros().parametros().cor())[1:] + '"') \
                            if ctx.parametros().mais_parametros().parametros().cor() is not None else ''
                    if alinhamento == '':
                        alinhamento = (' align="' +
                                       self.visitAlinhamento(
                                           ctx.parametros().mais_parametros().parametros().alinhamento())
                                       + '" ') if ctx.parametros().mais_parametros().parametros().alinhamento() \
                                                  is not None else ''

        paragrafo = '#LINK' + ('<p#ALINHAMENTO#COR>' + self.visitCadeia(ctx.CADEIA()) + '</p>#FECHALINK') \
            if ctx.CADEIA() is not None else ''

        link = '\n<a href="' + self.visitLink(ctx.link()) + '"' + self.visitNova_aba(ctx.link().nova_aba()) + '>\n' \
            if ctx.link() is not None else ''
        fecha_link = '\n</a>' if ctx.link() is not None else ''

        paragrafo = paragrafo.replace('#LINK', link).replace('#FECHALINK', fecha_link)
        paragrafo = paragrafo.replace('#COR', cor)
        paragrafo = paragrafo.replace('#ALINHAMENTO', alinhamento)

        return paragrafo

    def visitImagem(self, ctx: t3_cc2Parser.ImagemContext):
        imagem = '#ALINHAMENTO_IMAGEM#LINK<img src="' + self.visitCadeia(ctx.CADEIA()).replace('"', '') + \
                 '" class="ui #TAMANHO_IMAGEM image">#FECHALINK#FECHA_ALINHAMENTO_IMAGEM' \
            if ctx.CADEIA() is not None else ''

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
            <div class="ui stackable equal width center aligned grid container">
                #TEXTO
                #COLUNAS
            </div>
        </div>
        """
        colunas = (self.visitColunas(ctx.colunas()) if ctx.colunas() is not None else '') + \
                  (self.visitColuna(ctx.coluna()) if ctx.coluna() is not None else '')

        novas_colunas = """<div class="middle aligned row">
                    #COLUNAS
                </div>

        """

        if colunas != '':
            rodape = rodape.replace('#COLUNAS', novas_colunas.replace('#COLUNAS', colunas))
        else:
            rodape = rodape.replace('#COLUNAS', '')

        nova_linha = """<div class="middle aligned row">
                        <div class="column">
                            #TEXTO
                        </div>
                    </div>
                """

        texto = self.visitTexto(ctx.texto()) if ctx.texto() is not None else ''

        if texto != '':
            rodape = rodape.replace('#TEXTO', nova_linha.replace('#TEXTO', texto))
        else:
            rodape = rodape.replace('#TEXTO', '')

        rodape = rodape.replace('header', 'inverted header')
        rodape = rodape.replace('<h1', '<h3').replace('</h1>', '</h3>').replace('<h2', '<h4').replace('</h2>', '</h4>')

        return rodape

    def visitFonte(self, ctx: t3_cc2Parser.FonteContext):
        return self.visitOpcao_fonte(ctx.opcao_fonte()) if ctx.opcao_fonte() is not None else ''

    def visitOpcao_fonte(self, ctx: t3_cc2Parser.Opcao_fonteContext):
        return ctx.getText()

    def visitCor(self, ctx: t3_cc2Parser.CorContext):
        return self.visitOpcao_cor(ctx.opcao_cor())

    def visitOpcao_cor(self, ctx: t3_cc2Parser.Opcao_corContext):
        return ' ' + ctx.getText()

    def visitTamanho(self, ctx: t3_cc2Parser.TamanhoContext):
        return self.visitOpcao_tamanho(ctx.opcao_tamanho())

    def visitOpcao_tamanho(self, ctx: t3_cc2Parser.Opcao_tamanhoContext):
        return ctx.getText()

    def visitAlinhamento(self, ctx: t3_cc2Parser.AlinhamentoContext):
        return self.visitOpcao_alinhamento(ctx.opcao_alinhamento())

    def visitOpcao_alinhamento(self, ctx: t3_cc2Parser.Opcao_alinhamentoContext):
        alinhamento = ctx.getText()

        if alinhamento == 'esquerda':
            alinhamento = 'left'
        elif alinhamento == 'centralizado':
            alinhamento = 'center'
        elif alinhamento == 'direita':
            alinhamento = 'right'

        return alinhamento

    def getCodigo(self):
        return self.codigo
