#!/usr/bin/python
# coding=utf-8

import subprocess

subprocess.Popen(["git", "fetch"]).wait()
subprocess.Popen(["git", "checkout", "gh-pages "]).wait()
subprocess.Popen(["git", "pull"]).wait()
subprocess.Popen(["git", "checkout", "master"]).wait()
subprocess.Popen(["git", "pull"]).wait()
subprocess.Popen(["./src/doc.py", "all"]).wait()
subprocess.Popen(["mkdocs", "gh-deploy", "--clean"]).wait()