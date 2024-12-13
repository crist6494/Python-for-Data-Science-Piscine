# ft_package

`ft_package` is a Python package that can be easily installed and used in your Python projects. This README explains how to install, configure, and use the package.

## Installation

To install the `ft_package` locally, follow these steps:


### Step 1: Package Your Library

If you haven’t packaged your library yet, first create the distribution files. Run the following command in your package directory:

```bash
python setup.py sdist bdist_wheel
```


### Step 2: Install Your Package

Once the package is built, you can install it using pip. You can install it directly from the dist/ directory by running:

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

The .tar.gz file contains the source code of the package, and pip will compile and install it from the source.

Or, if you have the .whl file, you can use:


```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

The .whl file is a precompiled binary distribution, so the installation is faster because there’s no need to compile the source code

### Step 3: Verifying Installation
After installation, you can verify that the package is installed by importing it in a Python script or interactive session:

```python 
import ft_package
```


### Uninstalling the Package
If you need to remove the package from your environment, you can uninstall it using pip:

```bash
pip uninstall ft_package
```


### Updating the Package
If you release a new version of your package, you can update the installed package by running:

```bash
pip install --upgrade ./dist/ft_package-0.0.2.tar.gz
```
Replace the path with the new .tar.gz or .whl file for the updated version.