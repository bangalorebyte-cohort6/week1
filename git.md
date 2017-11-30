# Git, Github, and Your SSH Connection

* Git is the toolkit for programming collaboration and version control.

## Introduction

* First thing first. Git is NOT the same as Github
* Git is a version control system that is used to store and navigate information
* Github is a web service that utilizes Git. There are other services similar to Github such as Bitbucket and Gitlab. Github is currently the most popular and the one we will all be using for this class.

![git does not equal github](http://1.bp.blogspot.com/-WY2YpNr3W6g/UY6tZAc-H3I/AAAAAAAABLY/xJ9x3wIY8V8/s440/Github2.png)


## Command / Necessary Git Commands

### Initializing a repository

*  `git init` - This will initialize the folder you are currently in as a git repository

### Save your changes

* `git add <filename>` - a new file / edits to a specific file will be staged and ready to be committed to a repository
* `git add .` - the dot notation will target everything in your current directory. All new / updated files will be staged
* `git commit -m <message>` - commits changes you've made to the repository. The message will be wrapped in quotes and can be anything you want. usually it will describe the updates you are committing.

### Working with Remotes

* `git remote add <remote_name> <url>` - We can connect a folder to a repo with a remote url.
* `git remote rm <remote_name>` - This will remove a remote that was added earlier
* `git remote -v` - list all remotes
* `git push <remote_name> <branch>` - push your changes to a remote git repository
* `git pull <remote_name> <branch>` - pull and merge any changes from a remote git repository
* `git clone <url>` - copy a repository from github. This will pull everything down into a new folder

### Helpful Commands

* `git checkout -b <branch_name>` - Make your own branch on that repo so you don't interfere with the master branch
* `git checkout <branch_name>` - Move between branches inside of the repo
* `git help` - list possible git commands
* `git status` - will show you your current branch, and what files have been changed
* `git log` - show the commit history
* `git diff` - show the changes between commits / commit and working tree
* `git config --global user.name "John Doe"` - use this to attach a name to the commits. Make sure the name is in quotes
* `git config --global user.email johndoe@example.com` - use this to attach an email to commits. Make sure the email is in quotes


## Git History

* It was invented by [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds) while he was inventing Linux
* In short he invented Git to help him keep his versions organized while inventing Linux
* Feel free to [read more here](https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git) or google some history on your own time. Pretty cool stuff


## What is Git?

* So what the hell is git?
* It is a version control too that you can run from your terminal
* Programmers use git so they can track the history of changes made on specific projects
* We can also use git to undo changes as far back as we want (or at least have committed to)
* Git also allows us to have multiple people working on the same projects simultaneously
	* Similar to how google docs can have multiple people editing a file at the same time


## What is a repository?

* This is just a codebase in git.
* Git repos will be connected to a specific folder to your laptop


## What is Github?

* A web service that utilizes Git
* Acts as a social network for programmers
	* As mentioned earlier, there are many web services that do this. Github is just the most popular
* You should all have an account on Github
* You will be able to put your own code on Github
* View your classmates codes
* And work on a project with multiple people


## Basic Git Workflow

***Making your own repo***

1. Make a new directory with `mkdir directory_name`
2. Go into that directory with change directory `cd directory name`
3. Initialize a new repository with `git init`
4. Create a README.md file or any file you want to send to GitHub `touch README.md`
5. Write something in the file and stage it `open README.md` and save something
6. Add entire directory and all files within `git add .`
7. Commit entire directory with `git commit -m "your save text"`
7. Create a new repo on your Github account by visiting your profile, clicking the `+` on the top right and creating a new repo
8. Connect that repo to your directory (make sure you are in the right folder)
	9. You can copy the `ssh` link in the directory and paste it into the initilized folder using `git remote add origin url_you_copied`
9. Push to your repository with `git push origin master`

***Pulling down somebody elses EXISTING Github repo. Then creating your own branch***

1. Change directory into the folder you want this repository to be copied to
2. When you copy this repo it will create IT'S OWN REPO FOLDER inside the current directory
3. Go to the repo you want to copy and take the "ssh" link
4. Go back to your bash/terminal window and clone the repository using `git clone ssh_url`
5. If you list out the items in the folder `ls` you should see the new repository
6. Change directory into it `cd repo_name`
7. Make a new branch for your own edits using `git checkout -b the_branch_name_you_want`
8. Now you can jump between your branch, the master branch, or any other branches using the `git checkout branch_name` command
9. If you made any edits and want to push up your own branch make sure you are in the branch you intend to push. You can check this using the `git status` command
10. Add branch `git add .`
11. Commit the branch files `git commit -m "my branch save"`
12. Push up YOUR branch `git push origin branch_name`
13. Now if you check the repository on github that branch should appear in the drop down menu.

## SSH

* I mentioned `ssh` several times in the lesson above
* SSH stands for secure shell and basically allows two programs to securely connect to each other
* In this case we are putting an ssh key onto our github account so Github knows that specific device is okay.
* This way we don't have to put in our login credentials / authenticate every time we pull or push to a github repo
* To add an ssh key to your github account [follow these directions](https://help.github.com/articles/generating-an-ssh-key/)
* There are four main steps
	* Checking if you have a ssh key
	* Generating a new ssh key and adding it to the ssh-agent
	* Add the ssh key to your github account
	* Testing the SSH connection
