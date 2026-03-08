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
def _(Database, Path, binplot, database_path, plt, v):
    _alzn_path = Path(database_path).joinpath("alzn_mey.tdb")
    _db_alzn = Database(_alzn_path)

    from pycalphad.core.utils import filter_phases

    all_available_phases = filter_phases(_db_alzn, ["AL", "ZN", "VA"])

    _fig = plt.figure(figsize=(9, 6))
    _axes = _fig.gca()
    binplot(
        database=_db_alzn,
        components=["AL", "ZN", "VA"],
        phases=all_available_phases,
        conditions={v.X("ZN"): (0, 1, 0.02), v.T: (300, 1000, 10), v.P: 101325, v.N: 1},
        plot_kwargs={"ax": _axes},
    )
    plt.show()
    return


if __name__ == "__main__":
    app.run()
