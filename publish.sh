
#!/bin/bash

git branch -D "gh-pages"
git fetch
git checkout -b "gh-pages"  origin/gh-pages
git pull
git checkout 1.3
git pull
python ./src/doc.py all
mkdocs gh-deploy --clean
