# Welcome, contributors! :smiley:

All contributions are most welcome.

## Local setup

- Fork this repository (repo) (top right corner on this page in desktop view).
- [Clone](https://harshkapadia2.github.io/git_basics/#_git_clone) your forked repo.
- Install [Python 3.8.x](https://www.python.org/downloads/) **64-bit**.
- Create a [virtual environment](https://docs.python.org/3/library/venv.html#module-venv) (venv) and activate it.
- After activating the venv, run `pip install -r requirements.txt` in the root directory of the project to install all the dependencies.
- Create a `.env` file in the root directory and add `SECRET_KEY='<random_string>'` to it.
   - Please do not push the `.env` file to GitHub.
   - For hosting, the `SECRET_KEY` needs to be added to the `config vars` (environment variables) of the hosting service.
- Activate the venv and run `python app.py` to start the web app on `localhost:5000` by default.
- Make your contribution(s)!
   - If any new package has been used, please run `pip freeze > requirements.txt` in the root directory and add the modified file to a commit.
- [Commit your work properly](https://harshkapadia2.github.io/git_basics/#_git_commit).
- Push to your forked repo.
- Create a PR! ([Learn how to make a PR](https://github.com/firstcontributions/first-contributions))

### Further help

Do not hesitate to contact me via [Twitter (@harshgkapadia)](https://twitter.com/harshgkapadia), [LinkedIn (@harshgkapadia)](https://www.linkedin.com/in/harshgkapadia/) or e-mail (harshgkapadia@gmail.com).
