def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    res = []
    with open(csv_file_path) as f:
        for line in f:
            line = line.rstrip()
            line = line.split(",")
            line = [int(x) if x.isdigit() else x.strip("\"") for x in line ]
            res.append(line)
    return res
#
# if __name__ == '__main__':
#     path = "/Users/macbook/Downloads/college/GRAD/CS506/git_learn/CS506-Fall2020/02-library/tests/test_files/dataset_2.csv"
#     read_csv(path)