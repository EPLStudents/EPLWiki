# EPLWiki
Un recueil non-officiel d'explications, de conseils et d'astuces sur la vie à l'EPL par les étudiants du [Discord EPL](https://discord.gg/3ZH2YWhsCa).

## Installation and build

Execute the following commands in the repository's root directory

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -R requirements.txt
make [html|latex]
```
Next, check the `./source/[html|latex]` folder. You should be able to find the result of your build. The LaTeX version generates a second Makefile to execute by simply typing `make` in the LaTeX build directory. The PDF should be available in the same directory.

