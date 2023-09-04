import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['bmi'] = df['weight'] / ((df['height'] / 100)**2)
df['overweight'] = np.where(df['bmi'] > 25, 1, 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

#Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's catplot(). The dataset should be split by 'Cardio' so there is one chart for each cardio value. The chart should look like examples/Figure_1.png.

categorical_columns = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']

df_long = pd.melt(df, id_vars=['cardio'], value_vars=categorical_columns, var_name='variable', value_name='value')

g = sns.catplot(x='variable', hue='value', data=df_long, kind='count', col='cardio', aspect=1.2, height=4)

g.set_axis_labels('Categorical Features', 'Count')
g.set_titles('Cardio={col_name}')

plt.show()

#Clean the data. Filter out the following patient segments that represent incorrect data:
#diastolic pressure is higher than systolic
#height is less than the 2.5th percentile
#height is more than the 97.5th percentile
#weight is less than the 2.5th percentile
#eight is more than the 97.5th percentile

df_cleaned = df[
    (df['ap_lo'] <= df['ap_hi']) &  
    (df['height'] >= df['height'].quantile(0.025)) &  
    (df['height'] <= df['height'].quantile(0.975)) &  
    (df['weight'] >= df['weight'].quantile(0.025)) &  
    (df['weight'] <= df['weight'].quantile(0.975))  
]


print(df_cleaned)

#Create a correlation matrix using the dataset. Plot the correlation matrix using seaborn's heatmap()

def draw_heat_map():

    corr = df_cleaned.corr()
    
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    fig, ax = plt.subplots(figsize=(12, 10))

    ax = sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', linewidths=.3)
    
    fig.savefig('heatmap.png')

draw_heat_map()
