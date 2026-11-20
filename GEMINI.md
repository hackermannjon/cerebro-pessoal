# Notas para o Gemini (Antigravity CLI e Gemini CLI)

As regras do projeto estão no AGENTS.md (fonte única). Este arquivo só acrescenta o que é do Gemini.

- No Antigravity CLI (`agy`), que é onde contas Google gratuitas e o plano Google AI Pro usam o Gemini desde junho de 2026, o AGENTS.md já é lido sozinho. Nada a fazer.
- No Gemini CLI (`gemini`, hoje só para chave de API paga ou licença empresarial), a linha abaixo importa o AGENTS.md:

@AGENTS.md

## Só no Gemini

- Modelo: Flash no dia a dia (`/model`); o modelo Pro só para o diagnóstico. Volte para o Flash depois.
- Contexto: `/compact` no Antigravity (`/compress` no Gemini CLI) resume a conversa; `/clear` começa do zero; `/usage` (Antigravity) ou `/stats` (Gemini CLI) mostra o consumo.
- Subagentes: existem (`/agents`) e gastam mais cota. Use para pesquisa longa, com aviso.
