<img src="/assets/capa.png">

## Introdução
O foco deste projeto é abordar a detecção de faces em imagens, uma tarefa crucial em diversas aplicações, como reconhecimento facial e análise de vídeos.

## Problema e Justificativa
Detectar rostos é essencial em muitos contextos, e a precisão nessa tarefa é fundamental. Este projeto busca criar um modelo de detecção de faces utilizando a arquitetura YOLO-NAS e avaliar seu desempenho.

## Objetivo Geral
Desenvolver um modelo de detecção facial utilizando a arquitetura "YOLO-NAS", aprimorando a precisão da detecção em condições variáveis.

### Base de Dados
O conjunto de dados usado é proveniente do Kaggle, fonte [face-detection-dataset](<https://www.kaggle.com/datasets/fareselmenshawii/face-detection-dataset>), contendo imagens para validação e imagens para treinamento. 

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

### Componentes do Modelo
#### Arquitetura do Modelo YOLO-NAS
Baseada na arquitetura YOLO-NAS, inicializada com pesos pré-treinados do COCO, treinada para a detecção de "faces".

#### Modelos implementados

|   Modelo	     | Classe de modelo |	   Classe de Perda	 |    Retorno de chamada NMS       |    
|--------------- |--------------    |-------------------   |----------------------           |
|                |   Yolo-Nas-M     |       PPYoloELoss    |  PPYoloEPostPredictionCallback  |            
|   YoloNAS      |   Yolo-Nas-S     |       PPYoloELoss    |  PPYoloEPostPredictionCallback  |            
|                |   Yolo-Nas-L     |       PPYoloELoss    |  PPYoloEPostPredictionCallback  |  

#### Parametros de treinamentos

- taxa de aprendizado: CosineLRScheduler

````
from super_gradients import Trainer

    training_params={"initial_lr": 5e-4, 
    "lr_mode": "CosineLRScheduler",
    "cosine_final_lr_ratio": 0.1, ...}, 
    ...
}
````  

- otimizadores: SGD , Adam , AdamW

````
from super_gradients import Trainer

    training_params={"optimizer": "Adam", "optimizer_params": {weight_decay:0001}, ...}, 
    ...
}
````

- Média Móvel Exponencial ou EMA: "exp"

````
from super_gradients import Trainer

    training_params={"ema_params": {"decay": 0.9999, "decay_type": "exp", "beta": 15}, ...}, 
    ...
}
````

- Métricas: DetectionMetrics_050

````
from super_gradients import Trainer

    training_params={"valid_metrics_list": [
        DetectionMetrics_050 (
            score_thres=0.1,
            top_k_predictions=300,
            num_cls=len(dataset_params['classes']),
            normalize_targets=True,
            post_prediction_callback=PPYoloEPostPredictionCallback(
                score_threshold=0.01,
                nms_top_k=1000,
                max_predictions=300,
                nms_threshold=0.5, 
            )
        )
    ],
    "metric_to_watch": 'mAP@0.50
}
````
  

## Tabelas e Imagem 
- Resultado de uma imagem usada na detecção de face.

<img src="/assets/imagem tratada.png">

- Tabela com métricas de avaliação por modelo e otimizador considerando 35 épocas de treinamento e validação.
                                      

|   **`Modelo`**     |  **`Otimizador`**  |**`Classes de Perda (Loss)/Train`**|  **`Precisão`**      | **`Recall`**      | **`F1-score`** |   **`MAP`**   |**`Classes de Perda (Loss)/Val`** |
| ---------------  |:-------------: | :--------------------:  | :---------------:| :------------:| :---------:| :--------:| :------------------:     |
|                  |     AdamW      |       2.02              |      0.052       |    0.804      |  0.099     |  0.62     |    1.97                  |
|  Yolo-Nas-L      |     SGD        |       1.64              |      0.176       |    0.915      |  0.296     |  0.837    |    1.60                  |
|                  |     Adam       |       1.63              |      0.122       |    0.913      |  0.215     |  0.831    |    1.65                  |
|                  |                |                         |                  |               |            |           |                          |
|                  |     AdamW      |       1.66              |      0.105       |    0.904      |  0.188     |  0.82     |    1.68                  |
|  Yolo-Nas-M      |     SGD        |       1.65              |      0.167       |    0.912      |  0.282     |  0.83     |    1.59                  |
|                  |     Adam       |       1.67              |      0.109       |    0.903      |  0.194     |  0.81     |    1.69                  |
|                  |                |                         |                  |               |            |           |                          |
|                  |     AdamW      |       1.64              |      0.110       |    0.900      |  0.196     |  0.81     |    1.67                  |
|  Yolo-Nas-S      |     SGD        |       1.73              |      0.108       |    0.893      |  0.192     |  0.80     |    1.69                  |
|                  |     Adam       |       1.65              |      0.112       |    0.910      |  0.2       |  0.81     |    1.68                  |



## Estrutura do Repositório
- `data/`: Pasta contendo os dados utilizados no projeto.
- `models/`: Implementação da arquitetura YOLO-NAS.
- `notebooks/`: Notebooks colab com diferentes etapas do projeto.
- `utils/`: Funções auxiliares para pré-processamento de dados e métricas de avaliação.
- `requirements.txt`: Lista de dependências do projeto.

Este projeto foi desenvolvido como parte do desafio do bootcamp de Machine Learning com foco em detecção facial utilizando a arquitetura YOLO-NAS. Para mais detalhes sobre cada etapa do processo, consulte os notebooks fornecidos e nosso [Wiki](<https://github.com/FaceDetection-yolo-nas/Face_yolo_nas/wiki>).
