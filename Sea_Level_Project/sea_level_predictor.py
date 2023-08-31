import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
      
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, label='CSIRO Adjusted Sea Level', color='blue')
      
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')
    plt.title('CSIRO Adjusted Sea Level Over Years')
      
    plt.legend()
    plt.show()

    # Create first line of best fit
    slope = linregress(x, y)[0]
    intercept = linregress(x, y)[1]
    
    def line_of_best_fit(x):
        return slope * x + intercept
    
    predicted_sea_level_2050 = line_of_best_fit(2050)
    extended_x = np.linspace(min(x), 2050, num=100)
    fit = line_of_best_fit(extended_x)
    
    
    plt.figure(figsize=(10, 6))
    plt.plot(extended_x, fit, label='Fit line of CSIRO Adjusted Sea Level', color='red', linestyle='--', linewidth=2)
    plt.scatter(x, y, label='CSIRO Adjusted Sea Level', color='blue', edgecolor='k')
    plt.plot(2050, predicted_sea_level_2050, 'go', label='Predicted 2050')
    plt.xlabel('Year')
    plt.ylabel('Sea Level Rise (mm)')
    plt.title('Sea Level Rise Prediction')
    plt.legend()
    plt.grid()
    plt.show()
    print(f"Predicted sea level rise in 2050: {predicted_sea_level_2050:.2f} mm")

    # Create second line of best fit
        
    recent_years = df[df['Year'] >= 2000]
    recent_x = recent_years['Year']
    recent_y = recent_years['CSIRO Adjusted Sea Level']
    
    
    slope_recent = linregress(recent_x, recent_y)[0]
    intercept_recent = linregress(recent_x, recent_y)[1]
    
    
    def line_of_best_fit_recent(x):
        return slope_recent * x + intercept_recent
    
    
    predicted_sea_level_2050_recent = line_of_best_fit_recent(2050)
    extended_x = np.linspace(2000, 2050, num=100)
    
    fit_recent = line_of_best_fit_recent(extended_x)
    plt.figure(figsize=(10, 6))
  
    # Add labels and title
    plt.plot(extended_x, fit_recent, label='Recent Fit line of CSIRO Adjusted Sea Level', color='red', linestyle='--', linewidth=2)
    plt.scatter(x, y, label='CSIRO Adjusted Sea Level', color='blue', edgecolor='k')
    plt.plot(2050, predicted_sea_level_2050_recent, 'go', label='Predicted 2050 (Recent)')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.xlim(2000, 2050)
    plt.grid()
    plt.show()
    print(f"Predicted sea level rise in 2050 (Recent Trend): {predicted_sea_level_2050_recent:.2f} inches")
  
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()