import marimo

__generated_with = "0.20.4"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Imports
    """)
    return


@app.cell
def _(mo):
    from pathlib import Path

    import matplotlib.pyplot as plt
    from pycalphad import Database, binplot
    from pycalphad import variables as v

    notebook_path = mo.notebook_location()
    database_path = Path(notebook_path).parent.joinpath("databases")
    return Database, Path, binplot, database_path, plt, v


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Al-Zn (S. Mey, 1993)

    The miscibility gap in the fcc phase is included in the Al-Zn diagram, shown below.

    The format for specifying a range of a state variable is (*start*, *stop*, *step*).

    S. an Mey, Zeitschrift für Metallkunde 84(7) (1993) 451-455.
    """)
    return


@app.cell
def _(Database, Path, database_path):
    _alzn_path = Path(database_path).joinpath("alzn_mey.tdb")
    db_alzn = Database(_alzn_path)
    return (db_alzn,)


@app.cell
def _(binplot, db_alzn, plt, v):
    from pycalphad.core.utils import filter_phases

    # Is there a way to get all available components in a database?
    # A tentative way is to get this list via species or elements from Database instance
    available_elements = db_alzn.elements
    available_elements.remove("/-")

    all_available_phases = filter_phases(db_alzn, available_elements)

    _fig = plt.figure(figsize=(9, 6))
    _axes = _fig.gca()
    binplot(
        database=db_alzn,
        components=available_elements,
        phases=all_available_phases,
        conditions={v.X("ZN"): (0, 1, 0.02), v.T: (300, 1000, 10), v.P: 101325, v.N: 1},
        plot_kwargs={"ax": _axes},
    )
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Exploring database object
    """)
    return


@app.cell
def _(db_alzn):
    print("Elements:")
    for e in db_alzn.elements:
        print(e)
    return


@app.cell
def _(db_alzn):
    print("Species:")
    for s in iter(db_alzn.species):
        print(s)
    return


@app.cell
def _(db_alzn):
    print("Phases:")
    for p, pd in db_alzn.phases.items():
        print(p)
        print(f"{pd}\n")
    return


@app.cell
def _(db_alzn):
    print("Symbols")

    for syk, syv in db_alzn.symbols.items():
        print(syk)
        print(f"{syv}\n")
    return


@app.cell
def _(db_alzn):
    db_alzn.references
    return


if __name__ == "__main__":
    app.run()
