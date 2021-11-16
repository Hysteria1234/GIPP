import csv
from pathlib import Path


def read_csv(file):
    out_dict = {}
    with open(Path(f"./{file}"), "r", encoding="utf-8", newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader)  # Skipping header row
        for row in reader:
            out_dict[row[0]] = row[1]
    return out_dict


def main():
    business_dict = read_csv("../res/ABI_business_codes.csv")
    occupation_dict = read_csv("../res/ABI_occupation_codes.csv")
    print(business_dict["201"])
    print(occupation_dict["T01"])


if __name__ == "__main__":
    main()
