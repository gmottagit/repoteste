Esse código tem o objetivo de automatizar a organização de um repositório seja criando arquivos .gitkeep em diretorios vazios ou apagando os arquivos .gitkeep de pastas que já contem algum tipo de arquivo. Além disso, o programa salva em um arquivo json todas as mudanças que o programa fez automaticamente com a data e hora. Para que o programa funcione, ele usa as bibliotecas datetime, os e json.

A lógica do programa é:
1. Diretórios não vazios:
• Caso o diretório contenha arquivos ou subdiretórios:
⋄ O arquivo .gitkeep não deve existir;
⋄ Caso exista, ele deve ser removido.

2. Diretórios vazios:
• Caso o diretório não contenha arquivos nem subdiretórios:
⋄ Um arquivo .gitkeep deve ser criado.

3. O diretório logs não deve ser processado pelo algoritmo, ou seja, não
deve ser verificado nem sofrer alterações.

O programa também deverá:
- Criar um diretório chamado logs, caso não exista;
- Criar (ou atualizar) um arquivo log.json dentro desse diretório;
- Registrar, a cada execução: Arquivos .gitkeep criados; Arquivos .gitkeep removidos; Data e hora da execução.

  -----------------------
Explique as diferenças entre:

• json.dump() vs json.dumps()
Ambos são parecidos com a entrada sendo um objeto, mas a diferença entre eles é que no json.dump() o resultado é retornado em um arquivo Json. No json.dumps() o retorno é uma string Json.

• json.load() vs json.loads()

No json.load() você recebe de entrada um arquivo json e retorna os dados em um objeto. No json.loads() você também recebe de entrada um arquivo json, mas retorna esses dados no formato de string.

