#!/usr/bin/env bash
# Abre o visualizador 3D do cérebro (Linux e Mac).
# Gera visualizador/dados.js a partir dos neurônios e abre visualizador/index.html no navegador.
# Não precisa de servidor: o HTML lê os dados por <script>. Se o seu navegador bloquear arquivo local,
# rode com --servidor (sobe python3 -m http.server em 127.0.0.1:8737, só no seu computador).
cd "$(dirname "$0")" || exit 1
PY=$(command -v python3 || command -v python)
if [ -n "$PY" ]; then
  "$PY" ferramentas/cerebro.py visual || echo "Aviso: não consegui gerar os dados; abrindo a última versão."
else
  echo "Aviso: Python 3 não encontrado; abrindo com os dados da última geração (se houver)."
fi
abrir() { if command -v xdg-open >/dev/null; then xdg-open "$1"; elif command -v open >/dev/null; then open "$1"; else echo "Abra no navegador: $1"; fi; }
if [ "$1" = "--servidor" ] && [ -n "$PY" ]; then
  echo "Servidor em http://127.0.0.1:8737/visualizador/ (Ctrl+C para parar)"
  (sleep 1; abrir "http://127.0.0.1:8737/visualizador/index.html") &
  exec "$PY" -m http.server 8737 --bind 127.0.0.1
else
  abrir "visualizador/index.html"
fi
