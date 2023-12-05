from super_gradients.training import Trainer

trainer = Trainer(experiment_name=EXPERIMENT_NAME, ckpt_root_dir=CHECKPOINT_DIR)

trainer.train(model=model,
              training_params=train_params,
              train_loader=train_data,
              valid_loader=val_data)
