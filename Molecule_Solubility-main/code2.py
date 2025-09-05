!pip install --pre deepchem
!pip install tensorflow==2.14.0 keras==2.14.0
import deepchem as dc
from rdkit import Chem

tasks, datasets, transformers = dc.molnet.load_delaney(featurizer='GraphConv')

train, valid, test = datasets

model = dc.models.GraphConvModel(
    n_tasks=1,
    mode='regression',
    dropout=0.2,
    graph_conv_layers=[128, 128],
    dense_layer_size=128,
    batch_normalize=False  # Disable batch normalization to avoid the error
)

model.fit(train, nb_epoch=100)

metrics = dc.metrics.Metric(dc.metrics.pearson_r2_score)
train_scores = model.evaluate(train, [metrics], transformers)
print(train_scores)

test_score = model.evaluate(test, [metrics], transformers)
print(test_score)

smiles = ['Nc1cccc(O)c1', 'CC1CCCC(C)C1']

mol = [Chem.MolFromSmiles(molecules) for molecules in smiles]
mol

featurizer = dc.feat.ConvMolFeaturizer()
featurized_mol = featurizer.featurize(mol)

prediction = model.predict_on_batch(featurized_mol)
print(prediction)
