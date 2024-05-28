# EPLWiki
A non-official repository of explanations, advices and tips about the life at EPL by the students of the [EPL Discord](https://discord.gg/3ZH2YWhsCa).

## Installation and build

Execute the following commands in the repository's root directory

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -R requirements.txt
make [html|latex]
``` 
Next, check the `./source/[html|latex]` folder. You should be able to find the result of your build. The LaTeX version generates a second Makefile to execute by simply typing `make` in the LaTeX build directory. The PDF should be available in the same directory.

## TODO
### Pages
 - [ ] Home page
 - [ ] Tutorats
 - [ ] Erasmus
 - [ ] Drive
 - [ ] Discord
 - [ ] Cours (liste de ressources externes par cours)

### Other
 - [ ] When a link is pinned in a Discord course channel, the bot makes a PR to add this link to the concerned course's links list

