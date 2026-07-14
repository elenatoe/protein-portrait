import matplotlib.pyplot as plt
import numpy as np
from .colors import hydrophobicity_to_color
import os


def render_protein_portrait(properties, title="Protein Portrait", protein="Protein"):
    """
    Render a protein portrait based on amino acid properties.

    Visual encoding:
    - Angle = sequence position
    - Radius = hydrophobicity
    - Color = hydrophobicity
    - Marker shape = charge
    - Marker size = amino acid size
    """

    num_residues = len(properties)

    angles = np.linspace(0, 2 * np.pi, num_residues, endpoint=False)

    radii = []
    colors = []
    sizes = []
    markers = []

    for residue in properties:
        # Scale radius based on hydrophobicity
        radius = 1 + (residue['hydrophobicity'] * 0.05)
        radii.append(radius)
        colors.append(hydrophobicity_to_color(residue['hydrophobicity']))
        sizes.append(residue['size'])  # Scale size for better visibility
        if residue['charge'] > 0:
            markers.append('^')  # Upward triangle for positive charge
        elif residue['charge'] < 0:
            markers.append('s')  # Square for negative charge
        else:
            markers.append('o')  # Circle for neutral charge

    x = np.array(radii) * np.cos(angles)
    y = np.array(radii) * np.sin(angles)

    fig, ax = plt.subplots(figsize=(8, 8))

    # draw faint circle for reference
    theta = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(theta), 
            np.sin(theta), 
            color='lightgray', 
            linewidth=1)

    # draw radial petals
    for i in range(num_residues):

        ax.plot(
            [0, x[i]],
            [0, y[i]],
            color="gray",
            linewidth=0.4,
            alpha=0.25
        )

    # conenct residues
    ax.plot(
        np.append(x, x[0]),
        np.append(y, y[0]),
        color="black",
        linewidth=1,
        alpha=0.3
    )

    # draw residues
    scatter = None

    for i in range(num_residues):

        scatter = ax.scatter(
            x[i],
            y[i],
            c=[colors[i]],
            s=sizes[i],
            marker=markers[i],
            edgecolors="black",
            linewidth=0.6,
            zorder=3
        )

    # formatting
    cbar = plt.colorbar(scatter, ax=ax, shrink=0.8)
    cbar.set_label("Hydrophobicity (Kyte–Doolittle)")

    ax.set_title(title, fontsize=18)

    ax.set_aspect("equal")
    ax.axis("off")

    plt.tight_layout()

    filename = f"{protein}_portrait.png"
    save_path = os.path.join("figures", filename)

    plt.savefig(
        save_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
