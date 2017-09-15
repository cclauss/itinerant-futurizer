# itinerant-futurizer

### Pre-work:
* `pip install future`  # http://python-future.org/futurize_cheatsheet.html
* `shopt -s globstar`   # on bash 4+  https://unix.stackexchange.com/questions/49913/recursive-glob
* Why __fork (not clone)__: https://stackoverflow.com/questions/6286571/are-git-forks-actually-git-clones
    * If __you do not have write access__ to the repo then [__you must fork (not clone)__](why_fork.md) the repo (upstream) into a repo (origin) in your own GitHub account.  You then make changes and commits to a repo (local) on your computer and push those changes from local to origin.  Then you can create a pull request to suggest that changes move from origin to upstream.

### Manual Process
1. Using the GitHub web ui, visit the repo to be processed and click "__fork__" in the upper right (_not_ clone).
2. $ git clone `https://github.com/<your GitHub username>/<repo name>`
3. $ cd [reponame]
4. git checkout -b modernize-python2-code
5. python2 -m flake8 . --count --select=E901,E999,F821,F822,F823 --show-source --statistics
6. `futurize --stage1 -w **/*.py`
7. python3 -m flake8 . --count --select=E901,E999,F821,F822,F823 --show-source --statistics
8. git commit --all -m "Modernize Python 2 code to get ready for Python 3"
9. git push --set-upstream origin modernize-python2-code
10. Refresh GitHub web ui and you should have a Pull Request to submit back to upstream.

### Automatic Process (WIP, pipe dream, not ready for prime time)
There are two problems with automating this process.  Neither git CLI nor [github3.py](https://github3.readthedocs.io/en/develop/github.html) support:
1. creating a fork
2. creating a pull request

New proposal:
1. Using the GitHub web ui, the user visits the repo to be processed and clicks "fork" in the upper right (_not_ clone).
2. User runs `itinerant_futurizer.py` locally and when asked provide their GitHub password.
3. At the end of processing, a web browser is opened to the `futurize-stage-1` branch of the origin repo.
4. User can create a pull request to suggest that changes move from origin to upstream.

Under this proposal, `itinerant_futurizer.py` does:
1. Ask user for their GitHub password
2. Get the last repo created and ask user to verify this is the repo that they want to process
3. Verify that branch futurize-stage-1 does not yet exist on origin.  If it does then bail.
4. If .travis.yml exists in that repo then rename it to was.travis.yml
5. travis enable -r user/repo  # https://github.com/travis-ci/travis.rb#enable
6. Push our .travis.yml into repo to kick off futurize stage 1
7. Remove our .travis.yml and restore was.travis.yml if present
8. Open webbrowser to branch futurize-stage-1 on origin

Our .travis.yml does:
1. git checkout -b futurize-stage-1
2. pip install future
3. futurize --stage1 -w **/*.py
4. git commit --all -m "futurize --stage1 -w **/*.py"
5. git push --set-upstream origin futurize-stage-1
6. rm .travis.yml
7. mv was.travis.yml .travis.yml

