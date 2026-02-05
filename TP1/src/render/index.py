import os
from ..utils import page, write_file


def render(outdir):
    index_body = """
<ul>
  <li>
    <a href="reparacoes.html">Listagem das reparações</a>
  </li>

  <li>
    <a href="intervencoes.html">Listagem dos tipos de intervenção</a>
  </li>

  <li>
    <a href="veiculos.html">Listagem das marcas e modelos</a>
  </li>
</ul>
"""
    write_file(os.path.join(outdir, "index.html"),
        page("Intervenções numa oficina automóvel", index_body))