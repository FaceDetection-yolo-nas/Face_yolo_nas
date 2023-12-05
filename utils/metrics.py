'''
dataset_params = {
    'data_dir':'/content/avantiDataReduc',
    'train_images_dir':'/content/avantiDataReduc/kaggle/input/face-detection-dataset/images/train',
    'train_labels_dir':'/content/avantiDataReduc/kaggle/input/face-detection-dataset/labels/train',
    'val_images_dir':'/content/avantiDataReduc/kaggle/input/face-detection-dataset/images/val',
    'val_labels_dir':'/content/avantiDataReduc/kaggle/input/face-detection-dataset/labels/val',
    'test_images_dir':'/content/avantiDataReduc/kaggle/input/face-detection-dataset/images/val',
    'test_labels_dir':'/content/avantiDataReduc/kaggle/input/face-detection-dataset/labels/val',
     'classes': ['face']
}

train_data = coco_detection_yolo_format_train(
    dataset_params={
        'data_dir': dataset_params['data_dir'],
        'images_dir': dataset_params['train_images_dir'],
        'labels_dir': dataset_params['train_labels_dir'],
        'classes': dataset_params['classes']
    },
    dataloader_params={
        'batch_size': BATCH_SIZE,
        'num_workers': 1
    }
)

val_data = coco_detection_yolo_format_val(
    dataset_params={
        'data_dir': dataset_params['data_dir'],
        'images_dir': dataset_params['val_images_dir'],
        'labels_dir': dataset_params['val_labels_dir'],
        'classes': dataset_params['classes']
    },
    dataloader_params={
        'batch_size': BATCH_SIZE,
        'num_workers': 1
    }
)

test_data = coco_detection_yolo_format_val(
    dataset_params={
        'data_dir': dataset_params['data_dir'],
        'images_dir': dataset_params['test_images_dir'],
        'labels_dir': dataset_params['test_labels_dir'],
        'classes': dataset_params['classes']
    },
    dataloader_params={
        'batch_size': BATCH_SIZE,
        'num_workers': 1
    }
)
'''
train_params = {

  "loss": PPYoloELoss(
        use_static_assigner=False,
        num_classes=len(dataset_params['classes']),
        reg_max=16
        ),
    "valid_metrics_list": [
        DetectionMetrics_050(
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
    "metric_to_watch": 'mAP@0.50'
}
'''
dataset_params = {
    'data_dir':'/content/avantiDataReduc',
    'train_images_dir':'/content/avantiDataReduc/kaggle/input/face-detection-dataset/images/train',
    'train_labels_dir':'/content/avantiDataReduc/kaggle/input/face-detection-dataset/labels/train',
    'val_images_dir':'/content/avantiDataReduc/kaggle/input/face-detection-dataset/images/val',
    'val_labels_dir':'/content/avantiDataReduc/kaggle/input/face-detection-dataset/labels/val',
    'test_images_dir':'/content/avantiDataReduc/kaggle/input/face-detection-dataset/images/val',
    'test_labels_dir':'/content/avantiDataReduc/kaggle/input/face-detection-dataset/labels/val',
     'classes': ['face']
}

train_data = coco_detection_yolo_format_train(
    dataset_params={
        'data_dir': dataset_params['data_dir'],
        'images_dir': dataset_params['train_images_dir'],
        'labels_dir': dataset_params['train_labels_dir'],
        'classes': dataset_params['classes']
    },
    dataloader_params={
        'batch_size': BATCH_SIZE,
        'num_workers': 1
    }
)

val_data = coco_detection_yolo_format_val(
    dataset_params={
        'data_dir': dataset_params['data_dir'],
        'images_dir': dataset_params['val_images_dir'],
        'labels_dir': dataset_params['val_labels_dir'],
        'classes': dataset_params['classes']
    },
    dataloader_params={
        'batch_size': BATCH_SIZE,
        'num_workers': 1
    }
)

test_data = coco_detection_yolo_format_val(
    dataset_params={
        'data_dir': dataset_params['data_dir'],
        'images_dir': dataset_params['test_images_dir'],
        'labels_dir': dataset_params['test_labels_dir'],
        'classes': dataset_params['classes']
    },
    dataloader_params={
        'batch_size': BATCH_SIZE,
        'num_workers': 1
    }
)
'''
