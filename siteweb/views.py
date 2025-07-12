from django.shortcuts import render

def inicio(request):
    return render(request, "website/inicio.html")

elenco_vasco = [
        {"id": 1 ,"nome": "Léo Jardim", "idade": 30, "numero": 1, "posicao": "Goleiro", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/1.png"},
        {"id": 2 ,"nome": "Daniel Fuzato", "idade": 28, "numero": 13, "posicao": "Goleiro", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/13.png"},
        {"id": 3 ,"nome": "Pablo", "idade": 22, "numero": 37, "posicao": "Goleiro", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/37.png"},
        {"id": 4 ,"nome": "Puma Rodríguez", "idade": 28, "numero": 2, "posicao": "Lateral Direito", "local de nascimento": "São Paulo, Uruguai.", "imagem": "website/img/fotos_elenco/2.png"},
        {"id": 5 ,"nome": "Paulinho", "idade": 20, "numero": 22, "posicao": "Lateral Direito", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/22.png"},
        {"id": 6 ,"nome": "Paulo Henrique", "idade": 28, "numero": 96, "posicao": "Lateral Direito", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/96.png"},
        {"id": 7 ,"nome": "Riquelme", "idade": 22, "numero": 66, "posicao": "Lateral Esquerdo", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/66.png"},
        {"id": 8 ,"nome": "Leandrinho", "idade": 20, "numero": 67, "posicao": "Lateral Esquerdo", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/66.png"},
        {"id": 9,"nome": "Lucas Piton", "idade": 24, "numero": 6, "posicao": "Lateral Esquerdo", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/6.png"},
        {"id": 10,"nome": "Victor Luís", "idade": 32, "numero": 12, "posicao": "Lateral Esquerdo", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/12.png"},
        {"id": 11,"nome": "Lucas Freitas", "idade": 24, "numero": 43, "posicao": "Zagueiro", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/43.png"},
        {"id": 12,"nome": "Lucas Oliveira", "idade": 29, "numero": 29, "posicao": "Zagueiro", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/29.png"},
        {"id": 13,"nome": "João Victor", "idade": 30, "numero": 38, "posicao": "Zagueiro", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/38.png"},
        {"id": 14,"nome": "Luiz Gustavo", "idade": 26, "numero": 44, "posicao": "Zagueiro", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/44.png"},
        {"id": 15,"nome": "Mauricio Lemos", "idade": 29, "numero": 4, "posicao": "Zagueiro", "local de nascimento": "São Paulo, Uruguai.", "imagem": "website/img/fotos_elenco/4.png"},
        {"id": 16,"nome": "Tchê Tchê", "idade": 32, "numero": 3, "posicao": "Volante", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/3.png"},
        {"id": 17,"nome": "Juan Sforza", "idade": 23, "numero": 20,"posicao": "Volante", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/20.png"},
        {"id": 18,"nome": "Jair", "idade": 30, "numero": 8, "posicao": "Volante", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/8.png"},
        {"id": 19,"nome": "Paulinho", "idade": 28, "numero": 18, "posicao": "Volante", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/18.png"},
        {"id": 20,"nome": "Hugo Moura", "idade": 27, "numero": 25, "posicao": "Volante", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/25.png"},
        {"id": 21,"nome": "Coutinho", "idade": 33, "numero": 10, "posicao": "Meia", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/10.png"},
        {"id": 22,"nome": "Estrella", "idade": 20, "numero": 14, "posicao": "Meia", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/14.png"},
        {"id": 23,"nome": "Alex Teixeira", "idade": 35, "numero": 90, "posicao": "Meia", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/90.png"},
        {"id": 24,"nome": "Nuno Moreira", "idade": 26, "numero": 17, "posicao": "Atacante", "local de nascimento": "São Paulo, Portugal.", "imagem": "website/img/fotos_elenco/17.png"},
        {"id": 25,"nome": "Garré", "idade": 24, "numero": 15, "posicao": "Atacante", "local de nascimento": "São Paulo, Argentina.", "imagem": "website/img/fotos_elenco/15.png"},
        {"id": 26,"nome": "Loide Augusto", "idade": 25, "numero": 45, "posicao": "Atacante", "local de nascimento": "São Paulo, Angola.", "imagem": "website/img/fotos_elenco/45.png"},
        {"id": 27,"nome": "Jean David", "idade": 32, "numero": 21, "posicao": "Atacante", "local de nascimento": "São Paulo, Chile.", "imagem": "website/img/fotos_elenco/21.png"},
        {"id": 28,"nome": "David", "idade": 29, "numero": 7, "posicao": "Atacante", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/7.png"},
        {"id": 29,"nome": "Adson", "idade": 24, "numero": 28, "posicao": "Atacante", "local de nascimento": "São Paulo, Brasil.", "imagem": "website/img/fotos_elenco/28.png"},
        {"id": 30,"nome": "Rayan", "idade": 18, "numero": 77, "posicao": "Atacante", "local de nascimento": "Rio de Janeiro, Brasil.", "imagem": "website/img/fotos_elenco/77.png"},
        {"id": 31,"nome": "Vegetti", "idade": 36, "numero": 99, "posição": "Atacante", "local de nascimento": "São Paulo, Argentina.", "imagem": "website/img/fotos_elenco/99.png"},
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
