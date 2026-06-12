Esse código tem o objetivo de automatizar a organização de um repositório seja criando arquivos .gitkeep em diretorios vazios ou apagando os arquivos .gitkeep de pastas que já contem algum tipo de arquivo. Além disso, o programa salva em um arquivo json todas as mudanças que o programa fez automaticamente com a data e hora. Para que o programa funcione, ele usa as bibliotecas datetime, os e json.

Explique as diferenças entre:
• json.dump() vs json.dumps()
Ambos são parecidos com a entrada sendo um objeto, mas a diferença entre eles é que no json.dump() o resultado é retornado em um arquivo Json. No json.dumps() o retorno é uma string Json.
• json.load() vs json.loads()
No json.load() você recebe de entrada um arquivo json e retorna os dados em um objeto. No json.loads() você também recebe de entrada um arquivo json, mas retorna esses dados no formato de string.

