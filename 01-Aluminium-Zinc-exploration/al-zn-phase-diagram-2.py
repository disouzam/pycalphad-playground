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

    fig = plt.figure(figsize=(9, 6))
    axes = fig.gca()

    # Chart title is added automatically
    binplot(
        database=db_alzn,
        components=available_elements,
        phases=all_available_phases,
        conditions={v.X("ZN"): (0, 1, 0.02), v.T: (300, 1000, 10), v.P: 101325, v.N: 1},
        plot_kwargs={"ax": axes},
    )

    # But through matplotlib / Python magic, it can be modified afterwards
    axes.title.set_text("Al-Zn phase diagram")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Uses of Al-Zn - quick info

    Source: https://en.wikipedia.org/wiki/Zinc_aluminium

    Zinc-aluminium (ZA) alloys are alloys whose main constituents are zinc and aluminium. Other alloying elements include magnesium and copper. This type of alloy was originally developed for gravity casting. Noranda, New Jersey Zinc Co. Ltd., St. Joe Mineral Co. and the International Lead Zinc Research Organization (ILZRO) were the main companies that pioneered the ZA alloys between the 1950s and the 1970s. They were designed to compete with bronze, cast iron and aluminium using sand and permanent mold casting methods. Distinguishing features of ZA alloys include high as-cast strength, excellent bearing properties, as well as low energy requirements (for melting).

    ZA alloys make good bearings because their final composition includes hard eutectic zinc-aluminium-copper particles embedded in a softer zinc-aluminium matrix. The hard particles provide a low-friction bearing surface, while the softer material wears back to provide space for lubricant to flow, similar to Babbitt metal.
    """)
    return


if __name__ == "__main__":
    app.run()
