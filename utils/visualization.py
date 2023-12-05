best_model = models.get(
    MODEL_ARCH,
    num_classes=len(dataset_params['classes']),
    checkpoint_path=f"average_model.pth"
).to(DEVICE)

%load_ext tensorboard
%tensorboard --logdir {CHECKPOINT_DIR}/{EXPERIMENT_NAME}
   
img_1 = ""
best_model.predict(img_1).show()
     

img_2 = ""
best_model.predict(img_2).show()


