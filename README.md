# Merge Sort em Python

Este repositório contém uma implementação do algoritmo **Merge Sort** em Python.  
O Merge Sort é um algoritmo de ordenação do tipo *divisão e conquista*, que funciona dividindo a lista em sublistas menores, ordenando essas sublistas e depois mesclando os resultados.

---

## 🚀 Como funciona
1. A lista é dividida ao meio recursivamente até sobrar listas unitárias (ou vazias).
2. As sublistas são mescladas duas a duas, sempre de forma ordenada.
3. Ao final, a lista original está ordenada.

---

## 📂 Estrutura do código
- `merge_sort(lista)`:  
  Função principal que divide a lista em duas metades e chama a si mesma recursivamente até sobrar apenas listas de tamanho 1.

- `mesclar(a, b)`:  
  Função que recebe duas listas já ordenadas e as combina em uma lista ordenada final.

---

## ▶️ Exemplo de uso
```python
lista_para_ordenar = [37, 5, 92, 18, 63, 74, 29, 8, 41, 56]
print(merge_sort(lista_para_ordenar))
