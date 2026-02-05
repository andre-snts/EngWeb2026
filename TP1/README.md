## TCP 1

### Metainformação

* **Título:** Definição de um website a partir de um *script* python e um dataset
* **Data:** 4 fevereiro 2026
* **Autor:** André Santos
* **UC:** Engenharia Web

___

### Autor

* **Nome:** André Santos
* **Número:** a106854 \
![foto]()

___

### Resumo

Análise do dataset `dataset_reparacoes.json` sobre as intervenções realizadas numa oficina automóvel;

Definir a estrutura de um website de exploração do dataset:

* Página principal: lista de dados consultáveis;

* Listagem das reparações: Data, nif, nome, marca, modelo, número de intervenções realizadas;

* Listagem dos tipos de intervenção: lista alfabética de código das intervenções - código, nome e descrição;

* Listagem das marcas e modelos dos carros intervencionados: lista alfabética das marcas e modelos dos carros reparados - marca, modelo, número de carros;

* Página da Reparação: página com toda a informação de uma reparação;

* Página do tipo de intervenção: dados da intervenção (código, nome e descrição) e lista de reparações onde foi realizada;

* Página do marca/modelo: idem...

Criar uma ou várias scripts em Python para gerar o website a partir do dataset.

___

### Lista de Resultados

* [dataset_reparacoes.json](dataset_reparacoes.json) : dataset utilizado

Código:

* [build.py](src/build.py) : entrada do programa que gera o website.
* [render](src/render/) : diretório que possui o *html* base das diferentes páginas.
* [model](src/model.py) : normaliza o *json* reparacoes e cria índices por intervenção e veículo.
* [utils](src/utils.py) : *helpers* para html, ficheiros e diretórios.

Páginas web:

* [index.html](www/index.html) : página principal do website com os links para as três listas.
* [reparacoes.html](www/reparacoes.html) : página com a lista das reparações.
* [intervencoes.html](www/intervencoes.html) : página com a lista das intervenções.
* [veiculos.html](www/veiculos.html) : página com as listas das marcas e dos modelos.

**Nota:** As páginas individuais não se encontram neste repositório. Pelo facto de serem mais de 10000.

Para gerar o website completo basta correr o script:
```bash
python3 -m src.build
```