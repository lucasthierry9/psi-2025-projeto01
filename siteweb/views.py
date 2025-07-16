from django.shortcuts import render

elenco_vasco = [
        {"id": 1 ,"nome": "Léo Jardim", "idade": "30 anos", "numero": 1, "posicao": "Goleiro", "localnascimento": "Ribeirão Preto, SP.", "altura": "1,88 m", "gols": 0, "assist": 0, "imagem": "website/img/fotos_elenco/1.png"},
        {"id": 2 ,"nome": "Daniel Fuzato", "idade": "28 anos", "numero": 13, "posicao": "Goleiro", "localnascimento": "Santa Bárbara d´Oeste, SP.", "altura": "1,90 m", "gols": 0, "assist": 0, "imagem": "website/img/fotos_elenco/13.png"},
        {"id": 3 ,"nome": "Pablo", "idade": "22 anos", "numero": 37, "posicao": "Goleiro", "localnascimento": "Volta Redonda, RJ.", "altura": "1,88 m", "gols": 0, "assist": 0, "imagem": "website/img/fotos_elenco/37.png"},
        {"id": 4 ,"nome": "Puma Rodríguez", "idade": "28 anos", "numero": 2, "posicao": "Lateral Direito", "localnascimento": "Canelones, Uruguai.", "altura": "1,83 m", "gols": 6, "assist": 6, "imagem": "website/img/fotos_elenco/2.png"},
        {"id": 5 ,"nome": "Paulinho", "idade": "20 anos", "numero": 22, "posicao": "Lateral Direito", "localnascimento": "Tefé, Amazonas.", "altura": "1,75 m", "gols": 1, "assist": 0, "imagem": "website/img/fotos_elenco/22.png"},
        {"id": 6 ,"nome": "Paulo Henrique", "idade": "28 anos", "numero": 96, "posicao": "Lateral Direito", "localnascimento": "Sete Barras, SP.", "altura": "1,75 m", "gols": 5, "assist": 6, "imagem": "website/img/fotos_elenco/96.png"},
        {"id": 7 ,"nome": "Riquelme", "idade": "22 anos", "numero": 66, "posicao": "Lateral Esquerdo", "localnascimento": "Barra Mansa RJ.", "altura": "1,73 m", "gols": 0, "assist": 5, "imagem": "website/img/fotos_elenco/66.png"},
        {"id": 8,"nome": "Lucas Piton", "idade": "24 anos", "numero": 6, "posicao": "Lateral Esquerdo", "localnascimento": "Jundiaí, SP.", "altura": "1,75 m", "gols": 7, "assist": 21, "imagem": "website/img/fotos_elenco/6.png"},
        {"id": 9,"nome": "Victor Luís", "idade": "32 anos", "numero": 12, "posicao": "Lateral Esquerdo", "localnascimento": "São Paulo, SP.", "altura": "1,77 m", "gols": 1, "assist": 1, "imagem": "website/img/fotos_elenco/12.png"},
        {"id": 10,"nome": "Lucas Freitas", "idade": "24 anos", "numero": 43, "posicao": "Zagueiro", "localnascimento": "Rio de Janeiro, RJ.", "altura": "1,84 m", "gols": 0, "assist": 1, "imagem": "website/img/fotos_elenco/43.png"},
        {"id": 11,"nome": "Lucas Oliveira", "idade": "29 anos", "numero": 29, "posicao": "Zagueiro", "localnascimento": "Rio de Janeiro, RJ.", "altura": "1,87 m", "gols": 0, "assist": 0, "imagem": "website/img/fotos_elenco/29.png"},
        {"id": 12,"nome": "João Victor", "idade": "30 anos", "numero": 38, "posicao": "Zagueiro", "localnascimento": "Bauru, SP.", "altura": "1,87 m", "gols": 3, "assist": 2, "imagem": "website/img/fotos_elenco/38.png"},
        {"id": 13,"nome": "Luiz Gustavo", "idade": "19 anos", "numero": 44, "posicao": "Zagueiro", "localnascimento": "Itaboraí, RJ.", "altura": "1,88 m", "gols": 0, "assist": 0, "imagem": "website/img/fotos_elenco/44.png"},
        {"id": 14,"nome": "Mauricio Lemos", "idade": "29 anos", "numero": 4, "posicao": "Zagueiro", "localnascimento": "Rivera, Uruguai.", "altura": "1,87 m", "gols": 0, "assist": 0, "imagem": "website/img/fotos_elenco/4.png"},
        {"id": 15,"nome": "Tchê Tchê", "idade": "32 anos", "numero": 3, "posicao": "Volante", "localnascimento": "São Paulo, SP.", "altura": "1,75 m", "gols": 0, "assist": 4, "imagem": "website/img/fotos_elenco/3.png"},
        {"id": 16,"nome": "Juan Sforza", "idade": "23 anos", "numero": 20,"posicao": "Volante", "localnascimento": "Rosario, Argentina.", "altura": "1,79 m", "gols": 1, "assist": 1, "imagem": "website/img/fotos_elenco/20.png"},
        {"id": 17,"nome": "Jair", "idade": "30 anos", "numero": 8, "posicao": "Volante", "localnascimento": "Ibirubá, RS.", "altura": "1,78 m", "gols": 5, "assist": 0, "imagem": "website/img/fotos_elenco/8.png"},
        {"id": 18,"nome": "Paulinho", "idade": "28 anos", "numero": 18, "posicao": "Volante", "localnascimento": "Rio de Janeiro, RJ.", "altura": "1,73 m", "gols": 2, "assist": 3, "imagem": "website/img/fotos_elenco/18.png"},
        {"id": 19,"nome": "Hugo Moura", "idade": "27 anos", "numero": 25, "posicao": "Volante", "localnascimento": "São Paulo, Brasil.", "altura": "1,75 m", "gols": 3, "assist": 7, "imagem": "website/img/fotos_elenco/85.png"},
        {"id": 20,"nome": "Mateus Carvalho", "idade": "23 anos", "numero": 85, "posicao": "Volante", "localnascimento": "Tucuruí, PA.", "altura": "1,84 m", "gols": 2, "assist": 2, "imagem": "website/img/fotos_elenco/25.png"},
        {"id": 21,"nome": "Coutinho", "idade": "33 anos", "numero": 10, "posicao": "Meia", "localnascimento": "Rio de Janeiro, RJ.", "altura": "1,72 m", "gols": 13, "assist": 14, "imagem": "website/img/fotos_elenco/10.png"},
        {"id": 22,"nome": "Estrella", "idade": "20 anos", "numero": 14, "posicao": "Meia", "localnascimento": "São Paulo, Brasil.", "altura": "1,76 m", "gols": 1, "assist": 0, "imagem": "website/img/fotos_elenco/14.png"},
        {"id": 23,"nome": "Alex Teixeira", "idade": "35 anos", "numero": 90, "posicao": "Meia", "localnascimento": "Duque de Caxias, RJ.", "altura": "1,74 m", "gols": 21, "assist": 8, "imagem": "website/img/fotos_elenco/90.png"},
        {"id": 24,"nome": "Nuno Moreira", "idade": "26 anos", "numero": 17, "posicao": "Atacante", "localnascimento": "Espinho, Portugal.", "altura": "1,75 m", "gols": 5, "assist": 2, "imagem": "website/img/fotos_elenco/17.png"},
        {"id": 25,"nome": "Garré", "idade": "24 anos", "numero": 15, "posicao": "Atacante", "localnascimento": "Buenos Aires, Argentina.", "altura": "1,72 m", "gols": 0, "assist": 1, "imagem": "website/img/fotos_elenco/15.png"},
        {"id": 26,"nome": "Loide Augusto", "idade": "25 anos", "numero": 45, "posicao": "Atacante", "localnascimento": "Luanda, Angola.", "altura": "1,83 m", "gols": 0, "assist": 0, "imagem": "website/img/fotos_elenco/45.png"},
        {"id": 27,"nome": "Jean David", "idade": "32 anos", "numero": 21, "posicao": "Atacante", "localnascimento": "Quillota, Chile.", "altura": "1,63 m", "gols": 0, "assist": 0, "imagem": "website/img/fotos_elenco/21.png"},
        {"id": 28,"nome": "David", "idade": "29 anos", "numero": 7, "posicao": "Atacante", "localnascimento": "São Paulo, Brasil.", "altura": "1,75 m", "gols": 7, "assist": 4, "imagem": "website/img/fotos_elenco/7.png"},
        {"id": 29,"nome": "Adson", "idade": "24 anos", "numero": 28, "posicao": "Atacante", "localnascimento": "São Paulo, Brasil.", "altura": "1,75 m", "gols": 4, "assist": 1, "imagem": "website/img/fotos_elenco/28.png"},
        {"id": 30,"nome": "Rayan", "idade": "18 anos", "numero": 77, "posicao": "Atacante", "localnascimento": "Rio de Janeiro, Brasil.", "altura": "1,75 m", "gols": 9, "assist": 2, "imagem": "website/img/fotos_elenco/77.png"},
        {"id": 31,"nome": "Vegetti", "idade": "36 anos", "numero": 99, "posicao": "Atacante", "localnascimento": "São Paulo, Argentina.", "altura": "1,87 m", "gols": 52, "assist": 7, "imagem": "website/img/fotos_elenco/99.png"},
    ]

