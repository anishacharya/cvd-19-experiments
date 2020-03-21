import config as conf
import pandas as pd
import matplotlib.pyplot as plt


class CovidReader:
    def __init__(self, filename):
        self.filename = filename
        self.data = pd.read_csv(self.filename)

    def fetch_time_series(self, country: str = None, state: str = None):
        if country is None:
            raise Exception('specify either country (and region)')
        if country is not None:
            filtered_data = self.data.loc[self.data['Country/Region'] == country]
            if state is not None:
                return filtered_data.loc[self.data['Province/State'] == state]
            else:
                aggregate = filtered_data.sum(axis=0, skipna=True)[4:-1]
                return aggregate
        else:
            raise NotImplementedError


if __name__ == '__main__':
    covid_reader = CovidReader(filename=conf.confirmed_covid_jhu_time_series)
    time_series = covid_reader.fetch_time_series(country='US')

    time_series.plot(kind='bar')
    plt.ylabel('cumulative confirmed COVID-19 cases ')
    plt.xticks([])
    plt.show()
