import pandas as ps

tabela = pd.read_csv("clientes.csv")

display(tabela)

display(tabela.info())

from sklearn.preprocessing import LabelEncoder

codificador = LabelEncoder()

tabela["profissao"] = codificador.fit_transform(tabela["profissao"])

codificador2 = LabelEncoder()

tabela["mix_credito"] = codificador2.fit_transform(tabela["mix_credito"])

codificador3 = LabelEncoder()

tabela["comportamento_pagamento"] = codificador3.fit_transform(tabela["comportamento_pagamento"])

display(tabela.info())

y = tabela["score_credito"]
x = tabela.drop(columns=["score_credito", "id_cliente"])

from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x,y, test_size=0.3)

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

modelo_arvoredecisao = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()

modelo_arvoredecisao.fit(x_treino, y_treino)
modelo_knn.fit(x_treino, y_treino)


previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)
previsao_knn = modelo_knn(x_teste)

from sklearn.metrics import accuracy_score

display(accuracy_score(y_teste, previsao_arvoredecisao))
display(accuracy_score(y_teste, previsao_knn))

tabela_novos_clientes = pd.read_csv("novos_clientes.csv")
display(tabela_novos_clientes)

tabela_novos_clientes["profissao"] = codificador.fit_transform(tabela_novos_clientes["profissao"])
tabela_novos_clientes["mix_credito"] = codificador2.fit_transform(tabela_novos_clientes["mix_credito"])
tabela_novos_clientes["comportamento_pagamento"] = codificador3.fit_transform(tabela_novos_clientes["comportamento_pagamento"])

previsao = modelo_arvoredecisao.predict(tabela_novos_clientes)
display(previsao)
