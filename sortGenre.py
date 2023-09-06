import pandas as pd
import requests

try:
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

        # Verifica se a resposta da API foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            # parse response para json
            data = response.json()
            gender = data['gender']
            
            # aumenta os contadores
            if gender == 'male':
                male_count += 1
            elif gender == 'female':
                female_count += 1
        else:
            print(f'Erro ao processar o nome {name}')

    # Print results
    print(f'Contagem de masulinos: {male_count}')
    print(f'Contagem de femininos: {female_count}')
except Exception as e:
    print(f'O seguinte erro ocorreu {str(e)}')
