grammar t3_cc2;

CADEIA:
    '"' ~('\n' | '\r' | '"')* '"';

COMENTARIO:
    '//' ~('/'|'\n')* '//' -> skip
;

ESPACO:
    ( ' ' |'\t' | '\r' | '\n') -> skip
;

site:
	'site' '{' CADEIA '}' '{' menu sidebar banner conteudo rodape '}';

titulo:
	'titulo' '{' CADEIA '}';

menu:
	'menu' '{' (item)+ '}';

item:
	CADEIA link mais_itens;

link:
    'link' ':' CADEIA | ;

mais_itens:
	item | ;

sidebar:
	'sidebar' '{' (item)+ '}' | ;

banner:
	'banner' '{' imagem	titulo subtitulo '}';

subtitulo:
	'subtitulo' '{' CADEIA '}';

rodape:
	titulo subtitulo;

conteudo:
	secao mais_secoes | ;

secao:
	'uma_coluna' '{' uma_coluna '}'
	| 'duas_colunas' '{' duas_colunas '}'
	| 'tres_colunas' '{' tres_colunas '}'
	| 'linha' '{' linha '}';

uma_coluna:
	coluna;

duas_colunas:
	coluna coluna;

tres_colunas:
    coluna coluna coluna;

coluna:
    imagem | titulo subtitulo texto;

linha:
    imagem | titulo subtitulo texto;

texto:
	CADEIA | ;

uma_coluna_texto_uma_imagem:
	coluna imagem;

uma_coluna_imagem_uma_texto:
	imagem coluna;

uma_coluna_texto:
	coluna;

uma_linha_texto:
	linha;

imagem:
	'imagem' '{' CADEIA '}';

mais_secoes:
	secao | ;