## README

Install [scanpy](https://scanpy.readthedocs.io/en/stable/installation.html) into a Conda environment.

```console
mamba create -c conda-forge -n scanpy scanpy python-igraph leidenalg
conda activate scanpy
python3 -c "import scanpy" && echo "Installed" || echo "Not installed"
conda deactivate
```
