# Capacidade: vários dispositivos

Ligada quando `"varios_dispositivos": true`. Nada vem instalado: siga só depois do ok.

## O que é
Usar o cérebro em mais de um computador: PC→PC, PC→Mac, notebook→desktop. Há dois jeitos, do mais simples ao mais poderoso.

## Antes de começar, diga à pessoa
- **Custo no plano:** nenhum a mais no jeito A; no jeito B, cada comando remoto é uma chamada de ferramenta normal (baixo).
- **O que instalar e tempo:** A: git e um repositório privado (10 min). B: servidor SSH na máquina de destino e uma chave (20–30 min por máquina).
- **Risco:** no jeito B eu passo a poder rodar comandos na outra máquina. Por isso, todo comando remoto pede o ok dela, a não ser que ela libere por escrito em `guias/LIMITES.md`.
- Peça o ok e a escolha.

## Jeito A: a mesma memória em todas as máquinas (recomendado para começar)
Cada computador roda a própria sessão (Codex, Claude ou Gemini) nesta mesma pasta, sincronizada por git.
1. Ligue antes a capacidade `backup-git` (repositório PRIVADO).
2. Em cada máquina: `git clone` do repositório privado.
3. Acrescente no AGENTS.md, seção "Capacidades ligadas": "Vários dispositivos (A): ao começar, rode `git pull`; ao terminar algo relevante, faça commit e peça o ok para o push."
4. Conflito de git: eu mostro o conflito e resolvo junto com a pessoa, nunca descarto a versão dela.

## Jeito B: eu comando a outra máquina (SSH)
1. Na máquina de destino, ligar o servidor SSH:
   - Mac: Ajustes > Geral > Compartilhamento > Login Remoto.
   - Windows: Configurações > Sistema > Recursos opcionais > Servidor OpenSSH; depois `Start-Service sshd`.
   - Linux: `sudo apt install openssh-server`.
2. Na máquina de origem: `ssh-keygen -t ed25519` e copiar a chave pública para a de destino. Eu nunca leio a chave privada.
3. Testar: `ssh usuario@nome-ou-ip-da-maquina "echo ok"`. O endereço fica em `memoria/` como referência; nunca grave senha.
4. Acrescente no AGENTS.md: "Vários dispositivos (B): posso rodar `ssh <apelido> <comando>`; cada comando remoto pede ok, salvo as liberações em LIMITES.md."

## Para desligar
Tire a linha do AGENTS.md, ponha `false` no config e, no jeito B, desligue o servidor SSH na outra máquina.
