# Git Multiple Accounts SSH Setup

## Introduction

This little was created to automate the setup of my git dev environnement. I'm using multiple git accounts (work private, work public, personal etc...).  
Using different accounts on the same computer can get quite messy if not configured properly.

## How to use it

I think that it can't be simpler than that.

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

## Todo

I wan't to specify here all the things that could be improved : 
- [ ] Detection of already existing profiles in the configuration files. For now, it will always add a new one, even if the exact same already exists.
- [ ] GPG keys management
- [ ] Better documentation overall
- [ ] Add more parameters to both GIT configs and SSH ones.

## Authors

- [ANJOU Raphaël | Orange Business](https://github.com/orange-anjou)