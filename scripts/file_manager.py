# Loads data from files and manages them.
import os
import csv

class FileManager:
	def __init__(self):
		self.internal_db = []
		self.datasets = []


	def compile_dataset(self, dataset):
		"""Combines all data from the internal database which is linked to the given dataset."""
		if dataset not in self.datasets:
			return f"Invalid dataset: '{dataset}'"

		compiled_result = []

		compiled_name = ""
		present_files = 0

		for file in self.internal_db:
			if file["dataset"] == dataset:
				compiled_result.extend(file["data"])

				if compiled_name == "":
					compiled_name = file["filename"]
				else:
					present_files += 1

		if present_files > 0:
			compiled_name += f" + {present_files} other(s)"
	
		return {compiled_name: compiled_result}


	def load_data_source(self, filepath, dataset):
		"""Takes a path to a CSV file, reads its data and adds it to the internal database linked to the given dataset."""
		if dataset not in self.datasets:
			return "Invalid dataset"

		data = []
	
		try:
			with open(filepath) as File:
				filename = os.path.basename(filepath)

				if not filepath.endswith(".csv"):
					return "Invalid file type"

				reader = csv.DictReader(File)

				data = []
				for row in reader:
					data.append(row)

				data_packet = {"filename": filename, "dataset": dataset, "data": data}
				self.internal_db.append(data_packet)
				return "File loaded successfully"
   
		except:
			return "File not found "
 
 
	def create_dataset(self, dataset):
		"""Add a new dataset to the internal dataset list."""
		if dataset in self.datasets:
			return "Dataset already exists"

		self.datasets.append(dataset)
		return "Dataset created successfully"
 
 
	def remove_dataset(self, dataset):
		"""Remove a given dataset from the internal dataset list."""
		if dataset not in self.datasets:
			return "Dataset not found"

		self.internal_db = [file for file in self.internal_db if file["dataset"] != dataset]
		self.datasets.remove(dataset)

		return "Dataset removed successfully"
 
 
	def rename_dataset(self, dataset, new_name):
		"""Changes the given dataset to the new name in both the internal dataset list and each reference in the internal database."""
		if dataset not in self.datasets:
			return "Dataset not found"

		if new_name in self.datasets:
			return "Dataset already exists"

		self.datasets.remove(dataset)
		self.datasets.append(new_name)

		for datasource in self.internal_db:
			if datasource["dataset"] == dataset:
				datasource["dataset"] = new_name

		return "Dataset name updated successfully"
 
 
	def remove_data_source(self, filename, dataset):
		"""Removes a given file's data (e.g. file.csv), which is linked to the given dataset, from the internal database."""
		if dataset not in self.datasets:
			return "Dataset not found"
		
		for datasource in self.internal_db:
			if datasource["dataset"] == dataset and datasource["filename"] == filename:
				self.internal_db.remove(datasource)

		return "Datasource removed successfully"


	def get_data_sources(self, dataset):
		"""Return a list of the filenames under the given dataset."""
		if dataset not in self.datasets:
			return "Dataset not found"

		filenames = []

		for datasource in self.internal_db:
			if datasource["dataset"] == dataset:
				filenames.append(datasource["filename"])

		return filenames