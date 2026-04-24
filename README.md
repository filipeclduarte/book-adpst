# Análise de Dados e Previsão de Séries Temporais

> Métodos Quantitativos Modernos para Ciências Sociais Aplicadas — Fundamentos e Deep Learning com Python

Este repositório contém o código-fonte do livro **Análise de Dados e Previsão de Séries Temporais**, escrito em [Quarto](https://quarto.org) e destinado à submissão à Editora UFPB.

## Sobre o livro

O livro percorre o arcabouço moderno de previsão de séries temporais, desde métodos estatísticos clássicos (Naive, Suavização Exponencial, ARIMA) até arquiteturas de Deep Learning (MLP, LSTM/GRU, CNNs temporais, Transformers). Cada capítulo combina teoria, código Python executável e estudos de caso com dados brasileiros e internacionais.

## Estrutura

| Parte | Conteúdo |
|-------|----------|
| **Parte I** | Fundamentos e Métodos Clássicos (capítulos 1–4) |
| **Parte II** | Deep Learning para Séries Temporais (capítulos 5–8) |
| **Apêndices** | Setup, Álgebra Linear, PyTorch, Dados Brasileiros |

## Como renderizar

```bash
quarto render --to html   # GitHub Pages
quarto render --to pdf    # Amazon KDP 6×9
quarto render --to epub   # Leanpub / Kindle
quarto render --to docx   # Editora UFPB (requer template-ufpb.docx)
```

> **Importante:** execute sempre a partir do diretório raiz deste repositório.

## Notebook de soluções

Os notebooks `notebooks/cap*-solucoes.ipynb` contêm o código completo dos estudos de caso, com outputs gerados no Google Colab.

## Licença

[Creative Commons BY-NC-SA 4.0](LICENSE) — Atribuição-NãoComercial-CompartilhaIgual.

## Autor

**Filipe Coelho de Lima Duarte**  
Universidade Federal da Paraíba (UFPB)  
https://github.com/filipeclduarte
