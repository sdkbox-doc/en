
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

if [ -z "$CSC_PATH" ]
then
    echo "Need to set CSC_PATH to generate "
else
    echo "detects CSC_PATH"
    echo "Generating documentation for gpg"
    jsdoc $CSC_PATH/plugins/sdkboxgoogleplay/js/script/sdkboxgpg.js -d api/js/gpg
    mkdir -p site/api
    cp -R api/ site/api
fi

mkdocs gh-deploy
