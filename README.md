
## Tomato + task = tomask

a file organization task for Tomato +.

---

### requirements

1. sort all 1k files into folders depening on the language
    1. `arabic-*` -> `arabic/`, `english-*` -> `english/` . . .
1. bear in mind future proofability and readability
1. no external libraries

---

### design

#### ***Performance***
>
>performance of the script is not really a factor cause we rely on the host OS to do the work, as we are only moving files and not doing any kind of work on them.

#### **config file** *vs* **args**
>
> i've wanted to use `toml` but as it is not in the core python libs its out!

> i considered using `click`, `argparser` or a `config` file, after dwelling on it for a bit a `config` file will tie you down so i went with `arg parser` for simplicity.

### **code**
>
> organized by 4 functions that use each other cause simplicity rules

#### **Documentation**
>

- done via [sphinx](https://www.sphinx-doc.org/en/master/usage/quickstart.html)

> any function prefixed with `_` will not show up in the docs

## to build the docs

```powershell
sphinx-apidoc -F -H Tomato-Task  -A Canaan  -V 0.0.1 -o .\docs\ .\task\
sphinx-build -b html .\docs\ .\docs\_build # every time u make a change
```

can be accessed from: `docs/_build/index.html`

---

## how to run ?

```bash
 git clone https://github.com/CanaanGM/Tomato_Task
 cd Tomato_Task\task
 python organize_language_files.py 
 # or
 python organize_language_files.py -s <path to source files> -d <path to where to organize>

```