noticias_vasco = [
    {"id": 1, "titulo": "REFORÇO!", "subtitulo": "Vasco acerta a contratação do volante Thiago Mendes", "data": "14 de junho de 2025", "categoria": "Contratações", "imagem": "website/img/WhatsApp-Image-2025-07-09-at-13.01.00-1320x550.jpeg",
     "texto": "O Vasco da Gama acertou a contratação do seu nono reforço para 2025: o volante Thiago Mendes, de 33 anos. O jogador desembarcou no Rio de Janeiro na noite da última terça-feira (8), realizou exames médicos, foi aprovado e assinou contrato com o Gigante da Colina até dezembro de 2027.\n"
     "\n"
     "– Eu queria voltar ao futebol brasileiro para sentir a energia do torcedor. O treinador falou muito bem do projeto e isso foi fundamental para vestir a camisa do Vasco. Estou ansioso para estrear, a torcida do Vasco inflama. Espero dar alegria ao torcedor – disse Thiago Mendes em entrevista exclusiva à Vasco TV.\n"
     "\n"
     "Natural de São Luís, no Maranhão, Thiago Mendes iniciou a carreira no Goiás. Em 2015, foi contratado pelo São Paulo, onde teve grande destaque e foi vendido ao Lille (FRA). Da lá, seguiu no futebol francês, onde também defendeu o Lyon (FRA). Nas duas últimas temporadas, defendeu a camisa do Al-Rayyan (QAT)."},
]

