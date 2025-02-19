# A Systematic Review of AI Safety and Safe AI

This repository contains all data and codes to reproduce the results of our article "A Systematic Review of AI Safety and Safe AI" published in Nature Machine Intelligence.

The data consists of annotations and RIS citations of papers retrieved during our systematic database search process and our snowballing process.

## Data

If you want to see a list and citation of all papers used in the analysis, click [PAPERS.md](PAPERS.md).

If you would like to access the data itself used in our analyses you can navigate to the following locations:

- [`data/export`](https://github.com/gyevnarb/ai-safety-review/data/export) contains all retrieved non-duplicate publications in standard CSL JSON, RIS, and BibTex formats.
- [`data/annotations`](https://github.com/gyevnarb/ai-safety-review/data/annotations) contains all selected publications with annotations as described in Section 2.2 of the paper in a JSON format.

## Code

To reproduce our analyses in the paper you will need Python 3.11 and pip installed on your computer.
You need to run the following commands from the root directory of the repository:

```bash
pip install -r requirements.txt
python code/analysis.py
```

This will recreate all figures in the paper into a folder called `output`.

## Please Cite

If you found our work useful and/or used it for your work, we would appreciate you cite our paper:

```text
@article{gyevnar2025AISafety
    title     = {AI Safety for Everyone},
    author    = {Gyevnar, Balint and Kasirzadeh, Atoosa},
    journal   = {Nature Machine Intelligence},
    publisher = {Springer},
    address   = {New York, NY, USA},
    year      = {2025},
    volume    = {},
    issue     = {},
    doi       = {}
}
```
