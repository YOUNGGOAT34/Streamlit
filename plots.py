# type: ignore
import matplotlib.pyplot as plt 
import seaborn as sns



# Univariate analysis for numerical variables
numerical_variables = ['TotalPop', 'Men', 'Women', 'Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific', 'Unemployment', 'Income']

def general_histograms(df):

    # Plot histograms for numerical variables
    for var in numerical_variables:
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.histplot(df[var], bins=20, kde=True, ax=ax)
        ax.set_title(f'Histogram of {var}')
        ax.set_xlabel(var)
        ax.set_ylabel('Frequency')
        plt.close(fig)  # Close the figure to prevent multiple plots from being displayed
        yield fig  # Yield the figure to be displayed in Streamlit app


def generate_correlation_heatmap(df):
    # Calculate correlation matrix
    correlation_matrix = df[numerical_variables].corr()
    # Plot heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Matrix')
    # plt.close()  # Close the figure to prevent it from being displayed immediately
    return plt  # Return the plot to be displayed in Streamlit app

def unemployment_rate_across_different_states(df):
    # Calculate average unemployment rate for each state
    average_unemployment_by_state = df.groupby('State')['Unemployment'].mean().reset_index()

    # Bar plot of average unemployment rate across different states
    plt.figure(figsize=(10, 12)) 
    sns.barplot(data=average_unemployment_by_state, x='Unemployment', y='State', palette='viridis')
    plt.title('Average Unemployment Rate Across Different States')
    plt.xlabel('Average Unemployment Rate')
    plt.ylabel('State')
    return plt

def income_rate_across_the_states(df):
    # Calculate average unemployment rate for each state
    average_Income_by_state = df.groupby('State')['Income'].mean().reset_index()

    # Bar plot of average unemployment rate across different states
    plt.figure(figsize=(10, 12))  
    sns.barplot(data=average_Income_by_state, x='Income', y='State', palette='viridis')
    plt.title('Average Income Rate Across Different States')
    plt.xlabel('Average Income Rate')
    plt.ylabel('State')
    return plt

def total_pop_per_state(df):#pop for population
    # Calculate total population for each state
    total_population_by_state = df.groupby('State')['TotalPop'].sum().reset_index()

    # Bar plot of total population across different states
    plt.figure(figsize=(10, 12)) 
    sns.barplot(data=total_population_by_state, x='TotalPop', y='State', palette='viridis')
    plt.title('Total Population Across Different States')
    plt.xlabel('Total Population')
    plt.ylabel('State')
    return plt

def men_population_per_state(df):
    # Calculate total male population for each state
    total_Men_by_state = df.groupby('State')['Men'].sum().reset_index()

    # Bar plot of total population across different states
    plt.figure(figsize=(10, 12)) 
    sns.barplot(data=total_Men_by_state, x='Men', y='State', palette='viridis')
    plt.title('Total Men Population Across Different States')
    plt.xlabel('Total Men Population')
    plt.ylabel('State')
    return plt

def women_popualtion_per_state(df):
    # Calculate total population for each state
    total_Women_by_state = df.groupby('State')['Women'].sum().reset_index()
    # Bar plot of total female population across different states
    plt.figure(figsize=(10, 12)) 
    sns.barplot(data=total_Women_by_state, x='Women', y='State', palette='viridis')
    plt.title('Total Women Population Across Different States')
    plt.xlabel('Total Women Population')
    plt.ylabel('State')
    return plt

def Black_popualtion_per_state(df):
    # Calculate total black population for each state
    total_Black_pop_by_state = df.groupby('State')['Black'].sum().reset_index()
    # Bar plot of total Black population across different states
    plt.figure(figsize=(10, 12))  
    sns.barplot(data=total_Black_pop_by_state , x='Black', y='State', palette='viridis')
    plt.title('Total Black Population Across Different States')
    plt.xlabel('Total Black Population')
    plt.ylabel('State')
    return plt

def White_popualtion_per_state(df):
    # Calculate total white race population for each state
    total_White_pop_by_state = df.groupby('State')['White'].sum().reset_index()
    # Bar plot of total population across different states
    plt.figure(figsize=(10, 12))  
    sns.barplot(data=total_White_pop_by_state , x='White', y='State', palette='viridis')
    plt.title('Total White Population Across Different States')
    plt.xlabel('Total White Population')
    plt.ylabel('State')
    return plt

def Hispanic_popualtion_per_state(df):
    # Calculate total Hispanic race population for each state
    total_Hispanic_pop_by_state = df.groupby('State')['Hispanic'].sum().reset_index()
    # Bar plot of total population across different states
    plt.figure(figsize=(10, 12))  
    sns.barplot(data=total_Hispanic_pop_by_state, x='Hispanic', y='State', palette='viridis')
    plt.title('Total Hispanic Population Across Different States')
    plt.xlabel('Total Hispanic Population')
    plt.ylabel('State')
    return plt

def Asian_popualtion_per_state(df):
    # Calculate total Asian race population for each state
    total_Asian_pop_by_state = df.groupby('State')['Asian'].sum().reset_index()
    # Bar plot of total population across different states
    plt.figure(figsize=(10, 12))  
    sns.barplot(data=total_Asian_pop_by_state, x='Asian', y='State', palette='viridis')
    plt.title('Total Asian Population Across Different States')
    plt.xlabel('Total Asian Population')
    plt.ylabel('State')
    return plt

def Native_popualtion_per_state(df):
    # Calculate total Native race population for each state
    total_Native_pop_by_state = df.groupby('State')['Native'].sum().reset_index()
    # Bar plot of total population across different states
    plt.figure(figsize=(10, 12))  
    sns.barplot(data=total_Native_pop_by_state, x='Native', y='State', palette='viridis')
    plt.title('Total Native Population Across Different States')
    plt.xlabel('Total Native Population')
    plt.ylabel('State')
    return plt

def Pacific_popualtion_per_state(df):
    # Calculate total Hispanic race population for each state
    total_Pacific_pop_by_state = df.groupby('State')['Pacific'].sum().reset_index()
    # Bar plot of total population across different states
    plt.figure(figsize=(10, 12))  
    sns.barplot(data=total_Pacific_pop_by_state, x='Pacific', y='State', palette='viridis')
    plt.title('Total Pacific Population Across Different States')
    plt.xlabel('Total Pcific Population')
    plt.ylabel('State')
    return plt







