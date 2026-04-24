import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Arc, FancyArrowPatch
import numpy as np

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10

fig = plt.figure(figsize=(13, 6))
fig.patch.set_facecolor('white')

ax_left = fig.add_axes([0.05, 0.10, 0.28, 0.80])
ax_right = fig.add_axes([0.42, 0.10, 0.55, 0.80])

colors_cell = '#4C78A8'
colors_h = '#E45756'

# =============================
# PAINEL ESQUERDO: Visão Compacta
# =============================
ax_left.set_xlim(0, 5)
ax_left.set_ylim(0, 6)
ax_left.axis('off')
ax_left.set_title('Visão Compacta', fontsize=12, fontweight='bold', pad=10)

cell = FancyBboxPatch((1.5, 2.0), 2.0, 2.0, boxstyle="round,pad=0.15",
                       facecolor=colors_cell, edgecolor='black', linewidth=1.5)
ax_left.add_patch(cell)
ax_left.text(2.5, 3.0, 'RNN', ha='center', va='center',
             fontsize=14, fontweight='bold', color='white')

ax_left.annotate('', xy=(1.5, 3.0), xytext=(0.3, 3.0),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax_left.text(0.8, 3.25, r'$\mathbf{x}_t$', fontsize=12, color='#333333')

ax_left.annotate('', xy=(4.7, 3.0), xytext=(3.5, 3.0),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax_left.text(4.1, 3.25, r'$\mathbf{y}_t$', fontsize=12, color='#333333')

arc = Arc((2.5, 4.0), 2.0, 1.5, angle=0, theta1=0, theta2=180,
          color=colors_h, linewidth=2, linestyle='--')
ax_left.add_patch(arc)

ax_left.annotate('', xy=(1.6, 4.7), xytext=(1.55, 4.75),
                arrowprops=dict(arrowstyle='->', color=colors_h, lw=2))
ax_left.text(2.5, 5.0, r'$\mathbf{h}_{t-1} \rightarrow \mathbf{h}_t$',
             ha='center', va='center', fontsize=11, color=colors_h, fontweight='bold')

ax_left.text(2.5, 0.8, 'Mesmos parâmetros\ncompartilhados em todo $t$',
             ha='center', va='center', fontsize=9, color='#555555',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#f7f7f7', edgecolor='#cccccc'))

# =============================
# PAINEL DIREITO: Visão Desenrolada
# =============================
ax_right.set_xlim(0, 14)
ax_right.set_ylim(0, 6)
ax_right.axis('off')
ax_right.set_title('Visão Desenrolada no Tempo (Unrolling)', fontsize=12, fontweight='bold', pad=10)

x_positions = [1.5, 4.5, 7.5, 10.5]
labels_t = [r'$t-1$', r'$t$', r'$t+1$', r'$t+2$']

for i, (x, lab) in enumerate(zip(x_positions, labels_t)):
    cell = FancyBboxPatch((x - 0.9, 2.2), 1.8, 1.6, boxstyle="round,pad=0.12",
                           facecolor=colors_cell, edgecolor='black', linewidth=1.2)
    ax_right.add_patch(cell)
    ax_right.text(x, 3.0, 'RNN', ha='center', va='center',
                  fontsize=10, fontweight='bold', color='white')
    
    ax_right.text(x, 1.5, lab, ha='center', va='center', fontsize=11, fontweight='bold')
    
    ax_right.annotate('', xy=(x, 2.2), xytext=(x, 1.7),
                      arrowprops=dict(arrowstyle='->', color='black', lw=1.2))
    ax_right.text(x, 1.9, r'$\mathbf{x}$', ha='center', va='bottom', fontsize=9)
    
    ax_right.annotate('', xy=(x, 4.6), xytext=(x, 3.8),
                      arrowprops=dict(arrowstyle='->', color='black', lw=1.2))
    ax_right.text(x + 0.35, 4.3, r'$\mathbf{y}$', fontsize=9)
    
    if i < len(x_positions) - 1:
        x_next = x_positions[i + 1]
        ax_right.annotate('', xy=(x_next - 0.9, 4.4), xytext=(x + 0.9, 4.4),
                          arrowprops=dict(arrowstyle='->', color=colors_h, lw=2))
        ax_right.text((x + x_next) / 2, 4.7, r'$\mathbf{h}$',
                      ha='center', va='center', fontsize=9, color=colors_h, fontweight='bold')

ax_right.annotate('', xy=(12.5, 0.6), xytext=(0.5, 0.6),
                  arrowprops=dict(arrowstyle='->', color='#888888', lw=1.5))
ax_right.text(6.5, 0.3, 'Tempo →', ha='center', va='center', fontsize=10, style='italic', color='#888888')

# =============================
# LEGENDA
# =============================
legend_elements = [
    mpatches.Patch(facecolor=colors_cell, edgecolor='black', label='Célula RNN (mesmos parâmetros)'),
    mpatches.FancyArrowPatch((0, 0), (1, 0), color=colors_h, arrowstyle='->', lw=2,
                             label='Estado oculto h_t (memória)'),
]
fig.legend(handles=legend_elements, loc='lower center', ncol=2, fontsize=10,
           frameon=True, fancybox=True, bbox_to_anchor=(0.5, -0.02))

plt.savefig('../images/fig-rnn-unrolling.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.show()
