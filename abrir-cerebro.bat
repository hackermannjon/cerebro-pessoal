@echo off
rem Windows: dois cliques neste arquivo abrem o visualizador 3D do cerebro.
rem Gera visualizador\dados.js a partir dos neuronios e abre visualizador\index.html.
rem Se o navegador bloquear arquivo local, rode: abrir-cerebro.bat --servidor
chcp 65001 >nul
cd /d "%~dp0"
set PY=
where py >/dev/null 2>/dev/null && set PY=py -3
if not defined PY where python >/dev/null 2>/dev/null && set PY=python
if defined PY (
  %PY% ferramentas\cerebro.py visual
) else (
  echo Aviso: Python 3 nao encontrado. Instale em python.org para atualizar os dados.
)
if /i "%~1"=="--servidor" if defined PY (
  start "servidor do cerebro" %PY% -m http.server 8737 --bind 127.0.0.1
  timeout /t 2 >nul
  start "" "http://127.0.0.1:8737/visualizador/index.html"
  goto :eof
)
start "" "visualizador\index.html"
