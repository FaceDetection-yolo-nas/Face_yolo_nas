
## Introdução
O foco deste projeto é abordar a detecção de faces em imagens, uma tarefa crucial em diversas aplicações, como reconhecimento facial e análise de vídeos.

## Problema e Justificativa
Detectar rostos é essencial em muitos contextos, e a precisão nessa tarefa é fundamental. Este projeto busca criar um modelo de detecção de faces utilizando a arquitetura YOLO-NAS e avaliar seu desempenho.

## Objetivo Geral
Desenvolver um modelo de detecção facial utilizando a arquitetura "YOLO-NAS", aprimorando a precisão da detecção em condições variáveis.

### Base de Dados
O conjunto de dados usado é proveniente do Kaggle, fonte <https://www.kaggle.com/datasets/fareselmenshawii/face-detection-dataset>, contendo imagens para validação e imagens para treinamento. 

## Metodologia
1. **Preparação dos Dados:** Organização e pré-processamento dos conjuntos de treinamento, validação e teste.
2. **Definição do Modelo:** Utilização da arquitetura "YOLO-NAS" com pesos pré-treinados do COCO.
3. **Treinamento do Modelo:** Configuração de parâmetros e treinamento com dados de treinamento.
4. **Avaliação do Modelo:** Métricas de avaliação usando dados de validação.
5. **Visualização de Resultados:** Verificação do desempenho na detecção de faces em imagens de validação.
6. **Métodos de Processamento de Imagens:** Mixup, Augmentation, HSV, Normalização.

### Bibliotecas Usadas
- Kaggle (download de dados)
- Super Gradients (treinamento de modelos de visão computacional)
- PyTorch (criação e treinamento de modelos de aprendizado profundo)
- Bibliotecas padrão (os, shutil, random, tqdm, torch)

### Instalação

````
pip install -r requirements.txt
````

## Ilustrações e Tabelas/Figuras
- Imagens ilustrativas dos processos de Mixup, Augmentation e HSV.
- Tabelas/figuras com métricas de avaliação por classe para segmentação e detecção/classificação.


|   Modelo       | Precisão       | Recall        | F1-score   |
| ---------------|--------------  |-------------  |----------- |
| Yolo-Nas-M     |                |               |            |
| Yolo-Nas-S     |                |               |            |
| Yolo-Nas-L     |                |               |            |

### Componentes do Modelo
#### Arquitetura do Modelo YOLO-NAS
Baseada na arquitetura YOLO-NAS, inicializada com pesos pré-treinados do COCO, treinada para a detecção de "faces".

## Estrutura do Repositório
- `data/`: Pasta contendo os dados utilizados no projeto.
- `models/`: Implementação da arquitetura YOLO-NAS.
- `notebooks/`: Notebooks colab com diferentes etapas do projeto.
- `utils/`: Funções auxiliares para pré-processamento de dados e métricas de avaliação.
- `requirements.txt`: Lista de dependências do projeto.

Este projeto foi desenvolvido como parte do desafio do bootcamp de Machine Learning com foco em detecção facial utilizando a arquitetura YOLO-NAS. Para mais detalhes sobre cada etapa do processo, consulte os notebooks fornecidos e nosso Wiki.
