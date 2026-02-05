def normalize_reparacoes(data):
    reparacoes_raw = data["reparacoes"] if isinstance(data, dict) and "reparacoes" in data else data

    reparacoes = []
    for rid, rep in enumerate(reparacoes_raw, start=1):
        v = rep.get("viatura", {}) if isinstance(rep.get("viatura", {}), dict) else {}
        reparacoes.append({
            "rid": rid,
            "nome": rep.get("nome", ""),
            "nif": rep.get("nif", ""),
            "data": rep.get("data", ""),
            "marca": v.get("marca", ""),
            "modelo": v.get("modelo", ""),
            "matricula": v.get("matricula", ""),
            "nr_intervencoes": rep.get("nr_intervencoes", None),
            "intervencoes": rep.get("intervencoes", []) if isinstance(rep.get("intervencoes", []), list) else []
        })

    return reparacoes


def n_intervencoes(r):
    return r["nr_intervencoes"] if r["nr_intervencoes"] is not None else len(r["intervencoes"])


def build_indexes(reparacoes):
    interv = {}
    veic = {}

    for r in reparacoes:
        vm = (r["marca"], r["modelo"])
        if vm not in veic:
            veic[vm] = {"matriculas": set(), "rids": []}

        if r["matricula"]:
            veic[vm]["matriculas"].add(r["matricula"])
        veic[vm]["rids"].append(r["rid"])

        for it in r["intervencoes"]:
            if not isinstance(it, dict):
                continue

            code = it.get("codigo", "")
            if not code:
                continue

            if code not in interv:
                interv[code] = {
                    "codigo": code,
                    "nome": it.get("nome", ""),
                    "descricao": it.get("descricao", ""),
                    "rids": []
                }
            interv[code]["rids"].append(r["rid"])

    return interv, veic


def n_carros(info):
    return len(info["matriculas"]) if info["matriculas"] else len(info["rids"])