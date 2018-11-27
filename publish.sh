#!/bin/bash
function showHelp()
{
    echo "Usage: ./publish.sh [test]"
    exit 0
}

function publishTest()
{
    git checkout master
    git pull
    python ./src/doc.py all

    mkdocs serve
}

function publish()
{
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
        jsdoc $CSC_PATH/plugins/gpg/js/script/sdkboxgpg.js -d api/gpg/js
        mkdir -p site/api
        cp -R api/ site/api
    fi

    mkdocs gh-deploy
}

function checkenv()
{
    if command -v jsdoc >/dev/null 2>&1; then
        echo "jsdoc exists."
    else
        echo "> Please install jsdoc"
        echo "npm install jsdoc -g"
        exit 0
    fi

    if [ -z "$CSC_PATH" ]; then
        echo "> Need to set CSC_PATH to generate"
        exit 0
    fi

    which jsdoc
    echo "$CSC_PATH"
}

checkenv;
# main
if [ $# -eq 0 ]; then

    publish;
elif [ $# -eq 1 ] && [ $1 = 'test' ]; then
    publishTest;
else
    showHelp;
fi
