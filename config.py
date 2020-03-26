import os

curr_dir = os.path.dirname(__file__)
data_dir = curr_dir + '/../COVID-19/csse_covid_19_data/csse_covid_19_time_series/'

confirmed_covid_jhu_time_series = data_dir + 'time_series_covid19_recovered_global.csv'
deaths_covid_jhu_time_series = data_dir + 'time_series_covid19_deaths_global.csv'
recovered_covid_jhu_time_series = data_dir + ' time_series_covid19_recovered_global.csv'
