


# imgsimilarity
![Python package](https://github.com/RealNameHidden/imgsimilarity/workflows/Python%20package/badge.svg) ![Upload Python Package](https://github.com/RealNameHidden/imgsimilarity/workflows/Upload%20Python%20Package/badge.svg)

imgsimilarity tool automates the process of comparing image pairs to check if they are similar or not and produces a score that quantifies the comparison by providing a score between 0 to 1, 0 being exactly identical. 


# How to use the tool

The tool is published in the pypi repository and the latest version can be installed with just a single line of command.

### Prerequisites 
1. Python should be installed version 3 and above.
2. Python package manager "pip" should be installed.
### Installation
Open a terminal and paste:

`pip install imgsimilarity` 

>This will download the tool and set it up by installing all its dependencies 

### Execution
The module imgsimilarity takes a command line argument, i.e the path to the location of the csv file which needs to be provided when running it like in the example below

``  python -m imgsimilarity.diff C://pathtocsvfile ``
>The tool will execute and a comparison_results.csv file will be generated in the directory the command was run.
>
>The input csv file is expected to have the data in the format of (img1,img2).
>
>If executing in a linux or mac os env, ensure the file path is enclosed with quotes "/path/to/csv/file" or "//path//to//csv//file"
>
>Hint: to test the tool you can download the sample file and images in the folder imgsimilarity/tests/resources/ in this repo. (You will have to edit the data inthe csv file based on the path of the folder on your local)

## How does the tool work?

The tool uses dhash algorithm to find a hashcode for each image and then find how many bits differ between the hashcodes to find the score for similarity. Identical images have 
difference as 0.

The dhash pypi module is being used here, its an out of the box python module to compute hashes and determine the difference for images.
The hash for an image is stored in a dictionary to avoid repeated execution of dhash function and this reduces the cost of similarity detection.
The execution time for each pair is calculated by taking the difference of process time at the start of the iteration and the process time at the end of the iteration.

Below is a flowchart that briefly illustrates how the tool functions.


![alt text](https://inse-6250-40082192.s3.amazonaws.com/imgdiff+flow+chart.jpg)


## How does the tool achieve hassle free installation and usage?

It is by using the Python Package Index repository!

Once the latest code is pushed and tagged, the gitlab ci is configured to run pytests to make sure the code works and the once the tests succeed it creates the build and a distributable with the help of setup.py file and twindle.
and its uploaded to the PyPi Repository automatically.

The user can install the latest version using pip install or upgrade command. Thanks to the setup.py file all the dependencies are installed automatically 

![alt text](https://inse-6250-40082192.s3.amazonaws.com/pipeline_flowchart.jpg)


#### Reference:
>PyPi repo: https://pypi.org/project/imgsimilarity/
>dhash : https://pypi.org/project/dhash/


>#### note
>The source code is well documented and pydoc can be genrated.
