# primeiro devo criar um processo de automatização da criacao de conta
#segundo devo criar uma automatização do tutorial
# depois criar automacoes especificas

#calibra o bot( faz andar da direcao inicial(algum canto) ate o ponto antes de comecar o loop)


#Primeiro exemplo: https://www.kaggle.com/dansbecker/how-models-work
#Criar funcao recursiva que para cadeia que entrar, ele enviar um vetor de perguntas, o indice e o vetor de respostas sim ou nao


per = [3, 4, 3, 1, 2, 3, 6, 7, 8, 4, 5, 2, 1]

#13 vals

def respTrueOrFalse(perguntas, respostas = [], indice = 0):
    #Utilizar em arvore de decisao para dois valores, ou ate mais
    if perguntas[indice] > 3:
        respostas.append(True)
    else:
        respostas.append(False)   
    if len(perguntas) - 1 != indice:
        return respTrueOrFalse(perguntas, respostas, indice + 1)
  
    return respostas
    

def main():
    print(respTrueOrFalse(per))
    pass


if __name__ == "__main__":
    main()