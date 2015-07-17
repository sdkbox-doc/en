#!/usr/bin/python
# coding=utf-8

import subprocess

subprocess.Popen(["git", "fetch"], cwd=template_dir).wait()
subprocess.Popen(["git", "checkout", "gh-pages "], cwd=template_dir).wait()
subprocess.Popen(["git", "pull"], cwd=template_dir).wait()
subprocess.Popen(["git", "checkout", "master"], cwd=template_dir).wait()
subprocess.Popen(["git", "pull"], cwd=template_dir).wait()
subprocess.Popen(["mkdocs", "gh-deploy", "--clean"], cwd=template_dir).wait()