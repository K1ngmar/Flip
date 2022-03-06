
<p align="center">
  <img alt="flip <3" src="./flip.png" />
</p>

# 💖 Flip
#### ✨ A cool discord flaring bot ✨

# 📦 Content:
* [About](#-about)
* [Requirements](#-requirements)
* [Installation](#%EF%B8%8F-installation)

# 📝 About:

Flip will help you manage roles by making it possible for users to assign themselves the roles they desire °˖✧◝(⁰▿⁰)◜✧˖°

# 📋 Requirements:
This project uses **python3**

```bash
# brew:
$ brew install python3

# apt-get:
$ apt-get install python3
```

# ⚙️ Installation:

```bash
# Clone:
$ git clone https://github.com/K1ngmar/Flip.git

# Setup the .roles
$ vim config/.roles

# run:
$ python3 main.py

```
> Note that if you want to run this bot yourself make sure you have your bot's token as an *environment variable* named `token`

> Setting up roles in the .roles file should be done in the following fashion:  
```bash
[emoji]=[role name]
🖥️=Programmer
```
> responding to flips pinned message with this emoji will then grant you the programming role

# ✅ Features:

* Commands:
```Makefile
# -help
This will show you the help menu

# -roles
This will show all the roles flip is managing(the roles setup in the .roles file)

# -verysecretpincommand
This will make flip post a and pin a message that users will then be able to react with emoiji's on in order to gain roles
```
