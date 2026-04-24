# AGENTS.md

Livro Quarto em português (pt-BR): **Análise de Dados e Previsão de Séries Temporais**.

## Critical Build Rule

Sempre execute comandos a partir do diretório raiz deste repositório:

```bash
quarto render --to html     # HTML (GitHub Pages)
quarto render --to pdf      # PDF (Amazon KDP 6×9)
quarto render --to epub     # ePub (Leanpub / Kindle / Gumroad)
quarto render --to docx     # DOCX — requer template-ufpb.docx
```

## Code Execution Patterns

Python blocks usam Jupyter com três opções de integração (documentadas em `_quarto.yml`):

1. **Opção A**: Usar `.ipynb` diretamente do Google Colab
2. **Opção B**: `eval: false` + incluir figuras pré-computadas de `images/`
3. **Opção C**: Rodar localmente, commitar `_freeze/` para pular re-execução

Configuração atual: `execute: eval: false` (nenhuma execução automática).

## Architecture Notes

- **8 capítulos + 5 apêndices**: econometria/atuária + datasets brasileiros
- Bibliografia em `bibliography/references.bib`
- DOCX requer Word template `template-ufpb.docx` com estilos A5 + ABNT

## CI Pipeline

GitHub Actions (`.github/workflows/publish.yml`) — renderiza HTML e publica no GitHub Pages.

## Output Locations

- `_book/` — build output (gitignored)
- `_freeze/` — outputs congelados (gitignored)
