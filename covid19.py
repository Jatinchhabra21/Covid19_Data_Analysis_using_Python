import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
corona_dataset_csv = pd.read_csv('Datasets/Covid19_Confirmed_dataset.csv')
corona_dataset_csv.head(10)
corona_dataset_csv.drop(['Lat','Long'],axis=1,inplace=True)
corona_dataset_aggregated = corona_dataset_csv.groupby('Country/Region').sum()
countries = list(corona_dataset_aggregated.index)
max_infection_rates = []
for country in countries:
    max_infection_rates.append(corona_dataset_aggregated.loc[country].diff().max())
corona_dataset_aggregated['max_infection_rate'] = max_infection_rates
corona_data = pd.DataFrame(corona_dataset_aggregated['max_infection_rate'])
happiness_report_csv = pd.read_csv('Datasets/worldwide_happiness_report.csv') 
useless_cols = ['Overall rank','Score','Generosity','Perceptions of corruption']
happiness_report_csv.drop(useless_cols,axis=1,inplace=True)
happiness_report_csv.set_index('Country or region',inplace=True)
data = corona_data.join(happiness_report_csv,how='inner')
x = data['GDP per capita']
y = data['max_infection_rate']
sns.regplot(x=x,y=np.log(y))
x = data['Social support']
y = data['max_infection_rate']
sns.regplot(x=x,y=np.log(y))
x = data['Healthy life expectancy']
y= data['max_infection_rate']
sns.regplot(x=x,y=np.log(y))
x = data['Freedom to make life choices']
y=data['max_infection_rate']
sns.regplot(x=x,y=np.log(y))

