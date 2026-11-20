#!/usr/bin/env python3
"""Ferramenta do Cérebro: status, checagem de sinapses, índice, grafo e dados do visualizador.

Uso (rode da raiz do repositório; no Windows troque python3 por py ou python):
    python3 ferramentas/cerebro.py status [--completo]   fase, dias, neurônios, áreas silenciosas, diagnóstico
    python3 ferramentas/cerebro.py checar                sinapses sem volta e links quebrados
    python3 ferramentas/cerebro.py indice                reescreve cerebro/INDEX.md
    python3 ferramentas/cerebro.py grafo                 reescreve cerebro/_graph.md
    python3 ferramentas/cerebro.py visual                reescreve visualizador/dados.js
    python3 ferramentas/cerebro.py tudo                  indice + grafo + visual + checar
    python3 ferramentas/cerebro.py limpar-exemplos [--sim]  apaga os arquivos marcados <!-- exemplo -->

Só usa a biblioteca padrão do Python 3.8+.
"""
import datetime as dt
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CEREBRO = RAIZ / "cerebro"
CONFIG = RAIZ / "config" / "cerebro.json"
VISUAL = RAIZ / "visualizador" / "dados.js"
FORA = {"diario", "_arquivo", "_arquivo_dump", "_historico", "_scratch"}
TIPOS = ["causa", "contradiz", "suporta", "depende-de", "parte-de", "instancia", "relacionado"]
MARCA_EXEMPLO = "<!-- exemplo -->"
SINAPSE = re.compile(r"^-\s*\[\[([^\]]+)\]\]\s*[—–-]+\s*\*\*([^*]+)\*\*\s*(?:\([^)]*\)\s*)?[—–-]+\s*(.*)$")
LINK = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
DATA = re.compile(r"^###\s+(\d{4}-\d{2}-\d{2})")

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def ler_config():
    try:
        return json.loads(CONFIG.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def secoes(texto):
    """{'Fatos': [linhas], ...} a partir dos títulos '## '."""
    out, atual = {}, None
    for linha in texto.splitlines():
        if linha.startswith("## "):
            atual = linha[3:].strip()
            out[atual] = []
        elif atual:
            out[atual].append(linha)
    return out


def itens(linhas):
    vivos = []
    for l in linhas:
        l = l.strip()
        if l.startswith("- ") and not l.startswith("- ~~"):
            vivos.append(l[2:].strip())
    return vivos


def ler_neuronio(arq):
    texto = arq.read_text(encoding="utf-8")
    nome = arq.relative_to(CEREBRO).with_suffix("").as_posix()
    titulo = next((l[2:].strip() for l in texto.splitlines() if l.startswith("# ")), arq.stem)
    resumo = next((l[2:].strip() for l in texto.splitlines() if l.startswith("> ") and "EXEMPLO" not in l), "")
    sec = secoes(texto)
    sinapses = []
    for l in sec.get("Sinapses", []):
        m = SINAPSE.match(l.strip())
        if m and not l.strip().startswith("- ~~"):
            sinapses.append({"alvo": m.group(1).strip(), "tipo": m.group(2).strip().lower(), "motivo": m.group(3).strip()})
    datas = sorted({m.group(1) for l in sec.get("Linha do tempo", []) for m in [DATA.match(l.strip())] if m}, reverse=True)
    return {
        "id": nome,
        "nome": titulo,
        "lobo": nome.split("/")[0],
        "resumo": resumo,
        "fatos": itens(sec.get("Fatos", [])),
        "padroes": itens(sec.get("Padrões observados", [])),
        "investigar": itens(sec.get("A investigar", [])),
        "contradicoes": itens(sec.get("Contradições", [])),
        "sinapses": sinapses,
        "datas": datas,
        "linhas": texto.count("\n") + 1,
        "exemplo": MARCA_EXEMPLO in texto,
    }


def neuronios():
    out = {}
    for arq in sorted(CEREBRO.rglob("*.md")):
        rel = arq.relative_to(CEREBRO)
        if len(rel.parts) < 2 or rel.parts[0] in FORA or any(p.startswith("_") for p in rel.parts):
            continue
        n = ler_neuronio(arq)
        out[n["id"]] = n
    return out


def dias():
    out = {}
    pasta = CEREBRO / "diario"
    for arq in sorted(pasta.glob("*.md")) if pasta.exists() else []:
        if not re.match(r"\d{4}-\d{2}-\d{2}$", arq.stem):
            continue
        texto = arq.read_text(encoding="utf-8")
        out[arq.stem] = {"links": sorted({m.group(1).strip() for m in LINK.finditer(texto)}), "exemplo": MARCA_EXEMPLO in texto}
    return out


def faltas(ns):
    sem_volta, quebrados = [], []
    for n in ns.values():
        for s in n["sinapses"]:
            if s["alvo"].startswith("diario/"):
                continue
            if s["alvo"] not in ns:
                quebrados.append((n["id"], s["alvo"]))
            elif n["id"] not in {x["alvo"] for x in ns[s["alvo"]]["sinapses"]}:
                sem_volta.append((n["id"], s["tipo"], s["alvo"], s["motivo"]))
            if s["tipo"] not in TIPOS:
                quebrados.append((n["id"], f"tipo desconhecido '{s['tipo']}' para {s['alvo']}"))
    return sem_volta, quebrados


def cmd_checar(ns):
    sem_volta, quebrados = faltas(ns)
    for o, t, a, m in sem_volta:
        print(f"SEM VOLTA: [[{o}]] --{t}--> [[{a}]] ({m[:80]}). Acrescente a inversa em {a}.md")
    for o, a in quebrados:
        print(f"QUEBRADO: em {o}.md: {a}")
    if not sem_volta and not quebrados:
        print("sinapses ok: todas com volta, nenhum link quebrado")
    return len(sem_volta) + len(quebrados)


def cmd_indice(ns):
    linhas = ["# Índice do cérebro", "",
              "> Gerado por `ferramentas/cerebro.py indice`. Não edite à mão: edite os neurônios.", ""]
    lobo = None
    for n in sorted(ns.values(), key=lambda x: x["id"]):
        if n["lobo"] != lobo:
            lobo = n["lobo"]
            linhas += ["", f"## {lobo}"]
        ult = f" · {n['datas'][0]}" if n["datas"] else ""
        ex = " · EXEMPLO" if n["exemplo"] else ""
        linhas.append(f"- [[{n['id']}]] — {n['resumo'] or n['nome']}{ult}{ex}")
    d = dias()
    if d:
        linhas += ["", "## diário", f"- {len(d)} dias, de {min(d)} a {max(d)} (pasta `diario/`)"]
    (CEREBRO / "INDEX.md").write_text("\n".join(linhas).replace("\n\n\n", "\n\n") + "\n", encoding="utf-8")
    print(f"INDEX.md: {len(ns)} neurônios")


def cmd_grafo(ns):
    linhas = ["# Grafo (arestas)", "",
              "> Gerado por `ferramentas/cerebro.py grafo` a partir das `## Sinapses`. Cada linha: (origem) --tipo--> (destino): motivo.", ""]
    total = 0
    for n in ns.values():
        for s in n["sinapses"]:
            linhas.append(f"({n['id']}) --{s['tipo']}--> ({s['alvo']}): {s['motivo']}")
            total += 1
    (CEREBRO / "_graph.md").write_text("\n".join(linhas) + "\n", encoding="utf-8")
    print(f"_graph.md: {total} arestas")


def cmd_visual(ns):
    links, vistos = [], set()
    for n in ns.values():
        for s in n["sinapses"]:
            if s["alvo"] not in ns:
                continue
            chave = tuple(sorted([n["id"], s["alvo"]])) + (s["tipo"],)
            if chave in vistos:
                continue
            vistos.add(chave)
            links.append({"source": n["id"], "target": s["alvo"], "tipo": s["tipo"], "motivo": s["motivo"]})
    grau = {i: 0 for i in ns}
    for l in links:
        grau[l["source"]] += 1
        grau[l["target"]] += 1
    nodes = []
    for n in ns.values():
        nodes.append({**{k: n[k] for k in ("id", "nome", "lobo", "resumo", "exemplo")}, **{
            "fatos": n["fatos"][:8], "padroes": n["padroes"][:6], "investigar": n["investigar"][:4],
            "contradicoes": n["contradicoes"][:4], "ultima": n["datas"][0] if n["datas"] else "",
            "grau": grau[n["id"]], "sinapses": n["sinapses"]}})
    cfg = ler_config()
    dados = {"gerado": dt.datetime.now().strftime("%Y-%m-%d %H:%M"), "lente": cfg.get("lente", ""),
             "fase": cfg.get("fase", ""), "nodes": nodes, "links": links,
             "dias": {k: v["links"] for k, v in dias().items()}}
    VISUAL.parent.mkdir(parents=True, exist_ok=True)
    VISUAL.write_text("// Gerado por ferramentas/cerebro.py visual. Não edite.\nwindow.CEREBRO = "
                      + json.dumps(dados, ensure_ascii=False, indent=1) + ";\n", encoding="utf-8")
    print(f"visualizador/dados.js: {len(nodes)} neurônios, {len(links)} sinapses, {len(dados['dias'])} dias")


def cmd_status(ns, completo=False):
    cfg = ler_config()
    hoje = dt.date.today()
    d = dias()
    reais = {k: v for k, v in ns.items() if not v["exemplo"]}
    dias_reais = sorted(k for k, v in d.items() if not v["exemplo"])
    crit = cfg.get("diagnostico", {})
    print(f"fase: {cfg.get('fase', '?')} · lente: {cfg.get('lente', '?')} · onboarding: {'feito' if cfg.get('onboarding_feito') else 'PENDENTE'}")
    inicio = cfg.get("inicio_mapeamento") or (dias_reais[0] if dias_reais else "")
    corridos = (hoje - dt.date.fromisoformat(inicio)).days if inicio else 0
    print(f"neurônios: {len(reais)} (+{len(ns) - len(reais)} de exemplo) · dias com diário: {len(dias_reais)} · desde o início: {corridos} dias")
    sem_volta, quebrados = faltas(ns)
    print(f"sinapses: {sum(len(n['sinapses']) for n in ns.values())} · sem volta: {len(sem_volta)} · quebradas: {len(quebrados)}")

    # áreas silenciosas: neurônios cuja última data (linha do tempo ou diário) passou de 30 dias
    ultima = {i: (n["datas"][0] if n["datas"] else "") for i, n in reais.items()}
    for dia, v in d.items():
        for l in v["links"]:
            if l in ultima and dia > ultima[l]:
                ultima[l] = dia
    silenciosos = sorted((u or "nunca", i) for i, u in ultima.items() if not u or (hoje - dt.date.fromisoformat(u)).days > 30)
    if silenciosos:
        print("silenciosos há mais de 30 dias: " + ", ".join(f"{i} ({u})" for u, i in silenciosos[:8]))
    vertentes = cfg.get("vertentes", [])
    if vertentes:
        texto = " ".join((n["id"] + " " + n["nome"] + " " + n["resumo"]).lower() for n in reais.values())
        faltando = [v for v in vertentes if not any(p in texto for p in re.findall(r"\w{4,}", v.lower()))]
        if faltando:
            print("vertentes sem neurônio (pergunte sobre elas): " + ", ".join(faltando))

    ok = (corridos >= crit.get("dias_minimos", 30) and len(dias_reais) >= crit.get("dias_com_registro_minimos", 20)
          and len(reais) >= crit.get("neuronios_minimos", 8))
    if cfg.get("fase") == "mapeamento":
        if ok:
            extra = " (e já passou do prazo sugerido)" if corridos > crit.get("dias_sugeridos_maximos", 60) else ""
            print(f"diagnóstico: PRONTO para propor{extra} (veja guias/DIAGNOSTICO.md)")
        else:
            print(f"diagnóstico: ainda não (precisa de {crit.get('dias_minimos', 30)} dias, "
                  f"{crit.get('dias_com_registro_minimos', 20)} dias com diário e {crit.get('neuronios_minimos', 8)} neurônios)")

    if completo:
        print("\nhubs (mais ligados):")
        grau = {i: 0 for i in ns}
        for n in ns.values():
            for s in n["sinapses"]:
                grau[n["id"]] += 1
        for i, g in sorted(grau.items(), key=lambda x: -x[1])[:8]:
            print(f"  {i}: {g}")
        print("laços (A causa B e B causa A):")
        causa = {(n["id"], s["alvo"]) for n in ns.values() for s in n["sinapses"]
                 if s["tipo"] == "causa" and not s["motivo"].lower().startswith("causado por")}
        for a, b in sorted(causa):
            if a < b and (b, a) in causa:
                print(f"  {a} <-> {b}")
        print("contradições declaradas:")
        for n in ns.values():
            for c in n["contradicoes"]:
                print(f"  {n['id']}: {c[:120]}")
            for s in n["sinapses"]:
                if s["tipo"] == "contradiz" and n["id"] < s["alvo"]:
                    print(f"  {n['id']} x {s['alvo']}: {s['motivo'][:100]}")


def cmd_limpar(ns, sim):
    alvos = [CEREBRO / f"{i}.md" for i, n in ns.items() if n["exemplo"]]
    alvos += [CEREBRO / "diario" / f"{k}.md" for k, v in dias().items() if v["exemplo"]]
    if not alvos:
        print("nenhum exemplo para apagar")
        return
    print("Vai apagar:\n  " + "\n  ".join(str(a.relative_to(RAIZ)) for a in alvos))
    if not sim and input("Confirmar? [s/N] ").strip().lower() not in ("s", "sim", "y"):
        print("nada apagado")
        return
    for a in alvos:
        a.unlink()
    for pasta in sorted(CEREBRO.iterdir()):
        if pasta.is_dir() and pasta.name != "diario" and not any(pasta.iterdir()):
            pasta.rmdir()
    print(f"apagados: {len(alvos)}")
    cfg = ler_config()
    if cfg:
        cfg["exemplos_apagados"] = True
        CONFIG.write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tudo(neuronios())


def tudo(ns):
    cmd_indice(ns)
    cmd_grafo(ns)
    cmd_visual(ns)
    return cmd_checar(ns)


def main():
    args = sys.argv[1:]
    cmd = args[0] if args else "status"
    ns = neuronios()
    if cmd == "status":
        cmd_status(ns, "--completo" in args)
    elif cmd == "checar":
        sys.exit(1 if cmd_checar(ns) else 0)
    elif cmd == "indice":
        cmd_indice(ns)
    elif cmd == "grafo":
        cmd_grafo(ns)
    elif cmd == "visual":
        cmd_visual(ns)
    elif cmd == "tudo":
        tudo(ns)
    elif cmd == "limpar-exemplos":
        cmd_limpar(ns, "--sim" in args)
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main()
