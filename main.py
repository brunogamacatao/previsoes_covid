import json
from dados_covid import load_covid_data
from numpy import loadtxt, zeros, ones, array, linspace, logspace
import pylab

# carregamos os dados
results = json.loads(load_covid_data())['results']
results = list(map(lambda i: {
  'dia': i['label'],
  'casos': i['qtd_confirmado'],
  'obitos': i['qtd_obito']
}, results))

# formatamos os dados para exibição
dias   = range(1, len(results) + 1)
casos  = list(map(lambda i: i['casos'], results))
obitos = list(map(lambda i: i['obitos'], results))

# Fitting Polynomial Regression to the dataset 
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import PolynomialFeatures

# Treinando o modelo de regressão
dias_anteriores = list(zip(dias, dias))

poly = PolynomialFeatures(degree = 4) 
dias_anteriores = poly.fit_transform(dias_anteriores) 
  
poly.fit(dias_anteriores, casos) 
lin2 = LinearRegression() 
lin2.fit(dias_anteriores, casos) 

# Prevendo N dias para frente
n_dias = 10
ultimo_dia = dias[-1]
proximos_dias = range(ultimo_dia, ultimo_dia + n_dias)
proximos_dias = list(zip(proximos_dias, proximos_dias))
previsao_casos = lin2.predict(poly.fit_transform(proximos_dias))

# plotamos o gráfico
pylab.plot(dias, casos, '-b', marker='o', markersize=4, label='Casos')
pylab.plot(dias, obitos, '-r', marker='*', markersize=4, label='Óbitos')
pylab.plot(proximos_dias, previsao_casos, color = 'yellow', marker='o', markersize=4, label='Previsão de Casos')

pylab.legend(loc='upper left')
pylab.title('Casos confirmados por dia no Brasil')
pylab.xlabel('Dia')
pylab.show()
