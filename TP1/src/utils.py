import html, json, os, re, shutil


def esc(x):
    return html.escape("" if x is None else str(x), quote=True)


def slug(x):
    s = "" if x is None else str(x).strip().lower()
    s = re.sub(r"\s+", "_", s)
    s = re.sub(r"[^a-z0-9_ -]", "", s)
    s = s.replace(" ", "_")
    s = re.sub(r"_+", "_", s).strip("_")
    return s or "na"


def open_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def reset_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path, exist_ok=True)


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def page(title, body, back_href=None, back_text=None):
    back = ""
    if back_href and back_text:
        back = f'<address><a href="{esc(back_href)}">{esc(back_text)}</a></address>'

    return f"""
<!doctype html>

<html lang="pt">
  <head>
    <meta charset="utf-8">
    <title>{esc(title)}</title>
  </head>

  <body>
    {back}
    <h3>{esc(title)}</h3>

    <hr>

    {body}
  </body>
</html>
"""


def html_table(headers_html, rows_html, empty_row_html=None):
    rows = "".join(rows_html)
    if (not rows.strip()) and empty_row_html:
        rows = empty_row_html

    return f"""
<table border="1" cellpadding="6" cellspacing="0">
  <tr>
    {headers_html}
  </tr>
  {rows}
</table>
"""