# koalas
For now, is just a small matematical and statistical Python module


## table
Creates/display a table from given informations

### Example
```python
from koalas import *
info = [
        ["Nome", "Idade", "Curso"],
        ["Fulano", 20, "Engenharia"],
        ["Cicrano", 31, "Letras"],
        ["Genoveva Antao Bezerra", float('inf'), "Biologia"]
       ]
table.show_from_data(info)
          Nome          | Idade |   Curso    |
==============================================
         Fulano         |  20   | Engenharia |
        Cicrano         |  31   |   Letras   |
 Genoveva Antao Bezerra |  inf  |  Biologia  |


tabela = table(info)
tabela.show()
          Nome          | Idade |   Curso    |
==============================================
         Fulano         |  20   | Engenharia |
        Cicrano         |  31   |   Letras   |
 Genoveva Antao Bezerra |  inf  |  Biologia  |
```
