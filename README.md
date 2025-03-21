# DESAFIO DE QUALIDADE DE SOFTWARE – PRÁTICA DE CI/CD, PR E CR

## Objetivo
Você fará parte de uma equipe de desenvolvimento que está trabalhando em uma API de tarefas. O código inicial **foi entregue com falhas intencionais** (algumas bem escondidas 👀), e seu papel será:

- Identificar as falhas no código.
- Corrigir os erros de lógica ou estrutura.
- Criar novos testes, se necessário.
- Submeter suas correções via **Pull Request (PR)**.
- Revisar ao menos **1 PR de um colega**, apontando sugestões, melhorias ou problemas.

---

## O que você deve fazer

### 1. **Corrigir as falhas no código**
Identifique e corrija problemas como:
- Erros lógicos em endpoints (`PATCH`, `PUT`, `GET`, etc.).
- Falta de validações.
- Problemas de persistência em memória.

### 2. **Melhorar os testes**
- Os testes existentes não cobrem todos os casos.
- Escreva testes adicionais para validar:
  - Casos inválidos de entrada.
  - Retornos esperados de erros.

### 3. **Submeter um Pull Request (PR)**
- Crie uma **branch com seu nome** ou identificação.
- Suba as correções.
- Abra um PR explicando o que foi feito.
- Marque 1 ou mais colegas para revisão.

### 4. **Revisar um PR**
- Acesse o PR de um colega.
- Leia o código e analise se os objetivos foram atingidos.
- Deixe comentários construtivos (elogiando boas práticas, sugerindo melhorias, apontando falhas).

---

## Fluxo de trabalho recomendado

```bash
# Clone o projeto e crie uma nova branch
git clone https://github.com/RonierisonMaciel/T32.git
cd T32
git checkout -b minha-correcao

# Faça as alterações e valide os testes
pytest

# Suba as alterações
git add .
git commit -m "Corrige problema no PATCH de conclusão da tarefa"
git push origin minha-correcao

# Abra o PR no GitHub e marque seus colegas
```

---

## Pontuação (XP)

| Tarefa                                       | Pontos |
|---------------------------------------------|--------|
| Corrigiu uma falha de código                 | 5      |
| Criou um teste novo e últil                   | 5      |
| Revisou um PR com comentários pertinentes    | 5      |
| PR aceito sem erros após revisão             | 5      |
| Encontrou uma falha que ninguém viu ainda    | 10     |

> O aluno com mais pontos poderá apresentar suas soluções e melhorias para a turma

---

Boa sorte, e lembre-se: qualidade não é apenas escrever código que funciona, é escrever código que seja **limpo, confiável, testado e colaborativo**!
# T32
