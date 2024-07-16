import sys
import geojson
import argparse

def merge_geojson(files):
    print("Starte den Merge-Vorgang")
    merged_features = []
    for file in files:
        with open(file, 'r') as f:
            data = geojson.load(f)
            if 'features' in data:
                merged_features.extend(data['features'])
            else:
                print(f"Warnung: Datei {file} enthält keine Features.")
    merged_geojson = geojson.FeatureCollection(merged_features)
    return merged_geojson

def save_geojson(data, output_file):
    with open(output_file, 'w') as f:
        geojson.dump(data, f)
    print("Neue *.geojson Datei erfolgreich gemerged.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_files', nargs='+', help='Bitte die Pfade zur Input-Datei angeben.')
    parser.add_argument('-o', '--output_files', nargs=1, help='Bitte den Pfad zur Output-Datei angeben.')
    args = parser.parse_args()

    if args.input_files and args.output_files:
        input_files = args.input_files
        output_file = args.output_files[0]
        merged_data = merge_geojson(input_files)
        save_geojson(merged_data, output_file)
    else:
        print("Bitte Pfade zur Input/Output-Datei angeben.")
        sys.exit(-1)
