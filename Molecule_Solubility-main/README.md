# Solubility Prediction Model

This repository contains a machine learning model designed to predict the solubility of molecules based on their chemical structure.
The model uses molecular fingerprints to extract relevant features and then applies a predictive algorithm to estimate solubility values. 

## Table of Contents
- Installation
- Model Details
- Usage
- Requirements

## Installation

To get started with this project, clone the repository and install the required dependencies.

1. Clone the repository:
   ```bash
   git clone https://github.com/VeereshDodamani/Molecular_Solubility.git
   cd code
2. Install dependencies using pip (make sure you have Python 3.7+):
   ```bash
   pip install -r requirements.txt
   OR
   pip install numpy pandas scikit-learn rdkit

## Model Details

This model is built using molecular fingerprints to encode chemical information. The fingerprints are generated from SMILES strings using the RDKit library, and then a machine learning model (e.g., Random Forest, SVM, or Neural Network) is trained to predict solubility based on those features.

### Features :
Molecular fingerprints are generated from SMILES strings.
The model predicts solubility based on these fingerprints using machine learning algorithms.
## Usuage
After setting up the project, you can use the model to predict the solubility of molecules by providing their molecular structures in the form of SMILES strings.
You can change the molecules in the smile variable and check the solubility of the particular molecule
1. 
```bash
smiles = ['Nc1cccc(O)c1', 'CC1CCCC(C)C1']
```

## Requirements
deepchem

tensorflow==2.14.0

keras==2.14.0
