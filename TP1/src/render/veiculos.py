import os
from ..utils import esc, slug, page, write_file, html_table
from ..model import n_carros


def render_list(outdir, veic):
    vm_rows = []
    for (marca, modelo) in sorted(veic.keys(), key=lambda k: (str(k[0]).lower(), str(k[1]).lower())):
        info = veic[(marca, modelo)]
        n = n_carros(info)
        href = f'./veiculos/{slug(marca)}__{slug(modelo)}.html'
        vm_rows.append(f"""
<tr>
  <td>
    <a href="{href}">{esc(marca)}</a>
  </td>

  <td>{esc(modelo)}</td>

  <td>{esc(n)}</td>
</tr>""")

    headers = """
<th>Marca</th>
<th>Modelo</th>
<th>Número de carros</th>
""".strip()

    vm_body = html_table(headers, vm_rows)
    write_file(os.path.join(outdir, "veiculos.html"),
        page("Listagem das marcas e modelos dos carros intervencionados", vm_body,
             "index.html", "Voltar ao Índice")
    )


def render_details(outdir, veic):
    for (marca, modelo) in sorted(veic.keys(), key=lambda k: (str(k[0]).lower(), str(k[1]).lower())):
        info = veic[(marca, modelo)]
        n = n_carros(info)

        rep_links = []
        for rid in info["rids"]:
            rep_links.append(f'<li><a href="../reparacoes/reparacao{rid}.html">Reparação-{rid}</a></li>')

        rep_list = f"""
<ul>
  {''.join(rep_links) if rep_links else "<li>(nenhuma)</li>"}
</ul>
"""

        vm_detail = f"""
<ul>
  <li>
    <strong>Marca: </strong>{esc(marca)}
  </li>

  <li>
    <strong>Modelo: </strong>{esc(modelo)}
  </li>

  <li>
    <strong>Número de carros: </strong>{esc(n)}
  </li>

  <li>
    <strong>Reparações: </strong>
    {rep_list}
  </li>
</ul>
"""
        write_file(os.path.join(outdir, "veiculos", f"{slug(marca)}__{slug(modelo)}.html"),
            page(f"Página do marca/modelo {marca} / {modelo}", vm_detail,
                  "../veiculos.html", "Voltar à Página dos Veículos")
        )