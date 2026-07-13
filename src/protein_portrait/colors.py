"""
Color utilities for protein portrait visualization.

Hydrophobicity colors:
    Based on Kyte-Doolittle hydropathy values.

Charge colors:
    Positive / neutral / negative residue visualization.
"""

import matplotlib
import matplotlib.colors as mcolors


# Hydrophobicity range from Kyte-Doolittle scale
HYDROPHOBICITY_MIN = -4.5
HYDROPHOBICITY_MAX = 4.5


# Colormap used for hydrophobicity
HYDROPHOBICITY_COLORMAP = "coolwarm"


# Charge colors
CHARGE_COLORS = {
    1: "royalblue",   # positively charged residues: K, R
    0: "gray",        # neutral residues
    -1: "crimson"     # negatively charged residues: D, E
}


def hydrophobicity_to_color(value):
    """
    Convert Kyte-Doolittle hydrophobicity value into a color.

    Args:
        value (float): Hydrophobicity value (-4.5 to 4.5)

    Returns:
        RGBA color
    """

    normalized = mcolors.Normalize(
        vmin=HYDROPHOBICITY_MIN,
        vmax=HYDROPHOBICITY_MAX
    )

    colormap = matplotlib.colormaps[HYDROPHOBICITY_COLORMAP]
    return colormap(normalized(value))


def charge_to_color(charge):
    """
    Convert amino acid charge into a color.

    Args:
        charge (int):
            +1 positive
             0 neutral
            -1 negative

    Returns:
        color name
    """

    return CHARGE_COLORS.get(charge, "black")
