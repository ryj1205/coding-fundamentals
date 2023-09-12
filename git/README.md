# Git Exercises

## Git Workflow

- Git Bash
- cd to your home dir `cd`
- Create a work dir  `mkdir exercise1`
- Change into new dir `cd exercise1`
- Initialize Git repo `git init`
- create two text files in folder and add some text
- Stage the new files `git add <filename>`
- commit the changes `git commit`
- edit the files and repeat the add and commit workflow two more times

## Git Cloning

- Create a repository in Github.
- Give the repo a a name
- Give the repo a description
- tick the box to create a README
- copy the clone https url from the green box
- on the CLI change back to your users home directory with `cd`
- run `git clone <url>`
- check the new directory has been created with `ls`
- change into the new repository directory `cd <reponame>`
- Edit the README, stage and commit the changes

## Git Pushing and Pulling

- Create a 'classic' PAT for your repo 
  - <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token>
  - make sure you choose the scope 'repo'
- copy the PAT to your local workstation
- on the CLI check your repo is clean with `git status`
- perform a `git push`
- in the authentication pop up choose **Token**
- add your token as the password
- In the GitHub web interface edit one of your files and commit the changes
- on yout CLI use `git pull` to retrieve the change
