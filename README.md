# Análise de Score de Crédito de Clientes

Este projeto tem como objetivo realizar a análise de score de crédito de clientes com base em variáveis categóricas e preditivas. Utilizando algoritmos de Machine Learning, o projeto busca prever o score de crédito para novos clientes a partir de um conjunto de dados pré-existente.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **Scikit-learn**: Biblioteca para algoritmos de Machine Learning.
- **LabelEncoder**: Método de codificação de variáveis categóricas.
- **RandomForestClassifier**: Algoritmo de aprendizado supervisionado usado para classificação.
- **KNeighborsClassifier**: Algoritmo de aprendizado supervisionado baseado em vizinhos mais próximos.

## Funcionalidades

1. **Leitura e Análise de Dados**
   - O projeto lê um arquivo CSV (`clientes.csv`) contendo dados de clientes, e exibe informações sobre o conjunto de dados, como colunas e tipos de variáveis.

2. **Codificação de Variáveis Categóricas**
   - As variáveis categóricas como profissão, mix de crédito e comportamento de pagamento são transformadas em valores numéricos usando a técnica de codificação `LabelEncoder`.

3. **Divisão dos Dados**
   - Os dados são divididos em variáveis dependentes (`score_credito`) e independentes, excluindo a coluna `id_cliente`.
   - O conjunto de dados é dividido em dados de treino (70%) e dados de teste (30%) utilizando a função `train_test_split` do Scikit-learn.

4. **Treinamento de Modelos**
   - Dois modelos de aprendizado de máquina são treinados para prever o score de crédito:
     - **RandomForestClassifier**: Um modelo de floresta aleatória.
     - **KNeighborsClassifier**: Um modelo baseado em vizinhos mais próximos.

5. **Avaliação dos Modelos**
   - Após o treinamento, as previsões são feitas com base no conjunto de dados de teste.
   - A acurácia dos modelos é calculada e exibida utilizando a métrica `accuracy_score`.

6. **Previsão para Novos Clientes**
   - Um novo conjunto de dados (`novos_clientes.csv`) é lido e as variáveis categóricas são codificadas da mesma forma.
   - O modelo treinado de floresta aleatória é utilizado para prever o score de crédito dos novos clientes.

## Como Executar o Projeto

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale as bibliotecas necessárias:
   ```bash
   pip install pandas scikit-learn
    python script.py 

## Arquivos Utilizados

- **clientes.csv**: Contém os dados de clientes, incluindo informações como profissão, mix de crédito, comportamento de pagamento e score de crédito.
- **novos_clientes.csv**: Contém os dados de novos clientes para os quais as previsões de score de crédito serão feitas.

## Estrutura do Código

1. **Leitura e pré-processamento de dados**
2. **Treinamento de modelos de Machine Learning**
3. **Avaliação de modelos**
4. **Previsão para novos clientes**

## Resultados

Os modelos **RandomForestClassifier** e **KNeighborsClassifier** são treinados para prever o score de crédito com base nos dados fornecidos. A acurácia dos modelos é avaliada e o modelo com maior precisão é utilizado para fazer previsões sobre novos clientes.

## Contribuição

Sinta-se à vontade para contribuir com melhorias no código ou novas funcionalidades!

## Autor

Kaio Vitor - [GitHub](https://github.com/Kaio-0708)
