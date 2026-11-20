# Modelos, custos e contexto

Consultado em 20/11/2026. Nomes de modelo e limites mudam a cada poucos meses: confira nas fontes antes de decidir, e peça ao Cérebro para atualizar este arquivo quando algo mudar.

## Resumo em uma tabela

| | ChatGPT / Codex (caminho principal) | Claude Code (alternativa) | Gemini / Antigravity (alternativa) |
|---|---|---|---|
| Plano básico | Plus, US$ 20/mês | Pro, US$ 20/mês | Google AI Pro, R$ 96,99/mês (há nível gratuito) |
| Lê as regras de | `AGENTS.md` | `CLAUDE.md` (que importa o `AGENTS.md`) | `AGENTS.md` ou `GEMINI.md` |
| Dia a dia | GPT-6.2 Sol, esforço baixo ou médio | Sonnet (`sonnet`) | Gemini Flash |
| Diagnóstico (raro) | GPT-6.2 Astra, comece em baixo ou médio | Opus (`opus`) | Gemini Pro (Neon) |
| Rotina automática | GPT-6 Luna | Haiku (`haiku`) | Gemini Flash |
| Ver consumo | `/status` | `/usage` | `/usage` |
| Compactar a conversa | `/compact` | `/compact` | `/compact` (Gemini CLI: `/compress`) |
| Conversa nova | `/new` (ou `/clear`) | `/clear` | `/clear` |
| Sem interface (rotinas) | `codex exec` | `claude -p` | `agy -p` |
| Subagentes | sim, só quando pedidos; gastam mais | sim; gastam a mesma cota | sim (`/agents`) |

## ChatGPT / Codex (recomendado)

**Limites.** O Plus tem uma janela de uso de 5 horas e pode ter limite semanal. A OpenAI publica faixas estimadas de mensagens locais por janela de 5 h no Plus: GPT-6.2 Astra 6–50, GPT-6.2 Sol 17–180, GPT-6.1 Sol 15–160, GPT-6.1 Terra 35–285, GPT-6 Luna 350–3.000. A faixa é larga porque depende do tamanho de cada tarefa. Free (US$ 0) e Go (US$ 8) só têm o GPT-6 Luna no app desktop. O Pro (a partir de US$ 100) tem cota bem maior. Acabou a cota: espere a janela virar ou compre créditos (Configurações > Uso); o plano não troca de modelo sozinho. Tarefas na nuvem (Codex cloud) saem da mesma cota e tendem a gastar mais que as locais.

**App desktop ou CLI?**
- **App desktop do ChatGPT, modo Codex (recomendado para começar):** Mac, Windows e Linux; instala sem terminal; tem botões de permissão (sandbox) e aprovação; lê o `AGENTS.md` e os `.md` desta pasta do mesmo jeito; tem **tarefas agendadas** (menu "Scheduled": diária, semanal ou por intervalo), que servem para as rotinas, desde que o computador e o app estejam ligados; tem voz.
- **Codex CLI:** para quem gosta de terminal; tem `codex exec`, que roda sem interface e pode ser agendado pelo sistema (cron, launchd, Agendador de Tarefas) mesmo com o app fechado; também é o caminho para servidor sem tela.
- Os dois usam a mesma conta, a mesma cota, o mesmo `AGENTS.md`, skills e subagentes.

**Memória do próprio Codex.** O Codex tem uma memória automática opcional ("Codex memories"), desligada por padrão e guardada fora desta pasta. A memória do ChatGPT web é outra, separada, e não entra no Codex. Este projeto não depende de nenhuma das duas: a fonte da verdade são os arquivos em `cerebro/`. Se ligar a do Codex, saiba que ela pode divergir dos arquivos.

**Modelo.**
- Dia a dia: GPT-6.2 Sol, esforço baixo ou médio (`/model`). Se não aparecer, GPT-6.1 Sol.
- Diagnóstico (uma vez a cada um ou dois meses): GPT-6.2 Astra. A própria OpenAI sugere começar em esforço baixo ou médio; alto só para trabalho difícil de várias etapas. Volte para o Sol depois.
- Rotina automática: GPT-6 Luna (o mais econômico).
- Nunca deixe o Astra num loop ou numa tarefa agendada.

