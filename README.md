🎲 random-list-counter
Gera uma lista com 10 números inteiros aleatórios entre 1 e 10, solicita um número ao usuário e exibe quantas vezes esse número aparece na lista gerada.

📋 Descrição
Este projeto é um pequeno script Python de linha de comando que demonstra conceitos fundamentais da linguagem:

Geração de números aleatórios com o módulo random
Manipulação de listas com append() e count()
Entrada de dados pelo usuário com input()
Formatação de strings com f-strings


🚀 Como usar
Pré-requisitos

Python 3.6 ou superior instalado

Executando o script
bashpython main.py
Exemplo de execução
numero: 7
seu numero (7) apareceu 2 vezes
[3, 7, 1, 7, 5, 9, 2, 4, 6, 8]

🧠 Como funciona

Uma lista vazia é criada
Um laço for executa 10 vezes, adicionando um inteiro aleatório (entre 1 e 10) à lista a cada iteração
O usuário digita um número
O script usa .count() para contar quantas vezes esse número aparece
O resultado e a lista são exibidos no terminal


📁 Estrutura do projeto
random-list-counter/
└── main.py

🛠️ Tecnologias

Python 3 — linguagem principal
random — módulo da biblioteca padrão


📚 Conceitos demonstrados
ConceitoAplicação no códigoMódulo randomrandom.randint(1, 10)Listaslista.append(), lista.count()Laço for + rangefor i in range(10)Entrada de dadosint(input(...))f-stringsf"seu numero ({n}) apareceu..."

💡 Possíveis melhorias

Permitir que o usuário defina o tamanho da lista e o intervalo dos números
Exibir a frequência de todos os números da lista de uma vez
Ordenar a lista antes de exibir
Validar se o número inserido está dentro do intervalo válido


📄 Licença MIT
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.


Projeto simples para fins didáticos e prática de lógica de programação em Python.
