from setuptools import setup, find_packages


setup(
    name='ft_package',
    version='0.0.1',
    author='cmorales',
    author_email='moralesrojascr@gmail.com',
    description='A sample test package',
    long_description=open('README.md').read(),
    url='https://github.com/crist6494/Python-for-Data-Science-Piscine',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    installer='pip'
)
