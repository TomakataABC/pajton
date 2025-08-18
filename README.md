# Informatika 2023/2024

## Programy

### Průběh hodin

1. [První hodina – Základy I](01.py)
2. [Druhá hodina – TODO]()
3. [Třetí hodina – Základy II](03.py)
4. [Čtvrtá hodina – TODO]()

### Užitečné snippety

#### Formátování pomocí f-strings

```python
# Zdroj: https://builtin.com/data-science/python-code-snippets

# Formatting strings with f string.
str_val = 'books'
num_val = 15
print(f'{num_val} {str_val}') # 15 books
print(f'{num_val % 2 = }') # '=' na konci ukáže nejen výsledek, ale i levou stranu výrazu
print(f'{str_val!r}') # books

# Dealing with floats
price_val = 5.18362
print(f'{price_val:.2f}') # 5.18

# Formatting dates
from datetime import datetime
date_val = datetime.utcnow()
print(f'{date_val=:%Y-%m-%d}') # date_val=2021-09-24
```

## Návody

### Markdown

- https://jecas.cz/markdown
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes

### Codespaces

https://github.com/codespaces

- [Spolupráce ve sdíleném codespace](https://docs.github.com/en/codespaces/developing-in-codespaces/working-collaboratively-in-a-codespace)

### Klávesové zkratky

#### Speciální znaky na české klávesnici

| Znak | Jak |
| ----------- | ----------- |
| ` | ... |
| [ a ] | ... |
| / | Shift + ú |
| ... | ... |

#### Text

| Zkratka | Efekt |
| ----------- | ----------- |
| Ctrl + ←/→ | Posun o slovo |
| Shift a posuny výše | Označení posunu |
| ... | ... |

#### VSCode
