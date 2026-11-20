# Como nasce o diagnóstico

O diagnóstico é a leitura de conjunto depois do mapeamento: o que liga os padrões, para que eles servem (pela lente escolhida) e o que fazer com isso. Não é diagnóstico clínico, e o texto deve dizer isso.

## Quando

O `python3 ferramentas/cerebro.py status` diz "diagnóstico: pronto" quando os critérios de `config/cerebro.json` (`diagnostico`) são cumpridos. Padrão:
- pelo menos 30 dias desde o primeiro registro;
- pelo menos 20 dias com diário;
- pelo menos 8 neurônios de verdade (sem contar os exemplos).

Passou de 60 dias sem diagnóstico: proponha de novo. A pessoa pode pedir antes; avise que com pouco dado ele sai raso.

## Antes de começar, diga à pessoa
- É a hora certa de usar o modelo mais forte (veja `guias/MODELOS-E-CUSTOS.md`). Gasta muito de uma vez: ler o cérebro inteiro e escrever uma análise longa pode comer boa parte de uma janela de uso. Por isso é uma vez a cada um ou dois meses.
- Leva de 10 a 30 minutos.
- Peça o ok. Depois, volte para o modelo do dia a dia.

## Como fazer

1. Rode `cerebro.py status --completo`. Ele lista: os neurônios mais ligados (hubs), os laços (A causa B e B causa A), as contradições declaradas, as áreas silenciosas.
2. Leia `cerebro/_graph.md` inteiro e, de cada neurônio, `## Padrões observados`, `## Contradições` e `## A investigar`. Leia as `## Falas` de uma amostra de dias espalhados no período.
3. Procure:
   - o **núcleo**: a crença ou regra de vida que explica mais padrões ao mesmo tempo. Escreva como ela diria, numa frase entre aspas;
   - de 4 a 6 **padrões** que vêm desse núcleo, cada um com evidência datada (links para diário e neurônios);
   - a **finalidade** de cada padrão pela lente (na de Adler: "para que isso serve hoje?", e não "o que causou isso?");
   - os **pontos fortes**: o que já funciona e serve de alavanca. Diagnóstico só de defeito é falho;
   - o que **ainda não se sabe**: vertentes pouco mapeadas, hipóteses sem teste.
4. Escreva `analises/diagnostico-AAAA-MM-DD.md`:

```markdown
# Diagnóstico (AAAA-MM-DD)
> Leitura de N dias, M neurônios, K sinapses. Lente: <lente>. Não é avaliação clínica.

## Núcleo: "<a frase>"
Por que acho isso, com 3 evidências linkadas.

## Padrões
### 1. <nome>
- O que acontece, com datas e links.
- Para que serve (lente).
- Quanto custa a ela.

## Pontos fortes

## O que ainda não sei

## Rota
- A: ajuda profissional (psicólogo, médico, nutricionista...) — quando e por quê. Recomende A de cara se houver sofrimento forte, sono ou apetite muito alterados, uso de substância, ou qualquer risco.
- B: coach prático aqui — um foco por vez, tarefas com prazo, testes de campo.
(As duas podem andar juntas.)

## Testes de campo
| Teste | Previsão do cérebro | Como medir | Prazo |
|---|---|---|---|
```

5. Apresente em texto curto (o arquivo tem o detalhe). Peça que ela corrija o que estiver errado: diagnóstico que ela não reconhece está errado ou mal explicado, e as duas coisas valem uma conversa.
6. Ela escolhe a rota. Com o ok, mude `"fase"` para `"coach"` no config, registre no diário e siga `guias/COACH.md`.
7. Refaça o diagnóstico a cada um ou dois meses, comparando com o anterior (o que mudou, o que os testes de campo mostraram).
