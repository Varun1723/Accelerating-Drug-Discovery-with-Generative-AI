! pip install --pre deepchem
import deepchem as dc
import rdkit
import numpy as np
tasks, datasets, transformers = dc.molnet.load_tox21(reload =False)
print(tasks)
train_data, valid_data, test_data = datasets
print(train_data.X.shape, train_data.y.shape, train_data.w.shape)
print(valid_data.X.shape, valid_data.y.shape, valid_data.w.shape)
print(test_data.X.shape, test_data.y.shape, test_data.w.shape)
print(transformers)
model = dc.models.MultitaskClassifier(n_tasks=train_data.y.shape[1],n_features=train_data.X.shape[1],layer_sizes=[500],dropouts=0.5)
model.fit(train_data, nb_epoch=50)
met = dc.metrics.Metric(dc.metrics.roc_auc_score, np.mean)

train_score = model.evaluate(train_data, [met], transformers)
test_score = model.evaluate(test_data, [met], transformers)
print(train_score)
print(test_score)
