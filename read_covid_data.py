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

    def plot_country_trend(self, country, aggregation_type, plot_kind):
        cumulative_cases, new_cases = self.fetch_time_series(country=country)

        if aggregation_type == 'cum':
            plotted_cases = cumulative_cases
            plt.ylabel('cumulative confirmed COVID-19 cases ')
        elif aggregation_type == 'new':
            plotted_cases = new_cases
            plt.ylabel('new confirmed COVID-19 cases ')
        else:
            raise NotImplementedError

        max_val = plotted_cases.max()
        plotted_cases.index = list(range(0, len(plotted_cases)))
        plotted_cases.plot(kind=plot_kind)
        plt.grid(True, linestyle='-', axis='both')
        plt.xticks(ticks=np.arange(0, len(plotted_cases), step=7))
        plt.yticks(ticks=np.arange(0, 1.5 * max_val, step=int((1.5 * max_val)/10)))

        plt.xlabel('Weeks since first case (01/22/2020) ')
        plt.show()



