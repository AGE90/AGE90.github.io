"""Site chart theme for Plotly and matplotlib.

In a post:  `import sys; sys.path.insert(0, "../../viz"); import theme; theme.use("light")`
Palette = dataviz reference palette (validated for CVD in both modes); keep slot order.
"""

PALETTE = {
    "light": dict(surface="#fcfcfb", ink="#0b0b0b", ink2="#52514e", muted="#898781", grid="#e1e0d9",
                  series=["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948"]),
    "dark": dict(surface="#1a1a19", ink="#ffffff", ink2="#c3c2b7", muted="#898781", grid="#2c2c2a",
                 series=["#3987e5", "#d95926", "#199e70", "#c98500", "#d55181", "#008300", "#9085e9", "#e66767"]),
}
FONT = "Inter, system-ui, -apple-system, Segoe UI, sans-serif"


def use(mode="light"):
    """Register the 'age90' Plotly template and matplotlib style for `mode` ('light' | 'dark')."""
    p = PALETTE[mode]
    try:
        import plotly.graph_objects as go
        import plotly.io as pio

        axis = dict(gridcolor=p["grid"], linecolor=p["muted"], zeroline=False, tickcolor=p["muted"],
                    title_font_color=p["ink2"], tickfont_color=p["ink2"])
        pio.templates["age90"] = go.layout.Template(layout=dict(
            colorway=p["series"], font=dict(family=FONT, color=p["ink"], size=14),
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            xaxis=axis, yaxis=axis, hoverlabel=dict(font_family=FONT),
            legend=dict(orientation="h", y=1.08, x=0), margin=dict(l=48, r=16, t=48, b=40)))
        pio.templates.default = "age90"
    except ImportError:
        pass
    try:
        import matplotlib as mpl
        from cycler import cycler

        mpl.rcParams.update({
            "axes.prop_cycle": cycler(color=p["series"]),
            "figure.facecolor": "none", "axes.facecolor": "none", "savefig.transparent": True,
            "text.color": p["ink"], "axes.labelcolor": p["ink2"], "axes.edgecolor": p["muted"],
            "xtick.color": p["ink2"], "ytick.color": p["ink2"],
            "axes.spines.top": False, "axes.spines.right": False,
            "axes.grid": True, "grid.color": p["grid"], "grid.linewidth": 0.8,
            "lines.linewidth": 2, "font.family": "sans-serif",
            "font.sans-serif": ["Inter", "DejaVu Sans"], "figure.dpi": 120,
        })
    except ImportError:
        pass
    return p
