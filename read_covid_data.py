import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


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
                cumulative_cases = filtered_data.loc[self.data['Province/State'] == state]
            else:
                cumulative_cases = filtered_data.sum(axis=0, skipna=True)[4:-1]

            new_cases = cumulative_cases.diff(1)
            new_cases[0] = cumulative_cases[0]
            return cumulative_cases, new_cases
        else:
            raise NotImplementedError

    def plot_country_trend(self, country, kind='bar'):
        cumulative_cases, new_cases = self.fetch_time_series(country=country)

        max_val = cumulative_cases.max()
        cumulative_cases.index = list(range(0, len(cumulative_cases)))

        cumulative_cases.plot(kind=kind)

        plt.grid(True, linestyle='-', axis='y')
        plt.xticks(ticks=cumulative_cases.index, labels=[])
        plt.yticks(ticks=np.arange(0, 1.5 * max_val, step=int((1.5 * max_val)/10)))
        plt.ylabel('cumulative confirmed COVID-19 cases ')
        plt.xlabel('days since first 01/22/2020')
        plt.show()



