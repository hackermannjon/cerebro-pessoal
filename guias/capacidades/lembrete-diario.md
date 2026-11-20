# Capacidade: lembrete diário

Ligada quando `"lembrete_diario": true`. Siga só depois do ok.

## O que é
Um lembrete no horário escolhido: "conte o seu dia ao Cérebro". Sem IA rodando sozinha: é só um aviso.

## Antes de começar, diga à pessoa
- **Custo no plano:** zero (o lembrete não chama modelo).
- **O que instalar e tempo:** nada; 5 minutos.
- Peça o ok e o horário.

## Opções
1. **Calendário (mais simples):** crie `analises/lembrete-diario.ics`, um evento diário recorrente no horário dela (RRULE:FREQ=DAILY), com alarme. Ela abre com dois cliques e ele entra na agenda dela.
2. **Celular:** sugira um alarme recorrente com o texto "Cérebro".
3. **Sistema:** se ela preferir notificação no computador, agende um comando de notificação (Mac `osascript -e 'display notification ...'`, Linux `notify-send`, Windows Agendador de Tarefas). Agendar é configuração do sistema: pede ok.
4. **App do Codex:** se ela usa o app desktop, uma tarefa agendada pode abrir um chat diário com a pergunta "como foi o seu dia?". Isso gasta um pouco do plano por dia; avise.

## Para desligar
Apague o evento ou o agendamento e ponha `false` no config.

> **Registro:** tudo o que este passo a passo criar fora da pasta (agendamento, programa, modelo, pasta) vai antes para `estado/criados.md`, com o comando para desfazer. É o que o "apagar tudo" usa.
