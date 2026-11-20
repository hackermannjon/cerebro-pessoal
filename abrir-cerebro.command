#!/usr/bin/env bash
# Mac: dois cliques neste arquivo abrem o visualizador 3D do cérebro.
# Na primeira vez o macOS pode bloquear: clique com o botão direito > Abrir.
cd "$(dirname "$0")" || exit 1
exec ./abrir-cerebro.sh "$@"
