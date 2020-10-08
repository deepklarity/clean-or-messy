# Trainer

### Requirements
Install the requirements to train a fastai and a keras model using:
```pip install -r requirements.txt```

### Blog
blog here

### Jupyter notebooks for training a classifier.
- [Train a classifier in fastai and export pickle](Training-Fastai-Classifier.ipynb)
- [Train a classifier in fastai and export pickle and convert to tensorflowjs](Keras-Trainer-And-TFJSConverter.ipynb)

### Dataset
Create a directory called `datasets` and copy [this](https://github.com/Rahul240499/Clean-vs-Messy-Room-Classification/tree/master/dataset) dataset. Any data from other sources could also be placed inside this directory in a similar format.

Alternatively, same dataset could also be downloaded from [Kaggle Datasets](https://www.kaggle.com/cdawn1/messy-vs-clean-room)

### Deployment
- Once the models are trained, `models/model_v0.pkl` could be moved to `server/` and `streamlit/` directories to be deployed
- `models/tfjs_model` could be moved to `frontend/public/` directory for offline prediction
- `models/keras_model.h5` could also be loaded with some changes for inference