sobre_site = [
    {"titulo": "Sobre este Site", 
     "conteudo": "Este site foi criado para reunir tudo sobre o Vasco da Gama em um só lugar: notícias atualizadas, informações sobre o elenco, jogos, estatísticas e muito mais, e adquirir prática e conhecimento sobre o desenvolvimento de sites utilizando ferramentas como o framework Django."},

    {"titulo": "Sobre o Autor", 
     "conteudo": "Desenvolvedor: Lucas Thierry Araújo Vicente\n"
     "Email: lucasthierry092@gmail.com"},

    {"titulo": "Créditos", 
     "conteudo": "Todas as imagens, dados estatísticos e demais recursos visuais utilizados são de domínio público ou retirados da internet, sendo utilizados com fim exclusivamente educacional. Os direitos autorais pertencem aos seus respectivos criadores e detentores."},

     {"titulo": "Contato", 
     "conteudo": "Email: contato@vascodagama.com\n"
     "Redes Socias: @vascodagama"},
]

def inicio(request):
     context = {
        "noticias_vasco": noticias_vasco,
    }
     return render(request, "website/inicio.html", context)

def elenco(request):
    context = {
        "elenco_vasco": elenco_vasco,
    }
    return render(request, "website/elenco.html", context)

def jogador(request, id_jogador):
    return render(request, "website/jogador.html", elenco_vasco[id_jogador-1])

def noticia(request, id_noticia):
    return render(request, "website/noticias.html", noticias_vasco[id_noticia-1])

def sobre(request):
    context = {
        "sobre_site": sobre_site,
    }
    return render(request, "website/sobre.html", context)
