


# imgdiff

imgdiff tool automates the process of comparing image pairs to check if they are similar or not and produces a score that quantifies the comparison by providing a score between 0 to 1, 0 being exactly identical. 


# How to use the tool

The tool is published in the pypi repository and the latest version can be installed with just a single line of command.

### Prerequisites 
1. Python should be installed version 3 and above.
2. Python package manager "pip" should be installed.
### Installation
Open a terminal and paste:

`pip install imgdiff` 

>This will download the tool and set it up by installing all its dependencies 

### Execution
The module imgdiff takes a command line argument, i.e the path to the location of the csv file which needs to be provided when running it like in the example below

``  python -m imgdiff.diff C://path to csv file ``
>The tool will execute and a comparison_results.csv file will be generated in the directory the command was run.
