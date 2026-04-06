import matplotlib.pyplot as plt
import numpy as np

thresholds = [100, 200, 500, 1000, 2000]

old_hit_rate      = [0.5513, 0.6038, 0.6693, 0.7538, 1.0000]
old_vectors       = [66.82,  143.29, 367.52, 500.86, 1321.00]
old_score_acc     = [0.9222, 0.9296, 0.9511, 0.9676, 1.0000]
old_final_score   = [19.8676, 8.8994, 3.5376, 2.6364, 1.0000]

new_hit_rate      = [0.7120, 0.7608, 0.8885, 0.9613, 1.0000]
new_vectors       = [134.57, 290.55, 708.45, 935.72, 1321.00]
new_score_acc     = [0.8583, 0.8525, 0.8764, 0.8808, 0.9997]
new_final_score   = [8.5501, 3.9263, 1.6413, 1.2629, 0.9997]

x = np.arange(len(thresholds))
width = 0.35
labels = [str(t) for t in thresholds]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Single-Probe vs Multi-Probe Search Comparison", fontsize=15, fontweight='bold')

# 1. Hit Rate
ax = axes[0, 0]
ax.bar(x - width/2, old_hit_rate, width, label='Single-Probe', color='steelblue')
ax.bar(x + width/2, new_hit_rate, width, label='Multi-Probe',  color='tomato')
ax.set_title('Hit Rate')
ax.set_xticks(x); ax.set_xticklabels(labels)
ax.set_xlabel('MAX_VECTORS_PER_NODE Threshold')
ax.set_ylabel('Hit Rate')
ax.set_ylim(0, 1.1)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.5)

# 2. Avg Vectors Searched
ax = axes[0, 1]
ax.plot(labels, old_vectors, 'o-', color='steelblue', label='Single-Probe', linewidth=2)
ax.plot(labels, new_vectors, 's-', color='tomato',    label='Multi-Probe',  linewidth=2)
ax.set_title('Average Vectors Searched')
ax.set_xlabel('MAX_VECTORS_PER_NODE Threshold')
ax.set_ylabel('Vectors Searched')
ax.legend()
ax.grid(linestyle='--', alpha=0.5)

# 3. Score Accuracy
ax = axes[1, 0]
ax.plot(labels, old_score_acc, 'o-', color='steelblue', label='Single-Probe', linewidth=2)
ax.plot(labels, new_score_acc, 's-', color='tomato',    label='Multi-Probe',  linewidth=2)
ax.set_title('Score Accuracy')
ax.set_xlabel('MAX_VECTORS_PER_NODE Threshold')
ax.set_ylabel('Score Accuracy')
ax.set_ylim(0.8, 1.05)
ax.legend()
ax.grid(linestyle='--', alpha=0.5)

# 4. Final Score
ax = axes[1, 1]
ax.plot(labels, old_final_score, 'o-', color='steelblue', label='Single-Probe', linewidth=2)
ax.plot(labels, new_final_score, 's-', color='tomato',    label='Multi-Probe',  linewidth=2)
ax.set_title('Final Total Score (higher = better efficiency)')
ax.set_xlabel('MAX_VECTORS_PER_NODE Threshold')
ax.set_ylabel('Final Score')
ax.legend()
ax.grid(linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('./probe_comparison.png', dpi=150, bbox_inches='tight')
print("Saved to probe_comparison.png")