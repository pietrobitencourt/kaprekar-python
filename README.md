# Processo de Kaprekar em Python

> Programa desenvolvido para aplicar o **Algoritmo de Kaprekar** em números de 4 dígitos, encontrando a famosa **Constante de Kaprekar: 6174**.

---

## Sobre o Projeto

Este projeto foi desenvolvido na disciplina de **Programação de Computadores**, do curso de Ciências da Computação com o objetivo de praticar:

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

```text id="6c9x3v"
3524
5432 - 2345 = 3087
8730 - 0378 = 8352
8532 - 2358 = 6174

Funcionalidades:

Recebe número inteiro positivo de até 4 dígitos
Valida entradas inválidas
Detecta números com 3 ou mais dígitos repetidos
Executa o processo completo de Kaprekar
Mostra cada iteração detalhadamente
Conta quantas iterações foram necessárias
Exibe mensagem final ao atingir 6174

Fluxograma do Sistema:

O algoritmo segue a seguinte lógica:
Ler o número informado pelo usuário
Validar se está entre 0000 e 9999
Verificar repetição excessiva de dígitos
Aplicar o processo de Kaprekar
Repetir até atingir 6174
```
**Imagem do Fluxograma**
<img width="1024" height="1536" alt="Fluxograma" src="https://github.com/user-attachments/assets/57d03f78-26fe-4eb5-81af-d99555a96a45" />

**Exemplo de Execução:**
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
**Validações Implementadas**
O sistema impede entradas inválidas, como:

Número negativo
```
Erro: o número deve ser positivo.
```
Número maior que 4 dígitos
```
Erro: número inválido. Deve estar entre 0000 e 9999.
```
Muitos dígitos repetidos
```
Erro: número possui muitos dígitos repetidos.
```

Tecnologias Utilizadas
Python 3
Lógica de Programação
Operações Matemáticas Inteiras

Como Executar
1. Instale o Python

Download oficial:

https://www.python.org/downloads/

2. Clone o repositório
```
https://github.com/Ghosttxz/kaprekar-python
```

3. Acesse a pasta do projeto
```
cd seu-repositorio
```

4. Execute o programa
```
python kaprekar.py
```

Estrutura do Projeto
```
projeto-kaprekar/
├── kaprekar.py
├── README.md
└── fluxograma.png
```

Aprendizados com o Projeto:
```
Durante o desenvolvimento, foram reforçados conceitos como:

Raciocínio lógico
Algoritmos iterativos
Tratamento de erros
Decomposição numérica
Organização de código procedural
```

Licença:
```
Este projeto foi desenvolvido para fins acadêmicos e educacionais.
Uso livre para estudos.
```

Autor:
```
Piêtro Bitencourt Nunes
```

GitHub: 
```
pietrobitencourt
```
Instagram: 
```
@ Piiettrosz
```

Considerações Finais:
```
Este projeto demonstra como conceitos matemáticos interessantes podem ser resolvidos com programação simples e eficiente.

A Constante de Kaprekar é um excelente exemplo de como matemática + lógica + programação podem gerar resultados fascinantes.
```
