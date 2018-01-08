#!/usr/bin/env python3

import getpass
import sys
from collections import namedtuple

try:
    from subprocess import getstatusoutput  # Python3
except ImportError:
    from commands import getstatusoutput    # Python2

GITHUB_USERNAME = getpass.getuser()  # Assume local username == GitHub username

commands = """git clone {fork_url}
cd {repo_name}
git checkout -b modernize-python2-code
python2 -m flake8 . --count --select=E901,E999,F821,F822,F823 --show-source
python3 -m flake8 . --count --select=E901,E999,F821,F822,F823 --show-source"""

next_steps = """Next steps:
cd {repo_name} ; zsh
futurize --stage1 -w **/*.py ; exit
python2 -m flake8 . --count --select=E901,E999,F821,F822,F823 --show-source
python3 -m flake8 . --count --select=E901,E999,F821,F822,F823 --show-source
git commit --all -m "Modernize Python 2 code to get ready for Python 3"
git push --set-upstream origin modernize-python2-code
open {fork_url}
"""

# def getPythonMajorVersion():
#    return int(sys.version[:3].split('.')[0])


def shellCommand(inCommand):
    return getstatusoutput(inCommand)  # .splitlines()


def cmd(inCommand):  # do the command, ignore error code and return its output
    return shellCommand(inCommand)[1]


def printCmd(inCommand):  # print the command and its output
    theResult = cmd(inCommand)
    if 'command not found' not in theResult:
        print('{:34} = {}'.format(inCommand, theResult))


def get_repo_info(upstream_url):
    repo_info = namedtuple('repo_info', 'repo_name upstream_url fork_url')
    fork_url = upstream_url.split('/')
    repo_name = fork_url[-1]
    fork_url[-2] = GITHUB_USERNAME
    return repo_info(repo_name, upstream_url, '/'.join(fork_url))


def main(args):
    if not args:
        print("""You gotta give me a url to work with.""")
        sys.exit()

    repo_info = get_repo_info(args[0])
    print(repo_info)
    script = commands.format(**repo_info._asdict())
    print(script)
    with open('futurizer_temp.sh', 'w') as out_file:
        out_file.write(script)
    printCmd('chmod +x futurizer_temp.sh')
    printCmd('./futurizer_temp.sh')
    print('\nRemember to:')
    print(next_steps.format(**repo_info._asdict()))


if __name__ == '__main__':
    main(sys.argv[1:])
