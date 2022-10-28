# smack
_Smack is a cli application to create package folder structures for packages based on PyPi specifications_

## Installation
```bash
pip install smack
```

## Usage
```bash
smack [project-name]
```
## Folder structure
```bash
[name]_project
  -src 
    -[name]
      -__init__.py
      -[name].py
  -tests
  -LICENSE.txt
  -pyproject.toml
  -README.md
```