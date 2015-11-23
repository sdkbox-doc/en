
#!/bin/bash

BRANCHNAME=gh-pages

if [ `git branch --list ${BRANCHNAME} ` ]
then
   echo "Removing old ${BRANCHNAME} branch"
   git branch -D ${BRANCHNAME}
fi
git fetch
git checkout -b ${BRANCHNAME} origin/gh-pages
git pull
git checkout master
git pull
python ./src/doc.py all

plugins=('adcolony' 'agecheq' 'bee7' 'chartboost' 'facebook' 'flurryanalytics'
'fyber' 'googleanalytics' 'iap' 'kochava' 'review' 'soomlagrow' 'tune'
'valuepotion' 'vungle')

for i in ${plugins[@]}; do
    cp docs/plugins/${i}/index.html site/plugins/${i}/.
done

mkdocs gh-deploy #--clean
