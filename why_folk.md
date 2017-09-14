# itinerant-futurizer

See:
* http://python-future.org/futurize_cheatsheet.html
* https://stackoverflow.com/questions/6286571/are-git-forks-actually-git-clones

* git clone [url]
* cd [reponame]
* git checkout -b futurize-stage-1
* pip install future
* futurize --stage1 -w **/*.py
* git commit --all -m "futurize --stage1 -w **/*.py"
* git push --set-upstream origin futurize-stage-1

> remote: Permission to bfelbo/DeepMoji.git denied to cclauss.

> fatal: unable to access 'https://github.com/bfelbo/DeepMoji/': The requested URL returned error: 403

So...  If you do not have write access to the repo then __you must fork (not clone)__ the repo (upstream) into a repo (origin) in your own GitHub account.  You then make changes and commits to a repo (local) on your computer and push those changes from local to origin.  Then you can create a pull request to suggest that changes move from origin to upstream.

Back to [README.md]()
