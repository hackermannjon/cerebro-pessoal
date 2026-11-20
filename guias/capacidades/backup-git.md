# Capacidade: backup da memória no git

Ligada quando `"backup_git": true`. Siga só depois do ok.

## O que é
Guardar esta pasta (com o cérebro) num repositório git PRIVADO, com histórico: dá para ver o que mudou e quando, e voltar atrás se eu gravar algo errado.

## Antes de começar, diga à pessoa
- **Custo no plano:** zero se o commit for feito por script; baixo se eu fizer.
- **O que instalar e tempo:** git; conta no GitHub, GitLab ou similar se quiser cópia fora do computador. 10–15 min.
- **Atenção:** a memória tem dados pessoais. O repositório TEM que ser privado. Nunca faça push para um repositório público, nem para o repositório-modelo de onde esta pasta veio.
- Peça o ok.

## Passos
1. Confira o remoto: `git remote -v`. Se ele aponta para o repositório-modelo público, troque: o `origin` passa a ser o repositório privado da pessoa (criar repositório e fazer push pedem ok).
   - Com o GitHub CLI: `gh repo create <nome> --private --source . --push`.
2. Commit da memória: `git add cerebro analises config && git commit -m "cérebro: AAAA-MM-DD"`.
3. Ofereça um commit automático à noite, só de git, sem IA (custo zero; agendar é configuração do sistema e pede ok).
4. `git push` sempre com ok, a não ser que a pessoa libere em LIMITES.md.

## Para desligar
Ponha `false` no config; o repositório continua existindo.

> **Registro:** tudo o que este passo a passo criar fora da pasta (agendamento, programa, modelo, pasta) vai antes para `estado/criados.md`, com o comando para desfazer. É o que o "apagar tudo" usa.
