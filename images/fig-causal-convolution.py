import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10

fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
fig.patch.set_facecolor('white')

T = 6
series = [3, 5, 2, 7, 4, 6]
colors_serie = '#4C78A8'
colors_kernel = '#F58518'
colors_proibido = '#E45756'

def draw_series(ax, title, is_causal):
    ax.set_xlim(-0.5, T + 2.5)
    ax.set_ylim(-1.5, 3.5)
    ax.axis('off')
    ax.set_title(title, fontsize=12, fontweight='bold', pad=10)
    
    for t in range(T):
        ax.text(t, -0.6, f'$x_{{{t+1}}}$', ha='center', va='center', fontsize=10)
    ax.text(T + 1.2, -0.6, '$t$', ha='center', va='center', fontsize=10, style='italic')
    
    for t, val in enumerate(series):
        bar_height = val * 0.25
        rect = plt.Rectangle((t - 0.35, 0), 0.7, bar_height,
                              facecolor=colors_serie, edgecolor='black', linewidth=0.8, zorder=3)
        ax.add_patch(rect)
        ax.text(t, bar_height + 0.15, str(val), ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    target_idx = 2
    
    if is_causal:
        kernel_positions = [0, 1, 2]
        label_text = r'$y_3 = w_1 x_1 + w_2 x_2 + w_3 x_3$'
        subtitle = 'Só usa passado e presente'
        box_edge = '#4caf50'
        box_face = '#e8f5e9'
        text_color = '#2e7d32'
    else:
        kernel_positions = [1, 2, 3]
        label_text = r'$y_3 = w_1 x_2 + w_2 x_3 + w_3 x_4$'
        subtitle = 'Usa informação do futuro!'
        box_edge = '#E45756'
        box_face = '#ffebee'
        text_color = '#c62828'
    
    for i, kp in enumerate(kernel_positions):
        rect = plt.Rectangle((kp - 0.35, 2.0), 0.7, 0.55,
                              facecolor=colors_kernel, edgecolor='black', linewidth=1, zorder=4, alpha=0.85)
        ax.add_patch(rect)
        ax.text(kp, 2.27, f'$w_{{{i+1}}}$', ha='center', va='center',
                fontsize=9, fontweight='bold', color='white')
    
    ax.add_patch(plt.Rectangle((target_idx - 0.35, 0), 0.7, series[target_idx] * 0.25,
                                facecolor='none', edgecolor='#E45756', linewidth=3, zorder=5, linestyle='--'))
    ax.text(target_idx, -1.1, r'$\mathbf{y_3}$', ha='center', va='center',
            fontsize=11, fontweight='bold', color='#E45756')
    
    if not is_causal:
        ax.text(3, 0.6, 'futuro!', ha='center', va='center',
                fontsize=8, color='#E45756', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='#E45756', linewidth=1))
        ax.annotate('', xy=(3, 0.35), xytext=(3, 1.7),
                   arrowprops=dict(arrowstyle='->', color='#E45756', lw=1.5, ls='--'))
    
    ax.text(2.5, 3.2, label_text, ha='center', va='center', fontsize=10,
            color='#333333',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=box_face, edgecolor=box_edge, linewidth=1.5))
    ax.text(2.5, 2.85, subtitle, ha='center', va='center', fontsize=9, color=text_color)

draw_series(axes[0], 'Convolução Padrão (centrada)', is_causal=False)
draw_series(axes[1], 'Convolução Causal', is_causal=True)

legend_elements = [
    mpatches.Patch(facecolor=colors_serie, edgecolor='black', label='Série de entrada'),
    mpatches.Patch(facecolor=colors_kernel, edgecolor='black', label='Kernel / filtro'),
    mpatches.Patch(facecolor='none', edgecolor='#E45756', linewidth=2, linestyle='--', label='Elemento sendo calculado'),
]
fig.legend(handles=legend_elements, loc='lower center', ncol=3, fontsize=10,
           frameon=True, fancybox=True, bbox_to_anchor=(0.5, -0.02))

plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.savefig('../images/fig-causal-convolution.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.show()
