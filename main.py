#Montando uma main interativa para o código

from def_selecao import selecao_roleta, selecao_torneio
from def_elitismos import elitismo_simples, elitismo_composto
from def_mutacoes import mutacao_swap, mutacao_reverso
from def_crossover import crossover_um_ponto, crossover_dois_pontos
from def_matrizes import gerar_populacao, gerar_instalacoes, gerar_locais, gerar_matrizes
from algoritmo import algoritmo_genetico, lista_fitness

def main():
    print("Bem-vindo ao algoritmo genético para o problema de alocação de instalações!")
    while True:
        print("\nEscolha uma opção:")
        print("1. Executar o algoritmo genético")
        print("2. Sair")
        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Erro: Digite um número válido (1 ou 2).")
            continue

        if opcao == 1:
            try:
                n = int(input("Digite o tamanho da população: "))
                n_geracoes = int(input("Digite o número de gerações: "))
            except ValueError:
                print("Erro: Tamanho da população e número de gerações devem ser números inteiros.")
                continue

            # Gera locais fixos e instalações
            locais_fixos = gerar_locais(n)
            instalacoes = gerar_instalacoes(n)
            
            # Gera população inicial
            populacao = gerar_populacao(n, instalacoes, locais_fixos)
            matriz_distancia, matriz_fluxo = gerar_matrizes(locais_fixos, instalacoes)
            
            # Calcula fitness inicial
            fitness_pop = lista_fitness(populacao, locais_fixos, matriz_distancia, matriz_fluxo)

            print("\nPopulação inicial:")
            for i, individuo in enumerate(populacao):
                print(f'Indivíduo {i}: {individuo}')

            print("\nFitness da população inicial:")
            for i, f in enumerate(fitness_pop):
                print(f'Indivíduo {i}: {f}')

            # Seleção
            try:
                selecao_op = int(input("\nEscolha a seleção (1-Roleta, 2-Torneio): "))
            except ValueError:
                print("Seleção padrão (Roleta) será usada.")

            # Crossover
            try:
                crossover_op = int(input("Escolha o crossover (1-Um ponto, 2-Dois pontos): "))
            except ValueError:
                print("Crossover padrão (Um ponto) será usado.")

            # Mutação
            try:
                mutacao_op = int(input("Escolha a mutação (1-Swap, 2-Reverso): "))
            except ValueError:
                print("Mutação padrão (Swap) será usada.")

            # Elitismo
            try:
                elitismo_op = int(input("Escolha o elitismo (1-Simples, 2-Composto): "))
            except ValueError:
                print("Elitismo padrão (Simples) será usado.")

            # Executa o algoritmo genético
            populacao_final = algoritmo_genetico(
                populacao=populacao,
                n_geracoes=n_geracoes,
                fitness=fitness_pop,
                selecao=selecao_roleta if selecao_op == 1 else selecao_torneio,
                crossover=crossover_um_ponto if crossover_op == 1 else crossover_dois_pontos,
                elitismo=elitismo_simples if elitismo_op == 1 else elitismo_composto,
                mutacao=mutacao_swap if mutacao_op == 1 else mutacao_reverso
            )

            print("Solucao final:")
            solucao = populacao_final[0]
            print(f'Indivíduo: {solucao}')
            
        elif opcao == 2:
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")        
if __name__ == "__main__":
    main()