# Conversão de Diagramas Mermaid para PNG

## Problema
As APIs online para converter Mermaid em PNG estão instáveis no momento.

## Solução Manual (Recomendada)

### Opção 1: Site Mermaid Live Editor (Mais Fácil)

1. Acesse: https://mermaid.live
2. Abra o arquivo `.mmd` desejado (estão em `pt-br/images/mermaid/`)
3. Cole o conteúdo no editor
4. Clique em **Actions** → **PNG** para baixar
5. Salve com o mesmo nome (ex: `fig-rnn-unrolling.png`)

### Opção 2: Usando o Mermaid CLI (Melhor Qualidade)

Instale o mermaid-cli via npm:

```bash
# Instalar globalmente
npm install -g @mermaid-js/mermaid-cli

# Converter um arquivo
mmdc -i pt-br/images/mermaid/fig-rnn-unrolling.mmd -o pt-br/images/mermaid/fig-rnn-unrolling.png

# Converter todos
for file in pt-br/images/mermaid/*.mmd; do
    mmdc -i "$file" -o "${file%.mmd}.png"
done
```

### Opção 3: Usar o Script do Projeto

Se o npm estiver disponível, tente:

```bash
# Tornar o script executável
chmod +x convert_mermaid.sh

# Executar
./convert_mermaid.sh
```

## Lista de Arquivos para Converter

| Arquivo .mmd | Descrição | Capítulo |
|--------------|-----------|----------|
| `fig-rnn-unrolling.mmd` | RNN desenrolada no tempo | Cap 06 |
| `fig-baseline-selection.mmd` | Fluxo de seleção de baselines | Cap 03 |
| `fig-mlp-architecture.mmd` | Arquitetura MLP | Cap 05 |
| `fig-temporal-cv.mmd` | Validação cruzada temporal | Cap 02 |
| `fig-causal-convolution.mmd` | Convolução causal | Cap 07 |
| `fig-attention-mechanism.mmd` | Mecanismo de atenção | Cap 08 |

## Atualizar os Capítulos

Depois de gerar os PNGs, atualize os arquivos `.qmd` para referenciar as imagens em vez do código Mermaid:

```markdown
<!-- Antes (Mermaid) -->
::: {.mermaid #fig-rnn-unrolling}
graph LR
    ...
:::

<!-- Depois (PNG) -->
![RNN desenrolada no tempo](images/mermaid/fig-rnn-unrolling.png){#fig-rnn-unrolling}
```

## Scripts de Conversão em Lote

### macOS/Linux

```bash
cd pt-br/images/mermaid

# Usando mmdc (se instalado)
for file in *.mmd; do
    mmdc -i "$file" -o "${file%.mmd}.png" --scale 2 --backgroundColor white
done
```

### Windows (PowerShell)

```powershell
cd pt-br/images/mermaid

Get-ChildItem *.mmd | ForEach-Object {
    $output = $_.BaseName + ".png"
    mmdc -i $_.Name -o $output --scale 2 --backgroundColor white
}
```

## Qualidade das Imagens

Para melhor qualidade no PDF:
- Use `--scale 2` ou `--scale 3` para alta resolução
- Use `--backgroundColor white` para fundo branco
- Dimensões recomendadas: 1200x800 pixels ou maior

## Problemas Conhecidos

1. **Erro 500/400 da API**: A API pública do mermaid.ink pode estar instável
2. **Problemas de SSL**: Pode ocorrer em ambientes corporativos
3. **Timeout**: Diagramas complexos podem demorar mais para renderizar

## Alternativa Final

Se nada funcionar, você pode:
1. Abrir o diagrama no https://mermaid.live
2. Tirar um screenshot da área do diagrama
3. Salvar como PNG
4. Ajustar no Photoshop/GIMP/Preview se necessário