# IDL-PPBopt
Code for "IDL-PPBopt: A Strategy for Prediction and Optimization of Human Plasma Protein Binding of Compounds via an Interpretable Deep Learning Method"

## Requirements
That version of the model uses cuda.
- python 3.7
- pytorch 1.5.0
- openbabel 2.4.1
- rdkit
- scikit learn
- scipy 
- cairosvg

## Installation
Using conda:

```sh
# 1- Clone that repo.
git clone https://github.com/Aml-Hassan-Abd-El-hamid/IDL-PPBopt.git

# 2- Create conda environment form inside the repo folder.
cd IDL-PPBopt
conda env create -f environment.yml

# 3- Activate conda environment.
conda activate IDL_PPBopt_cuda

# 4- Build and install the modules insider the repo folder.
make build
make install
```

## Usage
The above instructions allow the import of two new modules: `AttentiveFP` and `IDLPPBopt`.
Have a look at the examples for detailed use instructions.

## Model
The iPPB model was trained with AttentiveFP algorithm and saved in the "saved_models" file.

## PPB prediction and second-level chemical rules' derivation for PPB optimization
1. Write the given molecules to *input_compounds.csv* file.
2. Run *IDL-PPBopt.ipynb* in jupyter notebook.
