# Processo de Kaprekar em Python
> Programa desenvolvido para aplicar o **Algoritmo de Kaprekar** em números de 4 dígitos, encontrando a famosa **Constante de Kaprekar: 6174**.

---

## Sobre o Projeto
Este projeto foi desenvolvido na disciplina de **Programação de Computadores**, do curso de Ciências da Computação, como um trabalho opcional (valendo ponto extra), com o objetivo de praticar:

- Estruturas condicionais (`if`, `elif`, `else`)
- Laços de repetição (`while`)
- Operações matemáticas com números inteiros
- Manipulação de dígitos sem uso de strings
- Validação de dados
- Lógica computacional

O programa recebe um número de **4 dígitos**, reorganiza seus algarismos em ordem crescente e decrescente, subtrai os valores e repete o processo até encontrar o número **6174**.

---

## O que é a Constante de Kaprekar?
A **Constante de Kaprekar (6174)** foi descoberta pelo matemático indiano **D. R. Kaprekar**.

Para qualquer número de 4 dígitos (com pelo menos dois dígitos diferentes), ao repetir o processo abaixo, sempre se chega em **6174**:

1. Organizar os dígitos em ordem decrescente
2. Organizar os dígitos em ordem crescente
3. Subtrair os dois números
4. Repetir com o resultado

### Exemplo
```text
3524
5432 - 2345 = 3087
8730 - 0378 = 8352
8532 - 2358 = 6174
```

---

## Funcionalidades
- Recebe número inteiro positivo de até 4 dígitos
- Valida entradas inválidas
- Detecta números com 3 ou mais dígitos repetidos
- Executa o processo completo de Kaprekar
- Mostra cada iteração detalhadamente
- Conta quantas iterações foram necessárias
- Exibe mensagem final ao atingir 6174

---

## Fluxograma do Sistema
O algoritmo segue a seguinte lógica:

1. Ler o número informado pelo usuário
2. Validar a entrada (deve estar entre 0000 e 9999 e não pode ter 3 ou mais dígitos repetidos)
3. Enquanto o número for diferente de 6174: montar o maior e o menor número possível com os mesmos dígitos, subtrair os dois valores e mostrar a iteração
4. Validar o resultado a cada iteração (interrompe o processo caso o resultado seja inválido)
5. Repetir até atingir 6174 e exibir o total de iterações

**Imagem do Fluxograma**

<img width="1474" height="2000" alt="image" src="https://github.com/user-attachments/assets/1f159908-8f42-4fb1-a91b-7cc6723bf36e" />

" />

---

## Exemplo de Execução
```
Este programa recebe um número de 4 dígitos e converte para a constante de Kaprekar.
---Digite apenas 4 dígitos (somente números inteiros positivos)---

Digite o número: 3524

Número informado: 3524

Iteração 1 : 5 4 3 2 - 2 3 4 5 = 3 0 8 7
Iteração 2 : 8 7 3 0 - 0 3 7 8 = 8 3 5 2
Iteração 3 : 8 5 3 2 - 2 3 5 8 = 6 1 7 4

Constante de Kaprekar (6174) atingida em 3 iterações.
```

---

## Validações Implementadas
O sistema impede entradas inválidas, como:

**Número negativo**
```
Erro: o número deve ser positivo.
```

**Número maior que 4 dígitos**
```
Erro: número inválido. Deve estar entre 0000 e 9999.
```

**Muitos dígitos repetidos**
```
Erro: número possui muitos dígitos repetidos.
```

---

## Tecnologias Utilizadas
- Python 3
- Lógica de Programação
- Operações Matemáticas Inteiras

---

## Como Executar

**1. Instale o Python**
Download oficial: https://www.python.org/downloads/

**2. Clone o repositório**
```
git clone https://github.com/pietrobitencourt/kaprekar-python
```

**3. Acesse a pasta do projeto**
```
cd kaprekar-python
```

**4. Execute o programa**
```
python kaprekar.py
```

---

## Estrutura do Projeto
```
kaprekar-python/
├── kaprekar.py
├── README.md
└── fluxograma_kaprekar.png
```

---

## Aprendizados com o Projeto
Durante o desenvolvimento, foram reforçados conceitos como:
- Raciocínio lógico
- Algoritmos iterativos
- Tratamento de erros
- Decomposição numérica
- Organização de código procedural

---

## Licença
Este projeto foi desenvolvido para fins acadêmicos e educacionais.
Uso livre para estudos.

---

## Autor
**Piêtro Bitencourt Nunes**

- GitHub: [pietrobitencourt](https://github.com/pietrobitencourt)
- Instagram: [@Piiettrosz](https://instagram.com/Piiettrosz)

---

## Considerações Finais
Este projeto demonstra como conceitos matemáticos interessantes podem ser resolvidos com programação simples e eficiente.

A Constante de Kaprekar é um excelente exemplo de como matemática + lógica + programação podem gerar resultados fascinantes.
