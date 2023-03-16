Heya~!

## Tomato + task = tomask

a file organization task by Tomato +.

---

### requirements

1. sort all 1k files into folders depening on the language
    1. `arabic-*` -> `arabic/`, `english-*` -> `english/` . . .
1. bear in mind future proofability and readability
1. no external libraries

---

### design

#### Performance
>
>performance of the script is not really a factor cause we rely on the host OS to do the work, as we are only moving files and not doing any kind of work on them.

#### config file vs args
>
> i've wanted to use `toml` but as it is not in the core python libs its out!

> i considered using `click` or `argparser` but settled on a `config` file so you can just run the script by `python <script.bye>`.

---

## how to run ?

```bash
 git clone https://github.com/CanaanGM/Tomato_Task
 cd Tomato_Task
 python organize_language_files.py 
```

alternativly put on some shoes and away u go!
