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

1. Create a **development branch** from `main` using the following naming convention: `dev-<your name>-<date the branch was created>`. For example, if Francisco wanted to create a _development branch_ from `main` on January 11, 2023, the following would be the name of his development branch: `dev-francisco-01112023`. Make sure that you shift your working branch to this new development branch in your local working environment.

2. Develop and push changes to the codebase in your **development branch**. Again, make sure to check that you are pulling and committing code in the **development branch** that you created, and not the `main` branch.

3. When you're ready for your codebase to be tested, **create a pull request** and request reviewers for your code. For this project, the reviewers could either be [Francisco Castro](https://github.com/franciscastro), [Sai Gattupalli](https://github.com/sai-educ), or [Allison Poh](https://github.com/apoh3). The reviewers may give additional feedback for any bugs or revisions that need to be made on your codebase. Once the reviewer has approved your codebase and verified stability, they will merge your changes into the `main` branch.