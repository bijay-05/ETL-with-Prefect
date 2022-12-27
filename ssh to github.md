# ssh to github tips and tricks

# ssh public key generation in windows

>ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

### put is_rsa and id_rsa.pub files from C:\Users\Username\  to C:\Users\Username\.ssh\

## check if SSH is running or not

from git bash

$eval $ (ssh-agent -s)

## add the new SSH private key to SSH agent

$ssh-add ./.ssh/id_rsa

## verify that you have a private key generated and loaded into SSH

$ ssh-add -l -E sha256

## test the connection with command
## donot use username below, use as specified.

$ssh -T git@github.com

## Notice
Please donot use git config --list. It uses vim which cannot be closed.

# git guides to remove a value for configuration
$git config --global --unset user.name

$git config --global --unset user.email

# replacing git config details
$git config --global --replace-all user.name "new name"

$git config --global --replace-all user.email "new email"

# view all the remotes of local repo
$git remote -v

$git remote rm upstream

## delete a git branch
$git branch --delete branch_name

### while using SSH to authenticate with github,
### we should use ssh mode while cloning the remote repo in our local machine
### in such a way, while we push code to remote repo, ssh takes care of everything

### just use command $git push origin branch_name
### although you have not set origin for the repo, ssh takes care of it
