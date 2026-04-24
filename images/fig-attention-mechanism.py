import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10

fig, ax = plt.subplots(figsize=(13, 6.5))
ax.set_xlim(0, 14)
ax.set_ylim(0, 7)
ax.axis('off')
fig.patch.set_facecolor('white')

c_q = '#4C78A8'
c_k = '#F58518'
c_v = '#72B7B2'
c_matmul = '#E45756'
c_softmax = '#59A14F'
c_out = '#9D7660'

def draw_box(ax, x, y, w, h, color, label, fontsize=10, text_color='white'):
    rect = plt.Rectangle((x, y), w, h, facecolor=color, edgecolor='black',
                          linewidth=1.2, zorder=3)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2, label, ha='center', va='center',
            fontsize=fontsize, fontweight='bold', color=text_color, zorder=4)

def draw_arrow(ax, x1, y1, x2, y2, color='black', lw=1.5):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw))

# =============================
# ENTRADAS Q, K, V
# =============================
draw_box(ax, 0.3, 4.8, 1.6, 0.9, c_q, 'Query\nQ')
draw_box(ax, 0.3, 2.8, 1.6, 0.9, c_k, 'Key\nK')
draw_box(ax, 0.3, 0.5, 1.6, 0.9, c_v, 'Value\nV')

# =============================
# MULTIPLICAÇÃO Q K^T (recebe Q e K)
# =============================
draw_box(ax, 3.5, 3.5, 2.2, 2.2, c_matmul, 'Q K^T')

# Q -> QK^T
draw_arrow(ax, 1.9, 5.25, 3.5, 5.0)
# K -> QK^T
draw_arrow(ax, 1.9, 3.25, 3.5, 4.2)

# =============================
# DIVISÃO POR sqrt(d_k)
# =============================
draw_arrow(ax, 5.7, 4.6, 6.5, 4.6)
ax.text(6.1, 4.85, r'$\div \sqrt{d_k}$', ha='center', va='center',
        fontsize=10, fontweight='bold', color='#333333',
        bbox=dict(boxstyle='round,pad=0.15', facecolor='#f7f7f7', edgecolor='#cccccc'))

# =============================
# SOFTMAX
# =============================
draw_arrow(ax, 6.9, 4.6, 7.7, 4.6)
draw_box(ax, 7.7, 3.6, 1.6, 2.0, c_softmax, 'softmax')

# =============================
# MULTIPLICAÇÃO FINAL x V
# =============================
draw_arrow(ax, 9.3, 4.6, 10.1, 4.6)

# V -> x V (por baixo, caminho em L)
draw_arrow(ax, 1.9, 0.95, 3.0, 0.95)
ax.plot([3.0, 3.0], [0.95, 3.2], color='black', linewidth=1.5, zorder=1)
draw_arrow(ax, 3.0, 3.2, 10.1, 3.2)

draw_box(ax, 10.1, 3.2, 2.2, 2.2, c_matmul, 'x V')

# =============================
# OUTPUT Z
# =============================
draw_arrow(ax, 12.3, 4.3, 13.0, 4.3)
draw_box(ax, 13.0, 3.7, 1.2, 1.2, c_out, 'Z')

# =============================
# FÓRMULA NO RODAPÉ
# =============================
formula = r'$\mathrm{Attention}(Q,K,V) = \mathrm{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$'
ax.text(7.0, 0.25, formula, ha='center', va='center', fontsize=11,
        color='#333333',
        bbox=dict(boxstyle='round,pad=0.35', facecolor='#f7f7f7',
                  edgecolor='#cccccc', linewidth=1))

# =============================
# LEGENDA (acima, fora do diagrama principal)
# =============================
legend_elements = [
    mpatches.Patch(facecolor=c_q, edgecolor='black', label='Query'),
    mpatches.Patch(facecolor=c_k, edgecolor='black', label='Key'),
    mpatches.Patch(facecolor=c_v, edgecolor='black', label='Value'),
    mpatches.Patch(facecolor=c_matmul, edgecolor='black', label='MatMul'),
    mpatches.Patch(facecolor=c_softmax, edgecolor='black', label='Softmax'),
    mpatches.Patch(facecolor=c_out, edgecolor='black', label='Output'),
]
ax.legend(handles=legend_elements, loc='upper center', ncol=6, fontsize=9,
          frameon=True, fancybox=True, bbox_to_anchor=(0.5, 1.12))

plt.tight_layout()
plt.savefig('../images/fig-attention-mechanism.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.show()
