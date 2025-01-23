import pandas as pd
from pathlib import Path
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
import numpy as np
import json
import json
import logging

def set_data(x, y, z):
    xx, yy, zz, i, j, k = [], [], [], [], [], []
    size = 1
    for index in range(len(x)):
        xx += [x[index], x[index], x[index] + (size), x[index] + (size), x[index], x[index], x[index] + (size),
               x[index] + (size)]
        yy += [y[index], y[index] + (size), y[index] + (size), y[index], y[index], y[index] + (size), y[index] + (size),
               y[index]]
        zz += [z[index], z[index], z[index], z[index], z[index] + (size), z[index] + (size), z[index] + (size),
               z[index] + (size)]

        i += [index * 8 + 7, index * 8 + 0, index * 8 + 0, index * 8 + 0, index * 8 + 4, index * 8 + 4, index * 8 + 6,
              index * 8 + 6, index * 8 + 4, index * 8 + 0, index * 8 + 3, index * 8 + 2]
        j += [index * 8 + 3, index * 8 + 4, index * 8 + 1, index * 8 + 2, index * 8 + 5, index * 8 + 6, index * 8 + 5,
              index * 8 + 2, index * 8 + 0, index * 8 + 1, index * 8 + 6, index * 8 + 3]
        k += [index * 8 + 0, index * 8 + 7, index * 8 + 2, index * 8 + 3, index * 8 + 6, index * 8 + 7, index * 8 + 1,
              index * 8 + 1, index * 8 + 5, index * 8 + 5, index * 8 + 7, index * 8 + 6]
    return xx, yy, zz, i, j, k


def voxel_to_html(voxel_file, html_file, grid_size):
    name = Path(voxel_file).stem
    show_visited = False

    with open(voxel_file, "r") as f:
        data = json.load(f)

    names = ["fill", "visit_by_fs", "surface", "visit_by_edt", "surface_by_edt"]
    colors = iter(["red", "blue", "green", "yellow", "purple"])
    opacities = iter([1, 1, 1, 1, 1])
    gridmap = {}

    if show_visited:
        gridmap["visited"] = data.get('visited', [])
        gridmap["visited_edt"] = data.get('visited_edt', [])
    gridmap["filled"] = data.get('filled', [])
    gridmap["surface"] = data.get('surface', [])
    gridmap["surface_edt"] = data.get('surface_edt', [])
    fig = go.Figure()
    for name, grid in gridmap.items():
        x = [g[0] for g in grid]
        y = [g[1] for g in grid]
        z = [g[2] for g in grid]
        xx, yy, zz, i, j, k = set_data(x, y, z)

        fig.add_trace(
            go.Mesh3d(x=xx, y=yy, z=zz, i=i, j=j, k=k, showscale=True, color=next(colors), name=name, opacity=next(opacities),
                      showlegend=True))
        logging.debug(f"Did {name}")

    fig.update_layout(scene=dict(xaxis=dict(nticks=grid_size, range=[1, grid_size], ),
                                 yaxis=dict(nticks=grid_size, range=[1, grid_size], ),
                                 zaxis=dict(nticks=grid_size, range=[1, grid_size], ), ), showlegend=True)

    logging.debug(f"Writing {html_file}")
    fig.write_html(html_file)


# perhaps make one that slices through the thing?