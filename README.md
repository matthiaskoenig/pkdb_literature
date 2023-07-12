# pkdb_literature


## Install

```bash
git clone https://github.com/matthiaskoenig/pkdb_literature.git
cd pkdb_literature
pip install -e .[development] --upgrade
```

## Retrieve PDFs via Sci-hub

- Go to the zotero library
- Select items without PDF attachment
- right click -> Export items -> `CSV` -> `<substance>.doi`

Run script from `src/pkdb_literature/scihub.tools`

```
python scihub_tools.py -f /home/mkoenig/git/pkdb_literature/dois/Ppp1r3b_dois.txt -o /home/mkoenig/git/pkdb_literature/results/Ppp1r3b
```

