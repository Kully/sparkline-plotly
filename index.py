import random

import dash
from dash import dcc, html, Input, Output, State
from plotly.subplots import make_subplots
import plotly.graph_objects as go

app = dash.Dash(__name__)
server = app.server


def make_sparkline(rows, cols):
	fig = make_subplots(
		rows,
		cols,
		horizontal_spacing=0.02,
		vertical_spacing=0.01,
	)
	for x in range(rows):
		for y in range(cols):
			trace = go.Scatter(
				x=list(range(100)),
				y=[random.random() for _ in range(100)],
				mode="lines",
				name="trendline",
				marker=dict(
					color="#000000",
				),
			)
			fig.add_trace(trace, x+1, y+1)

	# style the figure
	fig.update_layout(
		showlegend=False,
		plot_bgcolor="rgba(0,0,0,0)",
		paper_bgcolor="rgba(0,0,0,0)",
		margin=dict(
			t=10,
			b=10,
			l=10,
			r=10,
		)
	)
	fig.update_xaxes(
		visible=False,
	)
	fig.update_yaxes(
		visible=False,
	)
	return fig


sparkline_fig = make_sparkline(rows=20, cols=4)
layout = html.Div([
	html.H1("Sparklines in Plotly"),
	html.P(
		"We are looking at a figure factory that generates Sparklines using the Plotly ecosystem."
	),
	html.Div(
		className="",
		children=[
			dcc.Graph(
				id="sparkline",
				figure=sparkline_fig,
			)
		]
	)
])

app.layout = layout

if __name__ == "__main__":
	app.run_server(debug=True)
