candidatos = [ 
    ['candidato 1', 'e5_t10_p8_s8'],
    ['candidato 2', 'e10_t7_p7_s8'],
    ['candidato 3', 'e8_t5_p4_s9'],
    ['candidato 4', 'e2_t2_p2_s1'],
    ['candidato 5', 'e10_t10_p8_s9'],
]

def adicionarNovoCandidato(nomeCadidato, nota_entrevista, nota_teste_teórico, nota_teste_prático, nota_soft_skills):
    resultado = f"e{nota_entrevista}_t{nota_teste_teórico}_p{nota_teste_prático}_s{nota_soft_skills}"
    candidatos.append({"nome": nomeCadidato, "resultado": resultado})
    return resultado

def filtrarCandidatos(candidatos, nota_min_entrevista, nota_min_teorico, nota_min_pratico, nota_min_soft):
    candidatosSelecionados = []
    for candidato, resultado in candidatos:
        notas = resultado.split('_')
        e = int(notas[0][1:])
        t = int(notas[1][1:])
        p = int(notas[2][1:])
        s = int(notas[3][1:])
        if e >= nota_min_entrevista and t >= nota_min_teorico and p >= nota_min_pratico and s >= nota_min_soft:
            candidatosSelecionados.append(candidato)
    return candidatosSelecionados

opcao = -1

while opcao != 0:
    opcao = int(input(f'''
    ########### MENU DE OPÇÕES DEU MATCH!  ############
            [1] - BUSCAR UM CANDIDATO
            [2] - ADICIONAR NOVO CADIDATO
            [3] - MOSTRAR O BANCO DE CANDIDATOS                 
            [0] - SAIR
    ###################################################                            
    '''))

    if opcao == 1:
        nota_min_entrevista = int(input("Qual a nota mínima necessária na entrevista? [e] :")) 
        nota_min_teorico = int(input("Qual a nota mínima necessária no teste teórico? [t] :"))   
        nota_min_pratico = int(input("Qual a nota mínima necessária no teste prático? [p] :")) 
        nota_min_soft = int(input("Qual a nota mínima necessária em soft skills? [s] :"))         

        candidatosSelecionados = filtrarCandidatos(candidatos, nota_min_entrevista, nota_min_teorico, nota_min_pratico, nota_min_soft)

        if candidatosSelecionados:
            print("Candidatos selecionados com base nas notas minimas informadas: ")
            for candidato in candidatosSelecionados:
                print(candidato)
        else:
            print("Não existem candidatos com notas suficientes para a vaga!")
             
    elif opcao == 2:
        nomeCadidato = input("Digite o nome do candidato: ")
        nota_entrevista = int(input("Digite a nota do candidato na entrevista: "))
        nota_teste_teórico = int(input("Digite a nota do candidato no teste teórico: "))
        nota_teste_prático = int(input("Digite a nota do candidato no teste prático: "))
        nota_soft_skills = int(input("Digite a nota do candidato na avaliação de soft skills: "))

        print(f"O candidato {nomeCadidato} com a pontuação {adicionarNovoCandidato(nomeCadidato, nota_entrevista, nota_teste_teórico, nota_teste_prático, nota_soft_skills)} foi adicionado com Sucesso!")
    elif opcao == 3:
        print('Esse é o banco de candidatos cadastrados')
        print(candidatos)
    elif opcao == 0:
        print("O sistema foi encerrado, obrigado por usar meu app...")
    else:
        print("A opção escolhida é invalida! Por favor escolha umas das opções abaixo:")
