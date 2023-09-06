import pandas as pd
import requests

# carrega o excel em um dataframe
df = pd.read_excel('C:/Users/Igor/Desktop/Projetos/ProjetosPython/Pasta.xlsx')

# extrai os nomes do dataframe
names = df.iloc[:, 0]

# Inicializa os contadores
male_count = 0
female_count = 0

# Laco de repeticao que pega cada nome e executa a chamada da api
for name in names:
    # envia a request para a api
    response = requests.get(f'https://api.genderize.io/?name={name}')
    
    # parse response para json
    data = response.json()
    gender = data['gender']
    
    # aumenta os contadores
    if gender == 'male':
        male_count += 1
    elif gender == 'female':
        female_count += 1

# Print results
print(f'Contagem de masulinos: {male_count}')
print(f'Contagem de femininos: {female_count}')