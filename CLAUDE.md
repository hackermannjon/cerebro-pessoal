# Notas para o Claude Code

As regras do projeto estão no AGENTS.md (fonte única). Este arquivo só importa e acrescenta o que é do Claude.

@AGENTS.md

## Só no Claude Code

- Modelo: o arquivo `.claude/settings.json` deste repositório já fixa `sonnet`. No plano Pro o padrão do Claude Code é o Opus, que custa mais que o Sonnet (a própria documentação recomenda deixá-lo para tarefas complexas). Use o Opus (`/model opus`) só para o diagnóstico (uma vez a cada um ou dois meses), e volte para o Sonnet (`/model sonnet`) logo depois. Nunca use Opus em rotina automática.
- Contexto: `/context` mostra o que ocupa a janela; `/compact` resume a conversa (também gasta cota); `/clear` começa do zero sem custo. `/usage` mostra quanto do plano já foi.
- Subagentes: existem (Explore, Plan, general-purpose) e gastam a mesma cota. Para pesquisa simples, um subagente com `model: haiku` sai mais barato.
- Instruções que você der aqui valem só para o Claude. Regra para todas as ferramentas vai no AGENTS.md.
