#!/usr/bin/env python
# coding: utf-8

import click
import logging
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import plotly.graph_objects as go
import seaborn as sns

from datetime import datetime

@click.command()
@click.option('--input',
			default='measurements.csv',
			help='Input filename of the csv. (default=measurements.csv)')
@click.option('--output',
			default="fig-{}.png".format(datetime.now().strftime('%d_%m_%Y_%H_%M_%S')),
			help='Output filename.')
@click.option('--resolution',
			default=5,
			help='Quality of the resulting png. (default=5)')
def csv_to_png(input, output, resolution):
	## Read csv from file and clean it
	df = pd.read_csv(r'measurements.csv')
	df = df.iloc[:1].transpose()
	df = df.rename(columns={0: "Weight"})
	df = df.rename_axis("Date", axis="columns")
	df.index = pd.DatetimeIndex(data=df.index, dayfirst=True)
	click.echo("Successfully read csv.")

	## Plot figure
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=df.index, y=df["Weight"],
	                    mode='lines+markers',
	                    name='lines+markers'))
	# fig.add_trace(go.Scatter(x=df.index, y=df["Weight"],
	#                     mode='markers',
	#                     name='markers',))

	fig.show()

	## Saving figure
	fig.write_image(output, scale=5)
	click.echo("Image saved as {}".format(output))

# Save image to file
if __name__ == "__main__":
	try:
		csv_to_png()
	except Exception as e:
		click.echo(e)





