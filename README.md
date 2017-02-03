# Construção de Compiladores 2 - Trabalho 3

**UNIVERSIDADE FEDERAL DE SÃO CARLOS**<br>
Centro de Ciências Exatas e de Tecnologia<br>
Departamento de Computação<br>
Construço de Compiladores 2 - Semestre 2016/2<br>
Prof.ª Dr.ª Helena Caseli e Prof. Dr. Daniel Lucrédio

## Descrição do trabalho

O terceiro e último trabalho prático da disciplina consiste na implementação de um compilador completo para a linguagem especificada no Trabalho 2. O compilador deve, portanto, possui analisador léxico e sintático, analisador semântico e realizar geração de código ou interpretação.

Como ferramenta de auxílio para a construção do compilador, utilizaremos o gerador automático ANTLR versão 4.6. Como linguagem de programação, utilizaremos Python 3.

## Definição da linguagem

A linguagem definida para a construço deste compilador é uma linguagem capaz de criar websites de forma simplificada. Os websites criados são automaticamente responsivos e a sintaxe da linguagem bem simples. A seguir, a estrutura básica:

```
# comentário
site(titulo="Título do site", fonte=Open Sans) {
  menu {
    item("texto do menu") -> "link do menu"
    item("texto do menu") ->+ "link do menu que abre em nova guia"
  }
  sidebar = menu
  banner(fundo=imagem("local da imagem)) {
    texto {
      titulo("Título do banner")
      subtitulo("Subtítulo do banner")
    }
  }
  conteudo {
    secao {
      coluna {
        texto {
          titulo(cor=azul-claro, alinhamento=centralizado)("Título da seção")
          subtitulo(alinhamento=centralizado)("Subtítulo da seção")
        }
      }
    }
    secao {
      colunas {
        coluna {
          imagem("local da imagem")
        }
        coluna {
          texto {
            titulo("Título")
            paragrafo(alinhamento=direita)("Texto do parágrafo")
          }
        }
      } 
    }
  }
  rodape {
    titulo("...")
  }
}
```

### Componentes da linguagem

#### site

- Parâmetros `titulo` e `fonte` opcionais. Caso deixados em branco, título será vazio e fonte padrão será Lato.
- Fontes atualmente suportadas: `Arial`, `Helvetica`, `Lato`, `Open Sans`, `Roboto` e `Times New Roman`.

#### menu

- Não suporta parâmetros.
- Conjunto de itens.


#### itens

- Único parâmetro é o texto do item de menu.
- Links são opcionais. Link diretos são indicados por `-> "link"` e links que abrem em uma nova guia por `->+ "link"`.

#### sidebar

- Não suporta parâmetros.
- Conjunto de itens.
- Caso o conjunto de itens seja igual ao do menu, é permitido o uso do atalho `sidebar=menu`, contanto que um menu tenha sido declarado.

#### banner

- Parâmetro `fundo` opcional, que aceita imagem (sem links) ou cores. Sintaxe: `banner(fundo=imagem("local da imagem"))` ou `banner(fundo=cor=nomedacor)`. Se não forem especificados parâmetros, o padrão é `fundo=cor=preto`.
- Cores atualmente suportadas: `azul`, `verde`, `amarelo`, `branco`, `preto`, `vermelho`, `laranja`, `roxo`, `rosa`, `cinza`, `marrom` e `azul-claro`.

...texto em desenvolvimento


## Configuração do ambiente para executar o projeto

O projeto deste repositório é um projeto do PyCharm. Está sendo utilizada a versão 2016.3 do PyCharm. 

Para funcionar adequadamente, é necessária a instalação do plugin `ANTLR v4 grammar plugin` versão 1.8.2.

### Como instalar o plugin do ANTLR

#### macOS Sierra
Menu PyCharm -> Preferences... -> Plugins

#### Ubuntu ou outras distribuições Linux

Menu File -> Settings... -> Plugins
