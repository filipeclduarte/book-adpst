import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10

fig, ax = plt.subplots(figsize=(11, 7))
ax.set_xlim(0, 11)
ax.set_ylim(0, 8)
ax.axis('off')
fig.patch.set_facecolor('white')

# Cores das camadas
colors = {
    'input': '#4C78A8',
    'hidden1': '#F58518',
    'hidden2': '#E45756',
    'output': '#72B7B2',
    'conn': '#888888',
    'text': '#333333'
}

def draw_neuron(ax, x, y, color, label, radius=0.28):
    """Desenha um neurônio como círculo com label."""
    circle = plt.Circle((x, y), radius, facecolor=color, edgecolor='black',
                        linewidth=1.2, zorder=4)
    ax.add_patch(circle)
    ax.text(x, y, label, ha='center', va='center', fontsize=9,
            color='white', fontweight='bold', zorder=5)

def draw_connection(ax, x1, y1, x2, y2, color='#888888', lw=0.6):
    """Desenha uma linha de conexão entre dois neurônios."""
    ax.plot([x1, x2], [y1, y2], color=color, linewidth=lw, zorder=1, alpha=0.6)

# =============================
# CONFIGURAÇÃO DAS CAMADAS
# =============================

# Número de neurônios visíveis por camada (mostramos alguns + "...")
n_input = 4     # x1, x2, x3, xp
n_hidden1 = 4   # h1_1 .. h1_4
n_hidden2 = 3   # h2_1 .. h2_3
n_output = 1    # y_pred

# Posições X das camadas
x_input = 1.5
x_hidden1 = 4.2
x_hidden2 = 6.9
x_output = 9.6

# Posições Y (centralizadas)
def y_positions(n, y_center=4.0, spacing=1.1):
    if n == 1:
        return [y_center]
    total_h = (n - 1) * spacing
    start = y_center + total_h / 2
    return [start - i * spacing for i in range(n)]

y_in = y_positions(n_input, 4.0, 1.15)
y_h1 = y_positions(n_hidden1, 4.0, 1.15)
y_h2 = y_positions(n_hidden2, 4.0, 1.15)
y_out = y_positions(n_output, 4.0, 1.15)

# =============================
# DESENHA CONEXÕES (antes dos neurônios para ficar por baixo)
# =============================

# Entrada -> Hidden 1
for yi in y_in:
    for yh in y_h1:
        draw_connection(ax, x_input + 0.28, yi, x_hidden1 - 0.28, yh)

# Hidden 1 -> Hidden 2
for yh1 in y_h1:
    for yh2 in y_h2:
        draw_connection(ax, x_hidden1 + 0.28, yh1, x_hidden2 - 0.28, yh2)

# Hidden 2 -> Saída
for yh2 in y_h2:
    for yo in y_out:
        draw_connection(ax, x_hidden2 + 0.28, yh2, x_output - 0.28, yo)

# =============================
# DESENHA NEURÔNIOS
# =============================

# Camada de entrada
input_labels = [r'$x_1$', r'$x_2$', r'$x_3$', r'$x_p$']
for y, lab in zip(y_in, input_labels):
    draw_neuron(ax, x_input, y, colors['input'], lab)

# Camada oculta 1
h1_labels = [r'$h_1^{(1)}$', r'$h_2^{(1)}$', r'$h_3^{(1)}$', r'$\dots$']
for y, lab in zip(y_h1, h1_labels):
    draw_neuron(ax, x_hidden1, y, colors['hidden1'], lab)

# Camada oculta 2
h2_labels = [r'$h_1^{(2)}$', r'$h_2^{(2)}$', r'$h_3^{(2)}$']
for y, lab in zip(y_h2, h2_labels):
    draw_neuron(ax, x_hidden2, y, colors['hidden2'], lab)

# Camada de saída
for y, lab in zip(y_out, [r'$\hat{y}$']):
    draw_neuron(ax, x_output, y, colors['output'], lab)

# =============================
# LABELS DAS CAMADAS
# =============================

ax.text(x_input, 7.2, 'Camada de Entrada', ha='center', va='center',
        fontsize=11, fontweight='bold', color=colors['input'])
ax.text(x_input, 6.7, r'($p$ features)', ha='center', va='center',
        fontsize=9, color='#555555')

ax.text(x_hidden1, 7.2, 'Camada Oculta 1', ha='center', va='center',
        fontsize=11, fontweight='bold', color=colors['hidden1'])
ax.text(x_hidden1, 6.7, r'$f^{(1)} = \mathrm{ReLU}$', ha='center', va='center',
        fontsize=9, color='#555555')

ax.text(x_hidden2, 7.2, 'Camada Oculta 2', ha='center', va='center',
        fontsize=11, fontweight='bold', color=colors['hidden2'])
ax.text(x_hidden2, 6.7, r'$f^{(2)} = \mathrm{ReLU}$', ha='center', va='center',
        fontsize=9, color='#555555')

ax.text(x_output, 7.2, 'Camada de Saída', ha='center', va='center',
        fontsize=11, fontweight='bold', color=colors['output'])
ax.text(x_output, 6.7, r'(previsão)', ha='center', va='center',
        fontsize=9, color='#555555')

# =============================
# SETAS DE FLUXO
# =============================

arrow_y = 4.0
for x_start, x_end in [(x_input + 0.7, x_hidden1 - 0.7),
                        (x_hidden1 + 0.7, x_hidden2 - 0.7),
                        (x_hidden2 + 0.7, x_output - 0.7)]:
    ax.annotate('', xy=(x_end, arrow_y), xytext=(x_start, arrow_y),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
                zorder=6)

# =============================
# PAINEL DE NOTAÇÃO MATEMÁTICA
# =============================

notation_text = (
    r'$\mathbf{z}^{[\ell]} = \mathbf{W}^{[\ell]} \mathbf{a}^{[\ell-1]} + \mathbf{b}^{[\ell]}$' + '\n' +
    r'$\mathbf{a}^{[\ell]} = f^{[\ell]}(\mathbf{z}^{[\ell]})$'
)
ax.text(5.5, 0.6, notation_text, ha='center', va='center', fontsize=10,
        color=colors['text'],
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#f7f7f7',
                  edgecolor='#cccccc', linewidth=1))

# =============================
# LEGENDA
# =============================

legend_elements = [
    mpatches.Patch(facecolor=colors['input'], edgecolor='black', label='Entrada (features)'),
    mpatches.Patch(facecolor=colors['hidden1'], edgecolor='black', label='Oculta (ReLU)'),
    mpatches.Patch(facecolor=colors['hidden2'], edgecolor='black', label='Oculta (ReLU)'),
    mpatches.Patch(facecolor=colors['output'], edgecolor='black', label='Saída (previsão)'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=9,
          frameon=True, fancybox=True, bbox_to_anchor=(1.02, -0.02))

plt.tight_layout()
plt.savefig('../images/fig-mlp-architecture.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.show()
