# The WearableLearning Game Analysis Tool
This tool enables the analysis of the finite state machine JSON representations of WearableLearning games for research.

# Working on this Project

## Setup
Setup your development environment and download the necessary tools you'll need. This may include your IDE (e.g., Visual Studio Code) and programming tools and libraries (e.g., Python and related libraries).

Make sure to also download Git for version control. There are many tutorials online (e.g., https://docs.github.com/en/get-started/quickstart/hello-world) if you still need to learn how to work with Git and GitHub for version control.

Clone this repo into your local machine. Make sure to clone this in a directory you will remember so you know where to access your files.

## Development Workflow

The production branch for this project is `main`. This means that the `main` branch houses the **working** and **most stable** version of the project. This has several implications on the development workflow when working on code for the _WearableLearning Game Analysis Tool_.

Because `main` is the project's production branch, you will not want to create and develop changes _directly_ on the `main` branch. That said, any code or document that you want to **develop** and **test** before finalizing and deploying to production need to be done on a **development branch**. This allows us to have a separate safe environment to test things out without breaking the codebase in the `main` production branch. Once the codebase in the _development branch_ is stable, then it can be merged into the `main` branch.

The following is the team's workflow for developing the codebase for this project:

1. Create a **development branch** from `main` using the following naming convention: `dev-<your name>-<date the branch was created>`. For example, if Francisco wanted to create a _development branch_ from `main` on January 11, 2023, the following would be the name of his development branch: `dev-francisco-01112023`. Make sure that you shift (_i.e._ `checkout`) your working branch to this new development branch in your local working environment.

2. Develop and push changes to the codebase in your **development branch**. Again, make sure to check that you are pulling and committing code in the **development branch** that you created, and not the `main` branch.

3. When you're ready for your codebase to be tested, **create a pull request** and request reviewers for your code. For this project, the reviewers could either be [Francisco Castro](https://github.com/franciscastro), [Sai Gattupalli](https://github.com/sai-educ), or [Allison Poh](https://github.com/apoh3). The reviewers may give additional feedback for any bugs or revisions that need to be made on your codebase. Once the reviewer has approved your codebase and verified stability, they will merge your changes into the `main` branch.

# Code based, Analysis, and Result
## Set up: Tools and Modules
+ For local IDE: Setting up environment for **Ipython notebook** - just like Jupiter
+ For Google Colab: 
* Either use Google Drive or Upload manually data folder to Google Colab
* Go to Edit > Notebook Settings > Select GPU 
* Currently, Google Colab runs the code without any problem. However, some of the modules/libraries used may change over time, and new versions may have different syntax, so please check for the version if any error occurs. 
* Modules uses: transformers, torch, BERT
* Simple Run all when use Google Colab

## FSM and Manual data folder
For the data that you passed into the fsm-data and manual-analysis folder, it is important to use the same name (the JSON file name should match with the csv name file).

## The Code
Finding Loops and Conditional Part:
+ The results are now available in the “result_loop_if_else.txt” file. Data retrieval can be found in that file and treat it like a csv file.
+ Since the scarcity of the data we have, we actually remove 3 json files and wait until we get the manual analysis then we can re-add them. References are already presented in the code! All you have to do is comment out to re-add them.
+ The implementation of loops derives from the study of [detect cycle in a directed Graph by Geek For Geek](https://www.geeksforgeeks.org/detect-cycle-in-a-graph/)

Model to classify the children's text
+ The code is fully commented on in the ipynb file. The process would be extracting all of the text and then tokenizing them, creating a DataFrame that contains the input text and the output classes, building a model and then feeding the DataFrame to the model. 
+ Users also have to make sure that the json and csv files are in the same name. 
+ Currently, the complete version of the code is on Google Colab: [Text analyzation](https://colab.research.google.com/drive/1unju8IEMUfNFuNSi4zmcik0s6QUaCtzs)
+ To use the model, please ensure the type of the input feeding into the model. All input should be converted to the DataFrame, and follow the same step of preprocessing as the data that was used to train the model. 
+ The Result1.csv file contains the result of the model when running the following games (in this exact order):
* Hackers_IN
* IndianBoys_IN
* IndianGirls_IN
* MathParkour_US
* Raistar_IN
* fireballs20-us
+ Reference: Some of the code in this project (mainly the model) is adapted from the “Toxic Comment Classification Challenge” by Sebastion Raschka which can be found [here](https://www.kaggle.com/code/rasbtn/distilbert-v0/notebook). 
