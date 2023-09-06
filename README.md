# Sort Genre

Este é um projeto Python simples que utiliza a biblioteca Pandas para ler um arquivo Excel contendo nomes e, em seguida, faz chamadas à API Genderize.io para determinar o gênero associado a cada nome. O objetivo é contar quantos nomes são classificados como masculinos e quantos são classificados como femininos na lista de nomes.

## Pré-requisitos
Antes de executar o projeto, certifique-se de que você tenha os seguintes pré-requisitos instalados:

Python 3.x
Pandas
Requests

## Como Usar

1. Clone este repositório para o seu sistema local.
2. Certifique-se de que o arquivo Excel que você deseja analisar esteja localizado no caminho especificado em df = pd.read_excel('C:/Users/Igor/Desktop/Projetos/ProjetosPython/Pasta.xlsx'). Você pode substituir este caminho pelo caminho do seu arquivo Excel.
3. Execute o script Python gender_counter.py no seu ambiente Python: python gender_counter.py
4. O script lerá o arquivo Excel, enviará solicitações à API Genderize.io para determinar o gênero de cada nome e, em seguida, imprimirá os resultados na saída padrão.

Após a execução bem-sucedida do script, você verá os seguintes resultados:
Contagem de masculinos: X
Contagem de femininos: Y
Onde X é o número de nomes classificados como masculinos e Y é o número de nomes classificados como femininos.

## Notas
Certifique-se de que sua máquina tenha acesso à Internet para que o script possa fazer chamadas à API Genderize.io.

Este projeto é uma demonstração simples de como usar Pandas e a API Genderize.io para contar nomes masculinos e femininos em um arquivo Excel. Você pode personalizá-lo conforme suas necessidades específicas.

Lembre-se de respeitar os termos de uso da API Genderize.io e considerar a limitação de uso gratuito. Você pode querer verificar os termos e limites no site oficial da API em http://www.genderize.io.

Certifique-se de não compartilhar dados pessoais ou sensíveis ao usar este projeto.

Divirta-se explorando a contagem de gêneros em sua lista de nomes!
