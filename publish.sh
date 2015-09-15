
#!/bin/bash

git branch -D "gh-pages"
git fetch
git checkout -b "gh-pages"  origin/gh-pages
git pull
git checkout master
git pull
python ./src/doc.py all
mkdocs gh-deploy --clean
