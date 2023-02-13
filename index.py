import random

import dash
from dash import dcc, html, Input, Output, State
from plotly.subplots import make_subplots
import plotly.graph_objects as go

app = dash.Dash(__name__)
server = app.server


VALID_COLUMN_CHART_TYPES = [
	"scatter",
	"bar",
	"text",
	"number",
]

def make_sparkline(rows, cols, column_chart_types=None, column_names=None):
	"""Generate a Sparklines in Plotly."""

	if not column_chart_types:
		column_chart_types = ["scatter"] * cols

	# validate the parameters
	if len(column_chart_types) != cols:
		raise Exception("The length of `column_chart_types` must equal the value of `cols`.")

	fig = make_subplots(
		rows,
		cols,
		horizontal_spacing=0.02,
		vertical_spacing=0.01,
		subplot_titles=None if not column_names else column_names + [] * (rows*(cols-1))
	)
	is_first_row = True
	for x in range(rows):
		for y in range(cols):
			trace_type = column_chart_types[y]
			if trace_type.lower() == "scatter":
				trace = go.Scatter(
					x=list(range(100)),
					y=[random.random() for _ in range(100)],
					mode="lines",
					name="trendline",
					marker=dict(
						color="#000000",
					),
					line=dict(
						width=1,
					)
				)
			elif trace_type.lower() == "bar":
				trace = go.Bar(
					x=[letter for letter in "ABCDEFG"],
					y=[random.random() * 10 for _ in "ABCDEFG"],
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
			t=25,
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

sparkline_fig = make_sparkline(
	rows=15,
	cols=5,
	column_chart_types=["scatter", "bar", "scatter", "scatter", "bar"],
	column_names=["Column 1", "Column 2", "Column 3", "Column 4", "Column 5"],
)


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
