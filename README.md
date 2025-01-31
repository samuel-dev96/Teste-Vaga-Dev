## 1. Valor Final da Variável `SOMA`

```c
int INDICE = 13, SOMA = 0, K = 0;

while (K < INDICE) {
   K = K + 1;
   SOMA = SOMA + K;
}
printf("%d", SOMA);
```

**Resposta:** O valor final de `SOMA` é **91**.  
**Explicação:** O loop soma todos os inteiros de **1** a **13**. A soma de 1 + 2 + 3 + ... + 13 = 91.

---

## 2. Verificação de Pertinência à Sequência de Fibonacci

A sequência de Fibonacci inicia em **0** e **1**, e cada número seguinte é a soma dos dois anteriores (0, 1, 1, 2, 3, 5, 8, 13...).

**Estrutura da Solução (exemplo em Python):**
1. Ler ou definir o número a verificar.
2. Gerar valores de Fibonacci até ultrapassar ou igualar ao número.
3. Verificar se, em algum momento, o número se iguala a um dos gerados.

Exemplo simplificado de função em Python:

```python
def is_fibonacci(num):
    if num < 0:
        return False
    
    fibo_a, fibo_b = 0, 1
    
    if num == 0 or num == 1:
        return True

    while fibo_b < num:
        fibo_a, fibo_b = fibo_b, fibo_a + fibo_b
        
        if fibo_b == num:
            return True
    
    return False

numero = 21
if is_fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} NÃO pertence à sequência de Fibonacci.")
```

---

## 3. Faturamento Diário de uma Distribuidora

### Objetivos:
- Encontrar o **menor** e o **maior** valor de faturamento em um dia do mês.
- Calcular a **média mensal**, ignorando dias sem faturamento (0 ou dias inexistentes no registro).
- Descobrir em **quantos dias** o faturamento foi **superior** à média mensal.

### Passos Gerais:
1. Ler dados de um arquivo (JSON, XML etc.) com os valores de faturamento diário.
2. Ignorar dias com valor 0 ou que não estão presentes no arquivo (finais de semana, feriados).
3. Encontrar o menor e o maior valor usando funções de agregação (`min`, `max`).
4. Calcular a média (soma total / número de dias considerados).
5. Comparar cada valor de faturamento com a média para contar quantos dias excedem essa média.

Exemplo em Python (pseudo-estrutura):
```python
import json

def analisar_faturamento(arquivo):
    with open(arquivo, 'r') as f:
        dados = json.load(f)
    
    # Filtra somente dias com faturamento > 0
    valores = [item['valor'] for item in dados if item['valor'] > 0]
    
    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)
    
    dias_acima_media = sum(1 for valor in valores if valor > media_mensal)
    
    return menor_valor, maior_valor, dias_acima_media

arquivo = 'faturamento.json'
menor, maior, dias_acima = analisar_faturamento(arquivo)
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Dias acima da média: {dias_acima}")
```

---

## 4. Percentual de Representação Mensal por Estado

Dado:
```
SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53
```

### Passos Gerais:
1. Somar todos os valores para obter o **valor total**.
2. Calcular a porcentagem de cada estado em relação ao total:
   \[
   \text{percentual} = \frac{\text{valorEstado}}{\text{valorTotal}} \times 100
   \]

Exemplo em Python:
```python
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento.values())

for estado, valor in faturamento.items():
    percentual = (valor / total) * 100
    print(f"{estado} = {percentual:.2f}%")
```

---

## 5. Explicação do Código que Inverte uma String

O código em `inverter_string.py` (ou em outro arquivo de sua escolha) faz a inversão dos caracteres de uma string **sem usar** funções prontas de reversão, como `[::-1]` no Python ou `reverse()` em algumas linguagens.

### Funcionamento:

1. **Recebe uma string** como parâmetro.
2. **Verifica**:
   - Se é `None` (levanta erro).
   - Se não é do tipo `str` (levanta `TypeError`).
   - Se está vazia ou contém apenas espaços (levanta `ValueError`).
3. **Converte** a string em uma **lista de caracteres**.
4. **Define dois índices**, `inicio` (0) e `fim` (última posição da lista).
5. **Troca de caracteres**:
   - Enquanto `inicio < fim`:
     - Troca `chars[inicio]` com `chars[fim]`.
     - Incrementa `inicio` e decrementa `fim`.
6. **Reune** a lista de volta em uma string usando `"".join(chars)`.
7. **Retorna** a string invertida.

