# Relatório – Otimização da Função de Schaffer com Algoritmo Genético

## Objetivo
Aplicar um Algoritmo Genético (AG) para maximizar a função de Schaffer f6 no domínio [-10, 10], analisando seu comportamento e ajustando seus parâmetros para melhorar a convergência.

---

## Configuração Inicial

- Representação: cromossomos reais (x, y)
- Seleção: torneio (k = 3 inicialmente)
- Crossover: aritmético
- Mutação: gaussiana
- População: 50 indivíduos (inicialmente)
- Gerações: 200
- Taxa de mutação: 0.05


## Linha do Tempo dos Parâmetros e Impacto

### Tamanho da população
50 → 100 → 30
Impacto: Aumenta diversidade e cobertura do espaço de busca
1. Convergência Prematura 
Com 100 indivíduos, após algumas gerações a população fica geneticamente homogênea muito rápido:

Bons genes se replicam rapidamente
Todos ficam parecidos (exploram pouco)
Fica preso em um ótimo local, não o global
Com 30, a convergência é mais lenta = mais exploração do espaço.

2. Pressão de Seleção Mais Forte
Pop. 30: Cada bom indivíduo é "mais importante" → seus genes se replicam mais
Pop. 100: Bons indivíduos se "perdem" entre muitos mediocres → menos foco na exploração
3. Mutação vs Tamanho Popular
Seu código usa taxa fixa: mutation_rate = 0.15
População 30  → 30 × 0.15 = ~4-5 mutações por geração (proporcionalmente mais!)
População 100 → 100 × 0.15 = ~15 mutações por geração (diluído em mais indivíduos)

Com população pequena, cada mutação tem impacto maior na diversidade.

### Forma de seleção
Torneio (k=3) → Torneio (k=2)  
Impacto: Reduz pressão seletiva e evita convergência prematura

### Tipo de crossover
Aritmético (sem alteração)  
Impacto: Mantém combinação suave entre soluções

### Função de fitness
Schaffer f6 (sem alteração)  
Impacto: Define corretamente o problema

### Número de gerações
200 → 300  
Impacto: Permite maior refinamento

### Taxa de crossover
0.8 (sem alteração)  
Impacto: Mantém boa exploração combinatória

### Taxa de mutação
0.05 → 0.1 → 0.15 → adaptativa  
Impacto: Aumenta diversidade e melhora exploração

### Tipo de mutação
Gaussiana global → por gene → adaptativa  
Impacto: Melhor controle da variação

### Intensidade da mutação (σ)
0.5 → 1 → 2 → adaptativa  
Impacto: Permite escapar de ótimos locais e refinar no final

### Elitismo
Não utilizado → 1 indivíduo  
Impacto: Garante preservação da melhor solução


## Problemas Identificados e Ajustes

### 1. Convergência Prematura

**Problema:**  
A população se tornava homogênea por volta da geração 10, com todos os indivíduos apresentando o mesmo fitness.

**Ajustes realizados:**
- Aumento da taxa de mutação:
  - de 0.05 → 0.1 → 0.15  
- Mutação por gene (x e y mutam separadamente)

**Justificativa:**  
A taxa inicial de 0.05 era insuficiente para manter diversidade. Com 0.15, o algoritmo conseguiu continuar explorando o espaço de busca.

---

### 2. Pressão Seletiva Elevada

**Problema:**  
A seleção por torneio com k = 3 favorecia excessivamente os melhores indivíduos.

**Ajuste realizado:**
- Redução de k:
  - de 3 → 2

**Justificativa:**  
Reduzir k diminuiu a pressão seletiva, aumentando a diversidade da população.

---

### 3. Perda de Boas Soluções

**Problema:**  
Mesmo atingindo fitness próximo de 0.999, o algoritmo perdia essas soluções nas gerações seguintes, caindo para aproximadamente 0.990.

**Ajuste realizado:**
- Implementação de elitismo (preservação de 1 indivíduo)

**Justificativa:**  
Garantiu que o melhor indivíduo fosse mantido em todas as gerações.

---

### 4. Estagnação em Ótimo Local

**Problema:**  
Mesmo com elitismo, o algoritmo estabilizava em torno de fitness ≈ 0.9903.

**Ajuste realizado:**
- Aumento da intensidade da mutação:
  - desvio padrão: de 0.5 → 1 → 2

**Justificativa:**  
Valores maiores permitiram "saltos" mais amplos no espaço de busca, possibilitando escapar de ótimos locais.

---

### 5. Ajuste Fino da Convergência

**Problema:**  
Mutação constante gerava oscilações próximas ao ótimo.

**Ajuste realizado:**
- Mutação adaptativa:
  - taxa de mutação decrescente ao longo das gerações
  - sigma decrescente (de 2 até próximo de 0)

**Justificativa:**  
- Início (gerações iniciais): maior exploração  
- Final (gerações finais): refinamento da solução  

---

### 6. Aumento de Escala do Algoritmo

**Ajustes realizados:**
- População:
  - de 50 → 100 indivíduos  
- Gerações:
  - de 200 → 300  

**Justificativa:**  
Mais indivíduos e mais gerações aumentam a cobertura do espaço de busca e permitem melhor refinamento da solução.

### 7. Degraus no gráfico Fitness x Gerações
Os degraus ocorrem por três razões principais:

1. Elitismo: O melhor fitness nunca piora, apenas se mantém ou melhora. Cada degrau representa uma nova solução melhor encontrada.

2. Mutação Dinâmica: No início das gerações, a mutação é forte (σ=2), permitindo grandes saltos no espaço de busca e descobertas rápidas. No final, muta pouco, causando platô.

3. População Pequena: Com 30 indivíduos, há menos "candidatos" para melhorar a solução a cada geração, criando padrão discreto em vez de suave.

---

## Visualização

Foi implementado um vídeo mostrando a evolução da população ao longo das gerações:

- Cada geração apresenta:
  - os indivíduos (pontos no plano x,y)
  - as curvas de nível da função de Schaffer
- Intervalo fixo: [-10, 10] para ambos os eixos

**Melhorias visuais:**
- uso de contourf (fundo com gradiente)
- transparência nas curvas
- controle de sobreposição com zorder
- destaque do melhor indivíduo

**Otimização do vídeo:**
- redução para aproximadamente 100 frames
- duração ajustada para cerca de 10 segundos

---

## Resultados

Melhor solução antes do elistimo: 
- x = 0.6829171794670232 
- y = -3.0632843608119704 
- fitness = 0.9902840901224854

Melhor solução encontrada (pop = 100):
- x = -0.013531286837763397
- y = 0.009300271456026792
- fitness = 0.9997301640075642

Melhor solução encontrada (pop = 30):
- x = 0.0001301937298556532
- y = 0.007161680720015029
- fitness = 0.9999486429549551


Ótimo global da função:

- x = 0  
- y = 0  
- fitness = 1  

---

## Conclusão

Os ajustes realizados permitiram:

- evitar convergência prematura  
- preservar soluções de alta qualidade por meio do elitismo  
- escapar de ótimos locais com mutação mais intensa  
- equilibrar exploração e refinamento com mutação adaptativa  

O comportamento observado ao longo das gerações (crescimento inicial, estagnação e posterior melhoria) está de acordo com o esperado para algoritmos genéticos bem ajustados.