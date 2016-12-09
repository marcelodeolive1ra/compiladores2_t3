from antlr4 import *
from ANTLR.t3_cc2Visitor import *
from ANTLR.t3_cc2Parser import *

class Intepretador(t3_cc2Visitor):

    codigo = ""

    def visitSite(self, ctx: t3_cc2Parser.SiteContext):
        self.codigo += "<html>"
        self.visitBanner_principal(ctx.banner())


    def visitBanner_principal(self, ctx: t3_cc2Parser.BannerContext):
        self.codigo += "banner"
        self.visitTitulo(ctx.titulo())

    def visitTitulo(self, ctx: t3_cc2Parser.TituloContext):
        self.codigo += str(ctx.getText())


    def getCodigo(self):
        return self.codigo
