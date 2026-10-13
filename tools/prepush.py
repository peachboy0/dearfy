import subprocess

import toml

# ! Functions

def replaces(src: str, **kwargs: str) -> str:
    for old, new in kwargs.items():
        src = src.replace(old, new)
    return src

def clear(src: str, remove_chars: str = '\a\t\r\n ') -> str:
    for remove_char in remove_chars:
        src = src.replace(remove_char, '')
    return src

def get_git_repo_version() -> str:
    ver = clear(subprocess.check_output(['git', 'describe', '--tags']).decode())
    if len(ver.split('-')) == 3:
        main, commit, commit_hex = ver.split('-')
        return f"{main}-{commit}+{commit_hex}"
    else:
        return ver

# ! Main

def main():
    with open("pyproject.toml", "r") as f:
        pyproject_data = toml.load(f)
    pyproject_data['project']['version'] = get_git_repo_version()
    print(pyproject_data)
    with open("pyproject.toml", "w") as f:
        toml.dump(pyproject_data, f)

# ! Run

if __name__ == '__main__':
    main()