# itinerant-futurizer

See: http://python-future.org/futurize_cheatsheet.html

* git clone [url]
* cd [reponame]
* git checkout -b futurize-stage-1
* pip install future
* futurize --stage1 -w **/*.py
* git commit --all -m "futurize --stage1 -w **/*.py"
* git push --set-upstream origin futurize-stage-1

> remote: Permission to bfelbo/DeepMoji.git denied to cclauss.

> fatal: unable to access 'https://github.com/bfelbo/DeepMoji/': The requested URL returned error: 403

https://stackoverflow.com/questions/6286571/are-git-forks-actually-git-clones

So...  If you do not have write access to the repo then you must fork the repo (upstream) into a repo (origin) in your own GitHub account.  You then make changes and commits to a repo (local) on your computer and push those changes from local to origin.  Then you can can create a pull request to suggest that changes move from origin to upstream.

There are two problems with automating this process.  Neither git CLI nor [github3.py](https://github3.readthedocs.io/en/develop/github.html) support:
1. creating a fork
2. creating a pull request

New proposal:



