from django.shortcuts import render

def inicio(request):
    return render(request, "website/inicio.html")

elenco_vasco = [
        {"nome": "Léo Jardim", "idade": 30, "posição": "Goleiro", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Daniel Fuzato", "idade": 28, "posição": "Goleiro", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Pablo", "idade": 22, "posição": "Goleiro", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Puma Rodríguez", "idade": 28, "posição": "Lateral Direito", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Paulinho", "idade": 20, "posição": "Lateral Direito", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Paulo Henrique", "idade": 28, "posição": "Lateral Direito", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Riquelme", "idade": 22, "posição": "Lateral Esquerdo", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Leandrinho", "idade": 20, "posição": "Lateral Esquerdo", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Lucas Piton", "idade": 24, "posição": "Lateral Esquerdo", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Victor Luís", "idade": 32, "posição": "Lateral Esquerdo", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Lucas Freitas", "idade": 24, "posição": "Zagueiro", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Lucas Oliveira", "idade": 29, "posição": "Zagueiro", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "João Victor", "idade": 30, "posição": "Zagueiro", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Luiz Gustavo", "idade": 26, "posição": "Zagueiro", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Mauricio Lemos", "idade": 29, "posição": "Zagueiro", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Tchê Tchê", "idade": 32, "posição": "Volante", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Juan Sforza", "idade": 23, "posição": "Volante", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Jair", "idade": 30, "posição": "Volante", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Paulinho", "idade": 28, "posição": "Volante", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Hugo Moura", "idade": 27, "posição": "Volante", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Coutinho", "idade": 33, "posição": "Meia", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Estrella", "idade": 20, "posição": "Meia", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Alex Teixeira", "idade": 35, "posição": "Meia", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Nuno Moreira", "idade": 26, "posição": "Atacante", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Garré", "idade": 24, "posição": "Atacante", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Loide Augusto", "idade": 25, "posição": "Atacante", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Jean David", "idade": 32, "posição": "Atacante", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "David", "idade": 29, "posição": "Atacante", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Adson", "idade": 24, "posição": "Atacante", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Rayan", "idade": 18, "posição": "Atacante", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
        {"nome": "Vegetti", "idade": 36, "posição": "Atacante", "local de nascimento": "São Paulo, Brasil.", "imagem": "post-bg.jpg"},
    ]

def elenco(request):
    context = {
        "elenco_vasco": elenco_vasco,
    }
    return render(request, "website/elenco.html", context)

def sobre(request):
    return render(request, "website/sobre.html")
