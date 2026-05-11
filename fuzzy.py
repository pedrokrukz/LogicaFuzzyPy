from InquirerPy import prompt
from fuzzywuzzy import process

CIDADES = [
    "São Paulo",
    "Rio de Janeiro",
    "Belo Horizonte",
    "Curitiba",
    "Porto Alegre"
]

def buscar_cidade(nome_cidade):
    if not nome_cidade.strip():
        return None

    resultado = process.extractOne(nome_cidade, CIDADES)
    return resultado

def main():
    while True:
        pergunta = [{
            "type": "input",
            "name": "cidade",
            "message": "Digite o nome de uma cidade:"
        }]

        resposta = prompt(pergunta)

        cidade_digitada = resposta["cidade"].strip()

        resultado = buscar_cidade(cidade_digitada)

        if resultado:
            cidade_encontrada, porcentagem = resultado

            if porcentagem >= 60:

                pergunta_confirmacao = [{
                    "type": "confirm",
                    "name": "confirmacao",
                    "message": f"Você quis dizer '{cidade_encontrada}' ({porcentagem}% similar)",
                    "default": True
                }]

                resposta_confirmacao = prompt(pergunta_confirmacao)

                if resposta_confirmacao["confirmacao"]:
                    print(f"Você selecionou: {cidade_encontrada}")
                    break
                else:
                    print("Vamos tentar novamente.\n")

            else:
                print("Cidade não encontrada.\n")

        else:
            print("Nenhuma cidade encontrada. Tente novamente.\n")

if __name__ == "__main__":
    main()
