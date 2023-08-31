import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
  
    # [QUESTION 1] How many of each race are represented in this dataset? This should be a Pandas series           with race names as the index labels.
    race_count = df['race'].value_counts()

    # [QUESTION 2] What is the average age of men?
    average_age_men = df['age'].mean()

    # [QUESTION 3] What is the percentage of people who have a Bachelor's degree?
    #Count occurrences of each unique education level
    education_counts = df['education'].value_counts()

    #Calculate the percentage of people with a Bachelor's degree
    total_people = len(df)
    bachelors_count = education_counts.get("Bachelors", 0)  # Get count for 'Bachelors', default to 0 if not     found
    percentage_bachelors = (bachelors_count / total_people) * 100

    # [QUESTION 4]What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`)     make more than 50K?
  
    # [QUESTION 5] What percentage of people without advanced education make more than 50K?
    # List of advanced education levels
    higher_education_degrees = ['Bachelors', 'Masters', 'Doctorate']

    # Create DataFrames for higher and lower education individuals
    higher_education = df[df['education'].isin(higher_education_degrees)]
    lower_education = df[~df['education'].isin(higher_education_degrees)]

    # Calculate the percentage of people with higher education making more than 50K
    num_higher_edu_above_50K = higher_education[higher_education['salary'] == '>50K'].shape[0]
    total_higher_edu = higher_education.shape[0]
    percentage_higher_edu_above_50K = (num_higher_edu_above_50K / total_higher_edu) * 100

    # Calculate the percentage of people with lower education making more than 50K
    num_lower_edu_above_50K = lower_education[lower_education['salary'] == '>50K'].shape[0]
    total_lower_edu = lower_education.shape[0]
    percentage_lower_edu_above_50K = (num_lower_edu_above_50K / total_lower_edu) * 100

    # Display the percentages
    print("Percentage of people with higher education making more than 50K:",         percentage_higher_edu_above_50K)
    print("Percentage of people with lower education making more than 50K:", percentage_lower_edu_above_50K)

    # [QUESTION 6] with and without `Bachelors`, `Masters`, or `Doctorate`

    # Step 1: Count occurrences of each unique education level
    education_counts = df['education'].value_counts()
    
    # Step 2: Calculate the total number of individuals with higher education degrees
    higher_education_degrees = ['Bachelors', 'Masters', 'Doctorate']
    total_higher_education = education_counts[higher_education_degrees].sum()
    
    # Step 3: Calculate the percentage of individuals with and without higher education degrees
    total_individuals = len(df)
    higher_education = (total_higher_education / total_individuals) * 100
    lower_education = 100 - higher_education
   
    # [QUESTION 7] percentage with salary >50K
    # List of advanced education levels
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    
    # Create DataFrames for higher and lower education individuals with high salary
    higher_education_r = df[(df['education'].isin(advanced_education)) & (df['salary'] == '>50K')]
    lower_education_r = df[~df['education'].isin(advanced_education) & (df['salary'] == '>50K')]
    
    # Calculate the percentage of people with higher education and high salary
    higher_education_rich = (higher_education_r.shape[0] / df.shape[0]) * 100
    
    # Calculate the percentage of people with lower education and high salary
    lower_education_rich = (lower_education_r.shape[0] / df.shape[0]) * 100
    


    # [QUESTION 8] What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # [QUESTION 9] What percentage of the people who work the minimum number of hours per week have a salary     of >50K?

    #[QUESTION 10] Find the minimum number of hours worked per week
    min_hours_per_week = df['hours-per-week'].min()
    
    #Filter the data for rows with the minimum hours worked per week
    min_hours_workers = df[df['hours-per-week'] == min_hours_per_week]
    
    #Calculate the percentage of people with salary >$50,000
    total_min_workers = len(min_hours_workers)
    num_min_workers = min_hours_workers[min_hours_workers['salary'] == '>50K']
    rich_percentage = (len(num_min_workers) / total_min_workers) * 100
    
    # [QUESTION 11] What country has the highest percentage of people that earn >50K?
    #Filter the data for rows with salary > 50k
    high_earning_data = df[df['salary'] == '>50K']
    
    #Calculate the percentage for each country
    country_percentage = high_earning_data['native-country'].value_counts(normalize=True) * 100
    
    #Identify the country with the highest percentage
    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = country_percentage.max()

    # Identify the most popular occupation for those who earn >50K in India.

    #Filter data for rows with salary > $50,000 and native country is India
    high_earning_IN_data = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    
    # Count occurrences of each occupation
    top_IN_occupation = high_earning_IN_data['occupation'].value_counts().idxmax()


    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
