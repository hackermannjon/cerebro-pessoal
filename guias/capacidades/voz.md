# Capacidade: voz

Ligada quando `"voz": true`. Nada vem instalado: siga só depois do ok.

## O que é
- **Contar o dia por voz:** a pessoa fala, o texto chega aqui. É o jeito mais natural de alimentar um diário.
- **Ouvir as perguntas:** no fim de cada resposta, as perguntas são lidas em voz alta.

## Antes de começar, diga à pessoa
- **Custo no plano:** baixo. Ditado não gasta nada; ler em voz alta é um comando curto por resposta.
- **O que instalar e tempo:** ditado do sistema, nada (2 min). Para falar: voz do sistema (nada, 2 min), edge-tts (`pip install edge-tts`, 5 min, precisa de internet) ou Piper (offline, ~60 MB, 10–15 min). Se ela já tem um modelo de voz, use o dela.
- **Privacidade:** voz alta pode ser ouvida por quem está perto. Pergunte se pode, e lembre das `palavras_codigo`.
- Peça o ok e a escolha.

## Passos
1. Ditado: Mac, Ajustes > Teclado > Ditado; Windows, `Win + H`. O app do ChatGPT também tem voz, mas o modo de voz conversa sem ler estes arquivos: para registrar no cérebro, dite no Codex/terminal.
2. Ao contar por voz, a transcrição erra nomes: confirme a grafia de nomes próprios antes de gravar.
3. Para falar, crie `ferramentas/falar.py` que recebe um texto e fala: `say` no Mac, `System.Speech` no Windows, `espeak-ng` no Linux, ou `edge-tts --voice pt-BR-FranciscaNeural`.
4. Teste com uma frase. Acrescente no AGENTS.md, "Capacidades ligadas": "Voz: no fim, leia só as perguntas com `python3 ferramentas/falar.py \"...\"`, sem markdown."

## Para desligar
Tire a linha do AGENTS.md e ponha `false` no config.
