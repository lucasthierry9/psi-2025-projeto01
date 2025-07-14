from django.shortcuts import render

def inicio(request):
    return render(request, "website/inicio.html")

elenco_vasco = [
        {"id": 1 ,"nome": "Léo Jardim", "idade": "30 anos", "numero": 1, "posicao": "Goleiro", "localnascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/1.png"},
        {"id": 2 ,"nome": "Daniel Fuzato", "idade": "28 anos", "numero": 13, "posicao": "Goleiro", "localnascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/13.png"},
        {"id": 3 ,"nome": "Pablo", "idade": "22 anos", "numero": 37, "posicao": "Goleiro", "localnascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/37.png"},
        {"id": 4 ,"nome": "Puma Rodríguez", "idade": "28 anos", "numero": 2, "posicao": "Lateral Direito", "localnascimento": "São Paulo, Uruguai.", "imagem": "website/img/fotos_elenco/2.png"},
        {"id": 5 ,"nome": "Paulinho", "idade": "20 anos", "numero": 22, "posicao": "Lateral Direito", "localnascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/22.png"},
        {"id": 6 ,"nome": "Paulo Henrique", "idade": "28 anos", "numero": 96, "posicao": "Lateral Direito", "localnascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/96.png"},
        {"id": 7 ,"nome": "Riquelme", "idade": "22 anos", "numero": 66, "posicao": "Lateral Esquerdo", "localnascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/66.png"},
        {"id": 8,"nome": "Lucas Piton", "idade": "24 anos", "numero": 6, "posicao": "Lateral Esquerdo", "localnascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/6.png"},
        {"id": 9,"nome": "Victor Luís", "idade": "32 anos", "numero": 12, "posicao": "Lateral Esquerdo", "localnascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/12.png"},
        {"id": 10,"nome": "Lucas Freitas", "idade": "24 anos", "numero": 43, "posicao": "Zagueiro", "localnascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/43.png"},
        {"id": 11,"nome": "Lucas Oliveira", "idade": "29 anos", "numero": 29, "posicao": "Zagueiro", "localnascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/29.png"},
        {"id": 12,"nome": "João Victor", "idade": "30 anos", "numero": 38, "posicao": "Zagueiro", "localnascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/38.png"},
        {"id": 13,"nome": "Luiz Gustavo", "idade": "26 anos", "numero": 44, "posicao": "Zagueiro", "localnascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/44.png"},
        {"id": 14,"nome": "Mauricio Lemos", "idade": "29 anos", "numero": 4, "posicao": "Zagueiro", "localnascimento": "São Paulo, Uruguai.", "imagem": "website/img/fotos_elenco/4.png"},
        {"id": 15,"nome": "Tchê Tchê", "idade": "32 anos", "numero": 3, "posicao": "Volante", "localnascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/3.png"},
        {"id": 16,"nome": "Juan Sforza", "idade": "23 anos", "numero": 20,"posicao": "Volante", "localnascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/20.png"},
        {"id": 17,"nome": "Jair", "idade": "30 anos", "numero": 8, "posicao": "Volante", "localnascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/8.png"},
        {"id": 18,"nome": "Paulinho", "idade": "28 anos", "numero": 18, "posicao": "Volante", "localnascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/18.png"},
        {"id": 19,"nome": "Hugo Moura", "idade": "27 anos", "numero": 25, "posicao": "Volante", "localnascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/25.png"},
        {"id": 20,"nome": "Coutinho", "idade": "33 anos", "numero": 10, "posicao": "Meia", "localnascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/10.png"},
        {"id": 21,"nome": "Estrella", "idade": "20 anos", "numero": 14, "posicao": "Meia", "localnascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/14.png"},
        {"id": 22,"nome": "Alex Teixeira", "idade": "35 anos", "numero": 90, "posicao": "Meia", "localnascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/90.png"},
        {"id": 23,"nome": "Nuno Moreira", "idade": "26 anos", "numero": 17, "posicao": "Atacante", "localnascimento": "São Paulo, Portugal.", "imagem": "website/img/fotos_elenco/17.png"},
        {"id": 24,"nome": "Garré", "idade": "24 anos", "numero": 15, "posicao": "Atacante", "localnascimento": "São Paulo, Argentina.", "imagem": "website/img/fotos_elenco/15.png"},
        {"id": 25,"nome": "Loide Augusto", "idade": "25 anos", "numero": 45, "posicao": "Atacante", "localnascimento": "São Paulo, Angola.", "imagem": "website/img/fotos_elenco/45.png"},
        {"id": 26,"nome": "Jean David", "idade": "32 anos", "numero": 21, "posicao": "Atacante", "localnascimento": "São Paulo, Chile.", "imagem": "website/img/fotos_elenco/21.png"},
        {"id": 27,"nome": "David", "idade": "29 anos", "numero": 7, "posicao": "Atacante", "localnascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/7.png"},
        {"id": 28,"nome": "Adson", "idade": "24 anos", "numero": 28, "posicao": "Atacante", "localnascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/28.png"},
        {"id": 29,"nome": "Rayan", "idade": "18 anos", "numero": 77, "posicao": "Atacante", "localnascimento": "Rio de Janeiro, Brasil.", "imagem": "website/img/fotos_elenco/77.png"},
        {"id": 30,"nome": "Vegetti", "idade": "36 anos", "numero": 99, "posicao": "Atacante", "localnascimento": "São Paulo, Argentina.", "imagem": "website/img/fotos_elenco/99.png"},
    ]

def elenco(request):
    context = {
        "elenco_vasco": elenco_vasco,
    }
    return render(request, "website/elenco.html", context)

def jogador(request, id_jogador):
    return render(request, "website/jogador.html", elenco_vasco[id_jogador-1])

def sobre(request):
    return render(request, "website/sobre.html")
