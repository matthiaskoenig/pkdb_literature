# pkdb_literature


## Install

```bash
git clone https://github.com/matthiaskoenig/pkdb_literature.git
cd pkdb_literature
pip install -e .[development] --upgrade
```


## Retrieve PDFs via Sci-hub

- Open the zotero library
- Select items without PDF attachment
- right click -> Export items -> `CSV` -> `<substance>.txt`
- create DOI file with `dois_from_csv.py`

Run script from `src/pkdb_literature/scihub.tools`

```
python scihub_tools.py -f /home/mkoenig/git/pkdb_literature/dois/enalapril_dois.txt -o /home/mkoenig/git/pkdb_literature/results/enalapril
python scihub_tools.py -f /home/mkoenig/git/pkdb_literature/dois/Ppp1r3b_dois.txt -o /home/mkoenig/git/pkdb_literature/results/Ppp1r3b
python scihub_tools.py -f /home/mkoenig/git/pkdb_literature/dois/ethinylestradiol_dois.txt -o /home/mkoenig/git/pkdb_literature/results/ethinylestradiol
python scihub_tools.py -f /home/mkoenig/git/pkdb_literature/dois/HCTZ_dois.txt -o /home/mkoenig/git/pkdb_literature/results/HCTZ
python scihub_tools.py -f /home/mkoenig/git/pkdb_literature/dois/aliskiren_dois.txt -o /home/mkoenig/git/pkdb_literature/results/aliskiren
```