Fontes: [preços e limites](https://learn.chatgpt.com/docs/pricing), [modelos](https://learn.chatgpt.com/docs/models), [Codex no plano do ChatGPT](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan), [app](https://learn.chatgpt.com/docs/app), [tarefas agendadas](https://learn.chatgpt.com/docs/automations.md?surface=app), [CLI](https://learn.chatgpt.com/docs/cli), [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [subagentes](https://learn.chatgpt.com/docs/agent-configuration/subagents), [memórias](https://learn.chatgpt.com/docs/customization/memories.md), [créditos](https://help.openai.com/en/articles/12642688-using-credits-for-flexible-usage-in-chatgpt-freegopluspro-sora).

Detalhe técnico: o Codex junta os `AGENTS.md` da raiz do repositório até a pasta atual, com teto de 32 KiB somados. Por isso o `AGENTS.md` daqui é curto e o resto mora em `guias/`, lido só quando precisa.

## Claude Code com Pro (alternativa)

- O Pro tem uma janela de 5 horas e um limite semanal, divididos entre o app do Claude e o Claude Code. Trocar de modelo não destrava o limite.
- O padrão do Claude Code no Pro é o Opus. Este repositório fixa o **Sonnet** em `.claude/settings.json`, porque o Sonnet custa menos e dá conta do dia a dia. Opus (`/model opus`) só para o diagnóstico, e com parcimônia; nunca em rotina ou em loop.
- Rotina automática: `claude -p "..." --model haiku`.
- O Claude Code lê o `CLAUDE.md`; o deste repositório importa o `AGENTS.md` com a linha `@AGENTS.md`.
- Fontes: [modelos](https://code.claude.com/docs/en/model-config), [Pro no Claude Code](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan), [custos](https://code.claude.com/docs/en/costs), [comandos](https://code.claude.com/docs/en/commands), [memória e imports](https://code.claude.com/docs/en/memory), [preços](https://claude.com/pricing).

## Gemini (alternativa)

- Desde 18/06/2026, conta Google gratuita e Google AI Pro usam o Gemini no terminal pelo **Antigravity CLI** (`agy`). O Gemini CLI (`gemini`) ficou só para chave de API paga e licença empresarial.
- O Antigravity lê `AGENTS.md` ou `GEMINI.md` sozinho. O `GEMINI.md` daqui importa o `AGENTS.md` para quem ainda usa o Gemini CLI.
- Dia a dia: Gemini Flash. Gemini Pro (Neon, exige AI Pro) só para o diagnóstico. A cota do AI Pro renova a cada 5 horas até um limite semanal; o nível gratuito tem cota semanal.
- Fontes: [mudança para o Antigravity](https://developers.googleblog.com/en/an-important-update-transitioning-gemini-cli-to-antigravity-cli/), [modelos do Antigravity](https://antigravity.google/docs/models/), [planos](https://antigravity.google/docs/plans.md), [regras e AGENTS.md](https://antigravity.google/docs/rules/), [GEMINI.md no Gemini CLI](https://geminicli.com/docs/cli/gemini-md/).

## Economia de contexto (vale para as três)

Cada mensagem reenvia ao modelo as regras, a memória lida e a conversa até ali. Contexto grande = cada troca mais cara e o modelo mais distraído.

- **Arquivo de regras curto.** O `AGENTS.md` só tem o que vale em toda conversa. O resto vai para `guias/`, lido sob demanda.
- **Índice com um item por linha.** O `cerebro/INDEX.md` (gerado pelo `cerebro.py`) é só um sumário: link e resumo de uma linha. O Cérebro lê o índice e o `status`, e abre só os neurônios do assunto.
- **Neurônios enxutos.** Passou de ~150 linhas, divide; linha do tempo antiga vai para `_historico/`.
- **Quando compactar:** a conversa ficou longa mas o assunto continua (ex.: um plano sendo refinado). `/compact` troca o histórico por um resumo. Ele também gasta cota, porque relê a conversa.
- **Quando abrir sessão nova:** o assunto mudou, ou a tarefa terminou. `/new` ou `/clear` não custam nada. Antes, confira que o diário e os neurônios foram gravados.
- **Ver o que ocupa:** `/status` (Codex), `/context` e `/usage` (Claude), `/context` e `/usage` (Antigravity).
- **Subagentes** têm contexto próprio e devolvem só o resumo: bons para pesquisa longa, mas cada um gasta cota. Use quando a tarefa for grande de verdade.
- **Modelo forte é exceção:** use para uma análise de cada vez, depois volte ao do dia a dia.
