import os
from ..utils import esc, slug, page, write_file, html_table


def render_list(outdir, interv):
    int_rows = []
    for code in sorted(interv.keys(), key=lambda x: str(x).lower()):
        it = interv[code]
        href = f"./intervencoes/{slug(code)}.html"
        int_rows.append(f"""
<tr>
  <td>
    <a href="{href}">{esc(it["codigo"])}</a>
  </td>

  <td>{esc(it["nome"])}</td>

  <td>{esc(it["descricao"])}</td>
</tr>""")

    headers = """
<th>Código</th>
<th>Nome</th>
<th>Descrição</th>
""".strip()

    int_body = html_table(headers, int_rows)
    write_file(os.path.join(outdir, "intervencoes.html"),
        page("Listagem dos tipos de intervenção", int_body, "index.html", "Voltar ao Índice")
    )


def render_details(outdir, interv):
    for code in sorted(interv.keys(), key=lambda x: str(x).lower()):
        it = interv[code]

        rep_links = []
        for rid in it["rids"]:
            rep_links.append(f'<li><a href="../reparacoes/reparacao{rid}.html">Reparação-{rid}</a></li>')

        rep_list = f"""
<ul>
  {''.join(rep_links) if rep_links else "<li>(nenhuma)</li>"}
</ul>
"""

        int_detail = f"""
<ul>
  <li>
    <strong>Código: </strong>{esc(it["codigo"])}
  </li>

  <li>
    <strong>Nome: </strong>{esc(it["nome"])}
  </li>

  <li>
    <strong>Descrição: </strong>{esc(it["descricao"])}
  </li>

  <li>
    <strong>Reparações onde foi realizada: </strong>
    {rep_list}
  </li>
</ul>
"""
        write_file(os.path.join(outdir, "intervencoes", f"{slug(code)}.html"),
            page(f"Página do tipo de intervenção {code}", int_detail,
                "../intervencoes.html", "Voltar à Página das Intervenções")
        )