import os
from ..utils import esc, slug, page, write_file, html_table
from ..model import n_intervencoes


def render_list(outdir, reparacoes):
    rep_rows = []
    for r in sorted(reparacoes, key=lambda x: (str(x["data"]) or ""), reverse=True):
        nint = n_intervencoes(r)
        rep_href = f"./reparacoes/reparacao{r['rid']}.html"
        rep_rows.append(f"""
<tr>
  <td>{esc(r["data"])}</td>

  <td>{esc(r["nif"])}</td>

  <td>{esc(r["nome"])}</td>

  <td>{esc(r["marca"])}</td>

  <td>{esc(r["modelo"])}</td>

  <td>{esc(nint)}</td>

  <td>
    <a href="{rep_href}">abrir</a>
  </td>
</tr>
""")

    headers = """
<th>Data</th>
<th>NIF</th>
<th>Nome</th>
<th>Marca</th>
<th>Modelo</th>
<th>Nº intervenções</th>
<th></th>
""".strip()

    rep_body = html_table(headers, rep_rows)
    write_file(os.path.join(outdir, "reparacoes.html"),
        page("Listagem das reparações", rep_body, "index.html", "Voltar ao Índice"))


def render_details(outdir, reparacoes):
    for r in reparacoes:
        nint = n_intervencoes(r)
        veh_href = f"../veiculos/{slug(r['marca'])}__{slug(r['modelo'])}.html"

        it_rows = []
        for it in r["intervencoes"]:
            if not isinstance(it, dict):
                continue

            code = it.get("codigo", "")
            it_href = f"../intervencoes/{slug(code)}.html" if code else ""
            code_cell = f'<a href="{it_href}">{esc(code)}</a>' if code else ""
            it_rows.append(f"""
<tr>
  <td>{code_cell}</td>

  <td>{esc(it.get("nome",""))}</td>

  <td>{esc(it.get("descricao",""))}</td>
</tr>
""")

        it_headers = """
<th>Código</th>
<th>Nome</th>
<th>Descrição</th>
""".strip()

        it_empty = '<tr><td colspan="3">(sem intervenções)</td></tr>'
        it_table = html_table(it_headers, it_rows, empty_row_html=it_empty)

        rep_detail = f"""
<ul>
  <li>
    <strong>Data: </strong>{esc(r["data"])}
  </li>

  <li>
    <strong>NIF: </strong>{esc(r["nif"])}
  </li>

  <li>
    <strong>Nome: </strong>{esc(r["nome"])}
  </li>

  <li>
    <strong>Marca: </strong>{esc(r["marca"])}
  </li>

  <li>
    <strong>Modelo: </strong>{esc(r["modelo"])}
  </li>

  <li>
    <strong>Matrícula: </strong>{esc(r["matricula"])}
  </li>

  <li>
    <strong>Número de intervenções: </strong>{esc(nint)}
  </li>

  <li>
    <strong>Marca/Modelo: </strong>
    <a href="{veh_href}">{esc(r["marca"])} / {esc(r["modelo"])}</a>
  </li>
</ul>

<hr>

<h4>Intervenções</h4>
{it_table}
"""
        write_file(os.path.join(outdir, "reparacoes", f"reparacao{r['rid']}.html"),
            page(f"Página da Reparação {r['rid']}", rep_detail,
                  "../reparacoes.html", "Voltar à Página das Reparações")
        )