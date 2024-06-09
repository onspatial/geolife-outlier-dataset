import pol.conventions as conventions
import pol.utils as utils
import pandas


def get_outlier_map(outlier_dict, outlier_type):
    for key in conventions.outlier_level_map:
        if outlier_dict[key] is None:
            print('No agents for', key)
            outlier_dict[key] = []
    if outlier_type not in conventions.outlier_type_map:
        print('Invalid outlier type', outlier_type)
        exit(1)
    map = {}
    for key in outlier_dict:
        for agent in outlier_dict[key]:
            map[agent] = conventions.outlier_level_map[key] + \
                conventions.outlier_type_map[outlier_type]*10
    return map


def get_outlier_label(map, agent):
    if agent in map:
        return map[agent]
    else:
        return conventions.outlier_type_map["NO"]


def split_dataset(data_path, after):
    data = pandas.read_csv(data_path, sep='\t')
    data['CheckinTime'] = pandas.to_datetime(data['CheckinTime'])
    start_date = data['CheckinTime'].min()
    outlier_date = start_date + pandas.Timedelta(days=after)
    train = data[data['CheckinTime'] < outlier_date]
    test = data[data['CheckinTime'] >= outlier_date]
    train_path = data_path.replace('.tsv', '-train.tsv')
    test_path = data_path.replace('.tsv', '-test.tsv')
    print("Saving train data to", train_path)
    print("Saving test data to", test_path)
    train.to_csv(train_path, sep='\t', index=False)
    test.to_csv(test_path, sep='\t', index=False)


def label_dataset(data_path, map):
    data = pandas.read_csv(data_path, sep='\t')
    data['label'] = data['UserId'].apply(
        lambda x: utils.get_outlier_label(map, x))
    new_path = data_path.replace('.tsv', '-labeled.tsv')
    print("Saving labeled data to", new_path)
    data.to_csv(new_path, sep='\t', index=False)
    return new_path
