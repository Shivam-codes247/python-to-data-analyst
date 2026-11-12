# Python to Data Analyst 📊

My public learning log on the way to a **junior Data Analyst** role. I'm learning Python, Pandas, SQL and data visualization step by step, and every notebook and script here is my own practice work.

**Started:** September 2026 · **Currently learning:** SQL and data visualization · **Next:** an original end-to-end project

[LinkedIn](https://www.linkedin.com/in/shivam--tech) · [Email](mailto:shivam.code247@gmail.com)

---

## Progress

| Topic | Status | What's inside |
|-------|--------|---------------|
| [Python fundamentals](01_Python_Fundamentals/) | ✅ Done | Variables, operators, conditionals, loops, string slicing, 20+ practice problems |
| [NumPy](03_NumPy/) | ✅ Done | Array creation, indexing, slicing, reshaping, filtering, calculations |
| [Pandas](04_Pandas/) | ✅ Done | 9 class notebooks, from DataFrames to time series, plus 2 practice projects |
| [Data visualization](05_Data_Visualization/) | 🔄 In progress | Matplotlib done, Seaborn next |
| [SQL](07_SQL/) | 🔄 In progress | PostgreSQL basics, constraints, practice databases |
| Statistics and probability | ⏳ Planned | |
| Exploratory data analysis | ⏳ Planned | |
| Excel | ⏳ Planned | |
| Power BI | ⏳ Planned | |
| Portfolio projects | ⏳ Planned | |

---

## Featured work

| Project | Tools | What it shows |
|---------|-------|---------------|
| [Retail sales analysis](04_Pandas/Retail_sales_analysis/) | Python, Pandas, NumPy | Guided course project on the Superstore dataset (2014–2017): cleaning, category and region profit, time-series trends, rolling averages, business recommendations |
| [Student performance analysis](04_Pandas/practice_project_01/) | Python, Pandas | 30+ questions on a large student dataset: filtering, feature creation, ranking |
| [Tic Tac Toe game](01_Python_Fundamentals/Tic%20Tac%20Toe/) | Python, NumPy, Streamlit | A small interactive app with the game logic kept separate from the UI |

> The retail project is a guided classroom project. My own end-to-end analysis (own dataset, own questions, own findings) is the next milestone.

---

## Repository structure

```
python-to-data-analyst/
├── 01_Python_Fundamentals/   # basics, operators, conditionals, loops, Tic Tac Toe
├── 03_NumPy/                 # array practice notebook
├── 04_Pandas/                # class notebooks + practice projects
├── 05_Data_Visualization/    # Matplotlib, Seaborn
├── 07_SQL/                   # PostgreSQL practice files and sample databases
├── .gitignore
└── README.md
```

---

## Skills so far

- **Python:** data types, control flow, loops, functions, string handling
- **NumPy:** arrays, vectorized operations, boolean filtering
- **Pandas:** cleaning, filtering, `groupby`, pivot tables, merge/join, datetime and resampling, `apply`/`map`
- **Visualization:** Matplotlib figures, subplots, styling, scatter, histogram and boxplot
- **SQL (PostgreSQL):** creating databases and tables, data types, primary keys, `NOT NULL`, `UNIQUE`, `DEFAULT`

---

## Running things locally

```bash
git clone https://github.com/Shivam-codes247/python-to-data-analyst.git
cd python-to-data-analyst

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

jupyter notebook
```

**Tic Tac Toe:** `streamlit run "01_Python_Fundamentals/Tic Tac Toe/main.py"`

**SQL practice:** requires PostgreSQL. Load the sample databases into a disposable practice database, not one you care about, because the scripts drop and recreate tables:

```bash
psql -d hr -f 07_SQL/01_practice_data/hr_postgres.sql
```

---

## Roadmap

- [x] Python fundamentals
- [x] NumPy
- [x] Pandas
- [ ] Matplotlib ✅ / Seaborn
- [ ] SQL: joins, aggregations, subqueries, window functions
- [ ] Statistics and probability
- [ ] Excel and Power BI dashboard
- [ ] Original end-to-end portfolio project (Python + SQL + dashboard)
- [ ] Start applying for junior analyst roles
