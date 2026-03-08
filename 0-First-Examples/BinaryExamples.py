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
    # Plotting Isobaric Binary Phase Diagrams with `binplot`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    These are a few examples of how to use Thermo-Calc TDB files to calculate isobaric binary phase diagrams. As long as the TDB file is present, each cell in these examples is self contained and can completely reproduce the figure shown.

    ### binplot

    The phase diagrams are computed with `binplot`, which has four required arguments:
    1. The Database object
    2. A list of active components (vacancies (`VA`), which are present in many databases, must be included explictly).
    3. A list of phases to consider in the calculation
    4. A dictionary conditions to consider, with keys of pycalphad StateVariables and values of scalars, 1D arrays, or `(start, stop, step)` ranges

    Note that, at the time of writing, invariant reactions (three-phase 'regions' on binary diagrams) are not yet automatically detected so they
    are not drawn on the diagram.

    Also note that the [magic variable](https://ipython.readthedocs.io/en/stable/interactive/magics.html) `%matplotlib inline` should only be used in Jupyter notebooks.


    ### TDB files

    The TDB files should be located in the current working directory of the notebook. If you are running using a Jupyter notebook, the default working directory is the directory that that notebook is saved in.

    To check the working directory, run:

    ```python
    import os
    print(os.path.abspath(os.curdir))
    ```

    TDB files can be found in the literature. The [Thermodynamic DataBase DataBase](https://avdwgroup.engin.brown.edu) (TDBDB) has indexed many available databases and links to the original papers and/or TDB files where possible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Path setup
    """)
    return


@app.cell
def _(mo):
    from pathlib import Path

    notebook_path = mo.notebook_location()
    database_path = Path(notebook_path).parent.joinpath("databases")
    return Path, database_path, notebook_path


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Imports
    """)
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    from pycalphad import Database, binplot, variables as v

    return Database, binplot, plt, v


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Al-Zn (S. Mey, 1993)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The miscibility gap in the fcc phase is included in the Al-Zn diagram, shown below.

    The format for specifying a range of a state variable is (*start*, *stop*, *step*).

    S. an Mey, Zeitschrift für Metallkunde 84(7) (1993) 451-455.
    """)
    return


@app.cell
def _(Database, Path, binplot, database_path, plt, v):
    _alzn_path = Path(database_path).joinpath("alzn_mey.tdb")
    _db_alzn = Database(_alzn_path)
    _my_phases_alzn = ["LIQUID", "FCC_A1", "HCP_A3"]
    _fig = plt.figure(figsize=(9, 6))
    _axes = _fig.gca()
    binplot(
        database=_db_alzn,
        components=["AL", "ZN", "VA"],
        phases=_my_phases_alzn,
        conditions={v.X("ZN"): (0, 1, 0.02), v.T: (300, 1000, 10), v.P: 101325, v.N: 1},
        plot_kwargs={"ax": _axes},
    )
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Al-Mg (Y. Zhong, 2005)

    Y. Zhong, M. Yang, Z.-K. Liu, CALPHAD 29 (2005) 303-311 doi:[10.1016/j.calphad.2005.08.004](https://doi.org/10.1016/j.calphad.2005.08.004)
    """)
    return


@app.cell
def _(Database, Path, binplot, database_path, plt, v):
    _almg_path = Path(database_path).joinpath("Al-Mg_Zhong.tdb")
    _dbf = Database(_almg_path)
    _comps = ["AL", "MG", "VA"]
    _phases = _dbf.phases.keys()
    binplot(_dbf, _comps, _phases, {v.N: 1, v.P: 101325, v.T: (300, 1000, 10), v.X("MG"): (0, 1, 0.02)})
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Al-Ni (Dupin, 2001)

    Components and conditions can also be stored as variables and passed to binplot.

    N. Dupin, I. Ansara, B. Sundman, CALPHAD 25(2) (2001) 279-298 doi:[10.1016/S0364-5916(01)00049-9](https://doi.org/10.1016/S0364-5916(01)00049-9)
    """)
    return


@app.cell
def _(Database, Path, binplot, database_path, plt, v):
    _ni_al_path = Path(database_path).joinpath("NI_AL_DUPIN_2001.TDB")
    _dbf = Database(_ni_al_path)
    _comps = ["AL", "NI", "VA"]
    _phases = list(_dbf.phases.keys())
    conds = {v.N: 1, v.P: 101325, v.T: (300, 2000, 10), v.X("AL"): (1e-05, 1, 0.02)}
    _fig = plt.figure(figsize=(9, 6))
    _axes = _fig.gca()
    binplot(_dbf, _comps, _phases, conds, plot_kwargs={"ax": _axes})
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Al-Fe (M. Seiersten, 1991)

    Removing tielines
    """)
    return


@app.cell
def _(Database, Path, binplot, database_path, plt, v):
    _alfe_path = Path(database_path).joinpath("alfe_sei.TDB")
    db_alfe = Database(_alfe_path)
    my_phases_alfe = ["LIQUID", "B2_BCC", "FCC_A1", "HCP_A3", "AL5FE2", "AL2FE", "AL13FE4", "AL5FE4"]
    _fig = plt.figure(figsize=(9, 6))
    _axes = _fig.gca()
    binplot(
        db_alfe,
        ["AL", "FE", "VA"],
        my_phases_alfe,
        {v.X("AL"): (0, 1, 0.01), v.T: (300, 2000, 10), v.P: 101325},
        plot_kwargs={"ax": _axes, "tielines": False},
    )
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Nb-Re (Liu, 2013)

    X.L. Liu, C.Z. Hargather, Z.-K. Liu, CALPHAD 41 (2013) 119-127 doi:[10.1016/j.calphad.2013.02.006](https://doi.org/10.1016/j.calphad.2013.02.006)
    """)
    return


@app.cell
def _(Database, Path, binplot, database_path, plt, v):
    _nbre_path = Path(database_path).joinpath("nbre_liu.tdb")
    db_nbre = Database(_nbre_path)
    my_phases_nbre = ["CHI_RENB", "SIGMARENB", "FCC_RENB", "LIQUID_RENB", "BCC_RENB", "HCP_RENB"]
    _fig = plt.figure(figsize=(9, 6))
    _axes = _fig.gca()
    binplot(
        db_nbre,
        ["NB", "RE"],
        my_phases_nbre,
        {v.X("RE"): (0, 1, 0.01), v.T: (1000, 3500, 20), v.P: 101325},
        plot_kwargs={"ax": _axes},
    )
    _axes.set_xlim(0, 1)
    plt.show()
    return


if __name__ == "__main__":
    app.run()
