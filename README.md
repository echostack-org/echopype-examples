# echopype-examples

[![Zenodo Badge](https://img.shields.io/badge/DOI-10.5281/zenodo.5618177-blue)](https://doi.org/10.5281/zenodo.5618177)
[![Jupyter Book](https://img.shields.io/badge/Jupyter%20Book-view%20examples-blue?logo=jupyter)](https://echopype-examples.readthedocs.io/)
[![Documentation Status](https://readthedocs.org/projects/echopype-examples/badge/?version=latest)](https://echopype-examples.readthedocs.io/en/latest/?badge=latest)
[![GitHub License](https://img.shields.io/github/license/echostack-org/echopype-examples)](https://github.com/echostack-org/echopype-examples/blob/main/LICENSE)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/echostack-org/echopype-examples/main?labpath=notebooks/index.ipynb)

This repository hosts demonstration examples for [Echopype](https://echopype.readthedocs.io/en/stable/), an open-source Python library that enables scalable and interoperable water column sonar data processing.

The examples are written as executable Jupyter Notebooks that you can easily run and modify locally on your own machine or on a cloud virtual machine.

## See all examples via Jupyter Book

All notebooks are rendered at: <https://echopype-examples.readthedocs.io/>

## Run the notebooks locally on your computer

If you want to run these notebooks on your local computer, follow the steps below:

- Clone and go into the repo:

  ```shell
  # clone the repo
  git clone https://github.com/echostack-org/echopype-examples.git

  # go into the repo folder
  cd echopype-examples
  ```

- Create a conda environment using the `environment.yml` file in the `conda` folder. We recommend using Mamba (see steps [here](https://github.com/conda-forge/miniforge) to install).

  ```shell
  # create an environment using latest echopype branch
  mamba env create -n echopype-examples -f conda/environment-ep-main.yml

  # activate the environment
  conda activate echopype-examples
  ```

- Try out the notebooks in the `notebooks` folder!

## Run the notebooks on the cloud via Binder

You can run the notebooks directly on the cloud using MyBinder.org by clicking the Binder badge at the top of this page.

This will create a pre-configured JupyterLab with all the example notebooks under the `notebooks` folder. However, note that:

- It usually takes a few minutes to spin up Binder.
- The computational resources are very minimal on Binder, so some example notebooks that handle many files may take a very long time or fail.
- Any changes you make to the notebooks won't be saved permanently because Binder provides a temporary workspace.

## Contribute to the example notebooks

Contributions are welcome and greatly appreciated!

The steps to set up a development environment are the same as above. However:

- If you want to use the latest changes in the Echopype `main` branch, use `conda/environment-ep-main.yml` when creating the conda environment.
- If you already have a functional Echopype development environment (see [here](https://echopype.readthedocs.io/en/stable/contributing.html#installation-for-echopype-development)) and want to use that, you can install additional packages needed for this repo with:

  ```shell
  conda install -c conda-forge geopandas cartopy datashader holoviews hvplot
  ```

  Note that it is often cleaner and easier to just create a new environment.

To build the Jupyter Book locally:

```shell
# install Jupyter Book
conda install -c conda-forge jupyter-book

# go into the repo folder
cd echopype-examples

# build the Jupyter Book
jupyter-book build notebooks
```
