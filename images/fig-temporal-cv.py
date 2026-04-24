import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Configurações visuais
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10

fig, axes = plt.subplots(3, 1, figsize=(12, 7.2), gridspec_kw={'height_ratios': [1, 2.2, 2.2]})
fig.patch.set_facecolor('white')

colors = {
    'treino': '#4C78A8',
    'teste': '#F58518',
    'nao_usado': '#E0E0E0',
    'futuro': '#B0B0B0'
}

T = 12  # total de observações na série
h = 2   # horizonte de previsão

def draw_timeline(ax, folds_data, y_offset_start=0):
    """
    folds_data: lista de tuplas (treino_start, treino_end, teste_start, teste_end, label)
    """
    y = y_offset_start
    bar_height = 0.55
    gap = 0.30
    
    for tr_s, tr_e, te_s, te_e, label in folds_data:
        # Treino
        ax.barh(y, tr_e - tr_s + 1, left=tr_s - 0.5, height=bar_height,
                color=colors['treino'], edgecolor='black', linewidth=0.6, zorder=3)
        ax.text((tr_s + tr_e) / 2, y, 'Treino', ha='center', va='center',
                color='white', fontweight='bold', fontsize=9, zorder=4)
        
        # Teste
        ax.barh(y, te_e - te_s + 1, left=te_s - 0.5, height=bar_height,
                color=colors['teste'], edgecolor='black', linewidth=0.6, zorder=3)
        ax.text((te_s + te_e) / 2, y, 'Teste', ha='center', va='center',
                color='white', fontweight='bold', fontsize=9, zorder=4)
        
        # Não usado (antes do treino) — apenas para janela deslizante
        if tr_s > 1:
            ax.barh(y, tr_s - 1, left=0.5, height=bar_height,
                    color=colors['nao_usado'], edgecolor='black', linewidth=0.6, zorder=3)
            ax.text((tr_s) / 2, y, '—', ha='center', va='center',
                    color='#888888', fontsize=10, zorder=4)
        
        # Label da dobra
        ax.text(-0.6, y, label, ha='right', va='center', fontsize=10, fontweight='bold')
        
        y -= (bar_height + gap)
    
    return y

def add_axis_ticks(ax, y_pos=-2.6):
    """Adiciona ticks numéricos de 1 a T na base do painel."""
    ax.set_xlim(-2.5, T + 1.5)
    ax.set_ylim(-2.9, 0.8)
    ax.hlines(y_pos, xmin=0.5, xmax=T + 0.5, colors='#cccccc', linewidth=0.8, zorder=1)
    for t in range(1, T + 1):
        ax.vlines(t, ymin=y_pos - 0.05, ymax=y_pos + 0.05, colors='#cccccc', linewidth=0.8, zorder=1)
        ax.text(t, y_pos - 0.22, str(t), ha='center', va='top', fontsize=9, color='#333333')
    ax.text(T + 0.8, y_pos - 0.22, 'Observação ($t$)', ha='left', va='top', fontsize=9, style='italic', color='#555555')
    ax.axis('off')

# =============================
# PAINEL SUPERIOR: Série Temporal
# =============================
ax0 = axes[0]
ax0.set_xlim(0.5, T + 0.5)
ax0.set_ylim(-0.8, 0.8)
ax0.axis('off')
ax0.set_title('Série Temporal Hipotética (observações $t=1$ até $t=12$)', fontsize=12, fontweight='bold', pad=10)

# Caixas para cada ponto no tempo
for t in range(1, T + 1):
    rect = mpatches.FancyBboxPatch((t - 0.4, -0.25), 0.8, 0.5,
                                    boxstyle="round,pad=0.02", 
                                    facecolor='white', edgecolor='black', linewidth=1)
    ax0.add_patch(rect)
    ax0.text(t, 0, f'$t={t}$', ha='center', va='center', fontsize=9, fontweight='bold')

# =============================
# PAINEL DO MEIO: Janela Expansiva
# =============================
ax1 = axes[1]
ax1.set_title('Janela Expansiva (Expanding Window)', fontsize=12, fontweight='bold', loc='left', pad=8)

folds_expansiva = [
    (1, 4, 5, 6, 'Dobra 1'),
    (1, 6, 7, 8, 'Dobra 2'),
    (1, 8, 9, 10, 'Dobra 3'),
]
draw_timeline(ax1, folds_expansiva)
add_axis_ticks(ax1, y_pos=-2.5)

# Seta do tempo
ax1.annotate('', xy=(11, -0.75), xytext=(5, -0.75),
            arrowprops=dict(arrowstyle='->', color='black', lw=1.2))
ax1.text(8, -0.35, 'Tempo →', ha='center', va='center', fontsize=9, style='italic')

# Legenda inline
ax1.text(13.5, -0.3, 'Treino: cresce a cada dobra\nTeste: avança $h=2$ passos',
         ha='left', va='top', fontsize=9,
         bbox=dict(boxstyle='round,pad=0.3', facecolor='#f7f7f7', edgecolor='#cccccc'))

# =============================
# PAINEL INFERIOR: Janela Deslizante
# =============================
ax2 = axes[2]
ax2.set_title('Janela Deslizante (Rolling / Sliding Window)', fontsize=12, fontweight='bold', loc='left', pad=8)

folds_deslizante = [
    (1, 4, 5, 6, 'Dobra 1'),
    (3, 6, 7, 8, 'Dobra 2'),
    (5, 8, 9, 10, 'Dobra 3'),
]
draw_timeline(ax2, folds_deslizante)
add_axis_ticks(ax2, y_pos=-2.5)

ax2.annotate('', xy=(11, -0.75), xytext=(5, -0.75),
            arrowprops=dict(arrowstyle='->', color='black', lw=1.2))
ax2.text(8, -0.35, 'Tempo →', ha='center', va='center', fontsize=9, style='italic')

ax2.text(13.5, -0.3, 'Treino: tamanho fixo ($w=4$)\nTeste: avança $h=2$ passos',
         ha='left', va='top', fontsize=9,
         bbox=dict(boxstyle='round,pad=0.3', facecolor='#f7f7f7', edgecolor='#cccccc'))

# Legenda geral
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=colors['treino'], edgecolor='black', label='Treino'),
    Patch(facecolor=colors['teste'], edgecolor='black', label='Teste (avaliação)'),
    Patch(facecolor=colors['nao_usado'], edgecolor='black', label='Descartado / não utilizado'),
]
fig.legend(handles=legend_elements, loc='lower center', ncol=3, fontsize=10,
           frameon=True, fancybox=True, bbox_to_anchor=(0.5, -0.02))

plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.savefig('../images/fig-temporal-cv.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.show()
