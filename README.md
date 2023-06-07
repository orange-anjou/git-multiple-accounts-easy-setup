# Git Multiple Accounts SSH Setup

## Introduction

This little was created to automate the setup of my git dev environnement. I'm using multiple git accounts (work internal GitLab, work external GitHub, personal etc...).  
Using different accounts on the same computer can get quite messy if not configured properly.

## How does it work ?

In order to have a clean separation between all the GIT accounts, we use different folders. This means that we could for example have : 
- PersonalProjects/
- WorkProjects/
- FreelanceProjects/
Each of these directories will have a different GIT account and will automatically be configured to use the right SSH keys.

To configure everything, we have to modify the following files : 
- `~/.ssh/config`
- `~/.gitconfig`

But we also have to create specific files.  

We have the account specifics git configurations :  
- `~/.gitconfig-account01`
- `~/.gitconfig-account02`

We also have the different SSH keys that will be created : 
- `~/.ssh/key-account01`
- `~/.ssh/key-account01.pub`
- `~/.ssh/key-account02`
- `~/.ssh/key-account02.pub`

## How to use it ?

### Prerequities

The only requirement is to have `ssh-keygen` installed as this is the tool used to generate the SSH keys.

### Explanations

You must first clone the repository.

```bash
git clone git@github.com:orange-anjou/git-multiple-accounts-ssh-setup.git
cd git-multiple-accounts-ssh-setup
```

You then have to rename the configuration example file.

```bash
mv profiles_config.example.py profiles_config.py
```

Next, you can edit this file to specify your configuration. You can add as many profile as you want in the profiles list.  
I will add more precise explanations later.  
For now, you can find more information here : 
- [SSH configuration](https://goteleport.com/blog/ssh-client-config-file-example/) 
- [GIT configuration](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration)

Once you have configured all your profiles, you can execute the following.

```bash
python3 main.py
```

You will see in the output of the script that the public keys created are displayed. It is done on purpose to allow you to easily add those keys to some services like GitHub or GitLab in order to connect to them if needed.

## Todo

I wan't to specify here all the things that could be improved : 
- [ ] Detection of already existing profiles in the configuration files. For now, it will always add a new one, even if the exact same already exists.
- [ ] GPG keys management
- [ ] Better documentation overall
- [ ] Add more parameters to both GIT configs and SSH ones.

## Authors

- [ANJOU Raphaël | Orange Business](https://github.com/orange-anjou)