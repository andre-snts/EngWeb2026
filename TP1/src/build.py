import argparse
import os

from .utils import open_json, reset_dir, ensure_dir
from .model import normalize_reparacoes, build_indexes

from .render.index import render as render_index
from .render.reparacoes import render_list as render_reparacoes_list, render_details as render_reparacoes_details
from .render.intervencoes import render_list as render_intervencoes_list, render_details as render_intervencoes_details
from .render.veiculos import render_list as render_veiculos_list, render_details as render_veiculos_details


def build_site(dataset_path="dataset_reparacoes.json", outdir="www"):
    data = open_json(dataset_path)
    reparacoes = normalize_reparacoes(data)
    interv, veic = build_indexes(reparacoes)

    reset_dir(outdir)
    ensure_dir(os.path.join(outdir, "reparacoes"))
    ensure_dir(os.path.join(outdir, "intervencoes"))
    ensure_dir(os.path.join(outdir, "veiculos"))

    render_index(outdir)

    render_reparacoes_list(outdir, reparacoes)
    render_reparacoes_details(outdir, reparacoes)

    render_intervencoes_list(outdir, interv)
    render_intervencoes_details(outdir, interv)

    render_veiculos_list(outdir, veic)
    render_veiculos_details(outdir, veic)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("dataset", nargs="?", default="dataset_reparacoes.json")
    p.add_argument("outdir", nargs="?", default="www")

    args = p.parse_args()
    build_site(args.dataset, args.outdir)


if __name__ == "__main__":
    main()