# Programa que aplica o processo de Kaprekar.
# Autor: Piêtro Bitencourt Nunes
# Ig: @Piiettrosz - GitHub: pietrobitencourt
# Disciplina: Programação de Computadores
# Objetivo: Encontrar a constante 6174
        # O algoritmo organiza os dígitos em ordem crescente e decrescente, subtrai os valores e repete até chegar em 6174.

print("Este programa recebe um número de 4 dígitos e converte para a constante de Kaprekar.")
print("---Digite apenas 4 dígitos (somente números inteiros positivos)---")

num = int(input("Digite o número: "))

# ETAPA 1: VALIDAÇÃO DO NÚMERO INFORMADO

# Verifica se o número é negativo e aplica a mensagem de erro!
if num < 0:
    print("Erro: o número deve ser positivo.")

# Verifica se o número possui mais de 4 dígitos e aplica a mensagem de erro!
elif num > 9999:
    print("Erro: número inválido. Deve estar entre 0000 e 9999.")

# Se passou nas validações iniciais, continua o programa.
else:
    # ETAPA 2: SEPARAR OS 4 DÍGITOS DO NÚMERO
    d1 = num // 1000            # Representa o 1º dígito (milhar).
    d2 = (num // 100) % 10      # Representa o 2º dígito (centena).
    d3 = (num // 10) % 10       # Representa o 3º dígito (dezena).
    d4 = num % 10               # Representa o 4º dígito (unidade).

    # ETAPA 3: VALIDAR REPETIÇÃO DE DÍGITOS
    # Não pode ter 3 ou mais dígitos iguais
            # Comparamos todas as combinações possíveis de trios: (1º, 2º e 3º) OU (1º, 2º e 4º) OU (1º, 3º e 4º) OU (2º, 3º e 4º).
    if (d1 == d2 and d1 == d3) or (d1 == d2 and d1 == d4) or (d1 == d3 and d1 == d4) or (d2 == d3 and d2 == d4):
        print("Erro: número possui muitos dígitos repetidos.")      # Se qualquer uma for verdadeira, o número é inválido para o processo.

    else:
        print("")      # Imprime uma linha vazia.
        print("Número informado:", num)     # Mostra o número aceito pelo programa.

        # Variável para contar quantas iterações foram feitas
        contador = 0

        # ETAPA 4: PROCESSO DE KAPREKAR
        # Repete até encontrar 6174

        while num != 6174: # Enquanto a variável num estiver diferente de 6174, o loop continuará.

            # Separar novamente os dígitos do número atual.
            d1 = num // 1000             # Representa o 1º dígito (milhar).
            d2 = (num // 100) % 10       # Representa o 2º dígito (centena).
            d3 = (num // 10) % 10        # Representa o 3º dígito (dezena).
            d4 = num % 10                # Representa o 4º dígito (unidade).

            # MONTAR O NDC (Número em Dígitos Crescentes).
            a = d1
            b = d2      # Criar variáveis para cada dígito.
            c = d3
            d = d4
            # Ordenação manual crescente.
            if a > b:
                a, b = b, a     # Aqui trocamos os valores das variáveis para a ordem crescente.
            if a > c:           # Ex: Se a = 5 e b = 2.
                a, c = c, a     # Após a, b = b, a, o a vira 2 e o b vira 5 (o menor assume a primeira posição).
            if a > d:           # Assim sucessivamente com todas as variáveis.
                a, d = d, a
            if b > c:
                b, c = c, b
            if b > d:
                b, d = d, b
            if c > d:
                c, d = d, c     # Resultado final: Estão em ordem crescente!

            # Junta os dígitos formando o menor número possível.
            ndc = a * 1000 + b * 100 + c * 10 + d

            # MONTAR O NDD (Número em Dígitos Decrescentes).
            a = d1
            b = d2      # Criar variáveis para cada dígito.
            c = d3
            d = d4

            # Ordenação manual decrescente.
            if a < b:
                a, b = b, a  # Aqui trocamos os valores das variáveis para ordem decrescente.
            if a < c:           # Ex: Se a = 2 e b = 5.
                a, c = c, a     # Após a, b = b, a, o a vira 5 e o b vira 2 (o maior assume a primeira posição).
            if a < d:           # Assim sucessivamente com as demais variáveis.
                a, d = d, a
            if b < c:
                b, c = c, b
            if b < d:
                b, d = d, b
            if c < d:
                c, d = d, c     # Resultado final: Estão em ordem decrescente!

            # Junta os dígitos formando o maior número possível.
            ndd = a * 1000 + b * 100 + c * 10 + d

            # SUBTRAÇÃO PRINCIPAL DE KAPREKAR
            resultado = ndd - ndc

            # Soma mais uma iteração.
            contador = contador + 1

            # Mostra a operação realizada.
            # Desmembra o número (NDD, NDC ou Resultado) em 4 dígitos individuais.
            # Isso permite exibir zeros à esquerda que o Python normalmente esconderia.

            n1 = ndd // 1000            # Extrai o 1º dígito (milhar)
            n2 = (ndd // 100) % 10      # Extrai o 2º dígito (centena)
            n3 = (ndd // 10) % 10       # Extrai o 3º dígito (dezena)
            n4 = ndd % 10               # Extrai o 4º dígito (unidade)

            c1 = ndc // 1000            # Extrai o 1º dígito (milhar)
            c2 = (ndc // 100) % 10      # Extrai o 2º dígito (centena)
            c3 = (ndc // 10) % 10       # Extrai o 3º dígito (dezena)
            c4 = ndc % 10               # Extrai o 4º dígito (unidade)

            r1 = resultado // 1000              # Extrai o 1º dígito (milhar)
            r2 = (resultado // 100) % 10        # Extrai o 2º dígito (centena)
            r3 = (resultado // 10) % 10         # Extrai o 3º dígito (dezena)
            r4 = resultado % 10                 # Extrai o 4º dígito (unidade)

            # Exibe a linha da iteração imprimindo cada dígito isolado.
            # Como estava restrito o uso de 'processamento de texto (strings)', a saída terá espaços entre os números. Ex.: 5 4 2 1 - 1 2 4 5 = 4 1 7 6
            print("Iteração", contador, ":", n1, n2, n3, n4, "-", c1, c2, c3, c4, "=", r1, r2, r3, r4)

            # O resultado vira o novo número.
            num = resultado

            # REVALIDAÇÃO DO RESULTADO
            if num != 6174:     # Se a variável ainda estiver diferente de 6174.

                # Verifica se ainda está entre 0000 e 9999.
                if num < 0 or num > 9999:       # Se estiver menor que 0 ou estiver acima de 9999, mostrar a mensagem de erro.
                    print("Erro: resultado inválido.")
                    break   # Interrompe o loop e encerra o processo de cálculo devido ao erro.

                # Separa os dígitos novamente.
                d1 = num // 1000            # Representa o 1º dígito (milhar).
                d2 = (num // 100) % 10      # Representa o 2º dígito (centena).
                d3 = (num // 10) % 10       # Representa o 3º dígito (dezena).
                d4 = num % 10               # representa o 4º dígito (unidade).

                # Verifica se surgiram 3 dígitos iguais.
                if (d1 == d2 and d1 == d3) or (d1 == d2 and d1 == d4) or (d1 == d3 and d1 == d4) or (d2 == d3 and d2 == d4):
                    print("Erro: resultado possui muitos dígitos repetidos.")
                    break
        # Linha em branco no final.
        print("")
        # Se chegou em 6174, mostra sucesso.
        if num == 6174:
            print("Constante de Kaprekar (6174) atingida em", contador, "iterações.")
