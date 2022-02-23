# GIT

```shell
apt install git
```

```shell
ssh-keygen
```

```python
from flask import Flask
```

`количество файлов * количество разработчиков * количество изменений = количество модификаций проекта`

- история
- возврат к предыдущей версии файла
- распределённый доступ

```shell
mkdir test && cd test

git --version         # get git version

git init              # initial gir repository

git branch -m main    # change branch name

git log               # history
```

### `git status`
```shell
git status            # get state of repository
```

### `git add <file name>`
Подготовка файла к коммиту
```shell
git add file.txt      # add one file

git add file1.txt, file2.txt, file3.txt  # add many files

git add .             # add all files

git add *.py          # add all python files
```

### `git commit`
```shell
git commit                          # без комментария - откроется текстовый редактор (установленный по умолчанию)

git commit -m 'Commit some files'   # с комментарием
```

### `git log`
```shell
git log
```
