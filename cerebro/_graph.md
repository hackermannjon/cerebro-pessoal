# Grafo (arestas)

> Gerado por `ferramentas/cerebro.py grafo` a partir das `## Sinapses`. Cada linha: (origem) --tipo--> (destino): motivo.

(carreira/trabalho) --contradiz--> (comportamento/adiamento): o adiamento mira justo as tarefas que mostram o trabalho dela
(carreira/trabalho) --depende-de--> (saude/sono): rende mal com menos de 6 h
(comportamento/adiamento) --causa--> (saude/sono): tarefa adiada vira madrugada acordada
(comportamento/adiamento) --contradiz--> (carreira/trabalho): quer a promoção e adia justo o que mostra o trabalho dela
(saude/sono) --causa--> (comportamento/adiamento): causado por: tarefa adiada empurra a hora de dormir; e cansada, adia de novo
(saude/sono) --suporta--> (carreira/trabalho): dormir bem sustenta o rendimento no trabalho
(saude/sono) --causa--> (social/amizades): cansaço faz recusar convites
(social/amizades) --causa--> (saude/sono): causado por: cansaço vira recusa de convite
