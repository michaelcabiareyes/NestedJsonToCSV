import pandas as pd
import json
import argparse

def json_to_csv(input_json_filepath, output_csv_filename):
	data = json.load(open(input_json_filepath, encoding="utf8"))
	data = pd.json_normalize(data)
	data.to_csv(output_csv_filename)
	return

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("input_file", type=str, help="JSON Filepath or Data to be parsed.")
	parser.add_argument("output_file", type=str, help="The filename of the output CSV file.")
	args = parser.parse_args()

	json_to_csv(args.input_file, args.output_file)
	return


if __name__ == "__main__":
	main()

