import setuptools

with open('Readme.md') as fp:
    long_description = fp.read()

with open('requirements.txt') as fp:
    requirements = fp.read()

setuptools.setup(
    
    name = 'text_preprocess',
    package_data={
        'text_preprocess': ['data/*.json'],  # Include all .json files in the data folder
    },
    include_package_data=True,
    version = '1.0',
    author= 'Onome Joseph',
    description = 'This is a text preprocessing package',
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'LICENSE :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires= '>=3.7',
    install_requires = [],
)
