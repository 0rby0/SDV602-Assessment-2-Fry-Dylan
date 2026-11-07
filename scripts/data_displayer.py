# Takes in a set of data and generates a graph from it
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from operator import itemgetter
from data_config import DataConfig

class DataDisplay:
	def __init__(self):
		self.data_conf = DataConfig(None)

	def generate_chart_line(self):
		"""Creates a line chart from the given settings."""
		try:
			if not self.data_conf.data:
				return None

			series = {}
			for row in self.data_conf.data:
					series.setdefault(row.get(self.data_conf.series_key), []).append(row)

			plt.figure(figsize=(8, 6))

			for name, rows in series.items():
					rows.sort(key=itemgetter(self.data_conf.x_key))

					x_values = []
					y_values = []

					for row in rows:
						x_values.append(row[self.data_conf.x_key])
						y_values.append(float(row[self.data_conf.y_key]))

					plt.plot(x_values, y_values, marker='o', label=name)

			if self.data_conf.series_key:
				plt.legend()

			plt.xlabel(self.data_conf.x_key)
			plt.ylabel(self.data_conf.y_key)
			plt.title(self.data_conf.data_name)

			fig = plt.gcf()

			return fig  

		except:
			return None


	def generate_chart_pie(self):
		"""Creates a pie chart from the given settings."""
		try:
			if not self.data_conf.data:
				return None

			values = [] # y_key
			labels = [] # x_key

			fig, ax = plt.subplots(figsize=(8, 6))

			for row in self.data_conf.data:
				if row[self.data_conf.series_key] == self.data_conf.get_series:
					values.append(int(row[self.data_conf.y_key]))
					labels.append(row[self.data_conf.x_key])

			ax.pie(values, labels=labels, autopct='%1.0f%%')
			return fig

		except:
			return None


	def generate_chart_bar(self):
		"""Creates a bar chart from the given settings."""
		try:
			if not self.data_conf.data:
				return None

			x = []
			y = {}

			fig, ax = plt.subplots(figsize=(8, 6))

			for row in self.data_conf.data:
				if row[self.data_conf.x_key] not in x:
					x.append(row[self.data_conf.x_key])

				if row[self.data_conf.series_key] in y:
					y[row[self.data_conf.series_key]].append(int(row[self.data_conf.y_key]))
				else:
					y[row[self.data_conf.series_key]] = [int(row[self.data_conf.y_key])]

			ax.grouped_bar(y, tick_labels=x)
			ax.legend()
			return fig
   
		except:
			return None