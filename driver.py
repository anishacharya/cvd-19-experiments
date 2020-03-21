from read_covid_data import CovidReader
import argparse
import config as conf


def _parse_args():
    parser = argparse.ArgumentParser(description='read_covid_data.py')
    parser.add_argument('--c', type=str, default='US',
                        help='Pass Country name')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = _parse_args()
    print(args)
    covid_reader = CovidReader(filename=conf.confirmed_covid_jhu_time_series)
    covid_reader.plot_country_trend(country=args.c, kind='bar')
