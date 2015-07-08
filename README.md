# Intro
SDKBOX doc site uses mkdocs to generate static pages from markdown files

To view the site locally, you have to install mkdocs first

```
sudo pip install mkdocs
```

Then you can start a local server by
```
mkdocs serve
```
Open http://127.0.0.1:8000/ in browser

# Documents generator
We use generator to generate documents, so don't edit files in `docs/plugins/` manually.

Instead, use the following command to generate documents
```
cd src
./doc.py all
```

If you want to edit document, you should edit the templates at `src/<plugin name>`

# Publish

Use the following command to publish document to live
```
mkdocs gh-deploy --clean
```
