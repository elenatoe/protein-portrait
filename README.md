# protein-portrait



Generate art portraits from protein amino acid sequences by mapping biochemical properties into geometric and color patterns.



## Overview



Protein Portrait is a Python project that transforms any amino acid sequence into a visual artwork.



Each residue contributes to the final image using its biochemical properties:



- **Hydrophobicity** determines radial distance.

- **Charge** determines color.

- **Molecular size** determines marker size.

- **Sequence position** determines angular placement.



The goal is to combine protein biophysics with generative art to create visually distinct "portraits" for different proteins.



Example input:



```text

MVLSPADKTNVKAAWGKV...

```



Output:



- High-resolution PNG artwork

- Reproducible visualization for any protein sequence



## Project Structure



- **parser.py** — reads FASTA protein sequences

- **properties.py** — amino acid biochemical property tables

- **renderer.py** — generates the portrait visualization

- **colors.py** — color palettes and property mappings



## Status



In development.



Current goals:



- FASTA parser

- Amino acid property database

- Spiral renderer

- PNG export



Planned:



- Multiple visualization styles

- Interactive Streamlit web app

- Animated portrait generation



## Install



```bash

git clone https://github.com/[your-username]/protein-portrait.git

cd protein-portrait

pip install -r requirements.txt

```



## License



MIT
