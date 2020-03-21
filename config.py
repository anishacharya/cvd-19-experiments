import os

curr_dir = os.path.dirname(__file__)
data_dir = curr_dir + '/../COVID-19/csse_covid_19_data/csse_covid_19_time_series/'

confirmed_covid_jhu_time_series = data_dir + 'time_series_19-covid-Confirmed.csv'
deaths_covid_jhu_time_series = data_dir + 'time_series_19-covid-Deaths.csv'
recovered_covid_jhu_time_series = data_dir + 'time_series_19-covid-Recovered.csv'
