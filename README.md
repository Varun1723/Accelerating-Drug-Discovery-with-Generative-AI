# Accelerating Drug Discovery with Generative AI

## Project Overview

This project, developed for the GDG Solution Challenge 2025, tackles the significant hurdles in traditional drug discovery: high costs, long timelines, and a high failure rate. Our solution, the **Drug Discovery Assistant**, is a user-friendly and scalable tool powered by Generative AI. It aims to revolutionize the process by enabling researchers to efficiently identify, design, and optimize potential drug candidates. By doing so, we aim to reduce the time and cost associated with traditional methods and improve overall success rates.

---

## Features

Our assistant provides a powerful set of functionalities to streamline the drug discovery pipeline:

* **Molecule Toxicity Prediction:** Predicts the toxicity of molecular compounds using a Multitask Classifier. This helps in filtering out potentially harmful candidates early in the process.
* **Molecule Solubility Prediction:** Evaluates the solubility of molecules using a Graph Convolutional Neural Network (GNN). Good solubility is a crucial factor for a drug's effectiveness.
* **De Novo Molecule Generation:** Generates novel molecular structures using a fine-tuned GPT-2 model. This functionality allows researchers to explore the vast chemical space beyond existing compounds, creating unique candidates.
* **Protein Structure Prediction:** Visualizes the 3D structure of proteins from a single amino acid sequence using the ESMFold model. Understanding a protein's structure is essential for predicting how a drug might bind to it.

---

## Project Structure

The project is organized into modular components, each addressing a specific part of the drug discovery process.

```
├── ACCELERATING-DRUG-DISCOVERY-WITH-GEN...
│   ├── Molecule_2D_Structure_Predicting
│   │   ├── code1.py
│   │   ├── README.md
│   │   └── requirements.txt
│   ├── Molecule_Solubility-main
│   │   ├── code2.py
│   │   ├── README.md
│   │   └── requirements.txt
│   ├── Molecule_toxicity-main
│   │   ├── main.py
│   │   ├── README.md
│   │   └── requirements.txt
│   └── Predicting-protein-structure-main
│       ├── streamlit
│       │   └── config.toml
│       ├── app.py
│       ├── README.md
│       └── requirements.txt
└── README.md
```

---

## Technical Stack

This project uses a variety of powerful libraries and frameworks to build its core functionalities:

* **Python:** The primary programming language for all backend logic and model development.
* **DeepChem:** A library for deep learning in chemistry, used for training the toxicity and solubility prediction models.
* **PyTorch & Transformers:** Used for fine-tuning the GPT-2 model for generative molecule design.
* **RDKit:** A cheminformatics toolkit for manipulating molecular structures.
* **Streamlit:** Used to create the interactive web application for the protein structure predictor.
* **ESM-2:** The language model powering ESMFold, used for predicting protein structures.
* **Py3Dmol:** A Python wrapper for `3Dmol.js`, used to visualize the predicted protein structures in 3D.

---

## Installation and Usage

To get the project running locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Install dependencies:** Navigate to each module's directory and install the required packages using the respective `requirements.txt` file. For example:
    ```bash
    pip install -r Molecule_2D_Structure_Predicting/requirements.txt
    ```

3.  **Run the application:** To launch the protein structure prediction tool, for instance, run the Streamlit app:
    ```bash
    streamlit run Predicting-protein-structure-main/app.py
    ```

---

## License

This project is licensed under the MIT License.