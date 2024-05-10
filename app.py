# type: ignore
import numpy as np 
import pandas as pd 
from scipy import stats 
import streamlit as st 
from plots import (
    general_histograms,
    generate_correlation_heatmap,
    unemployment_rate_across_different_states,
    income_rate_across_the_states,
    total_pop_per_state,
    men_population_per_state,
    women_popualtion_per_state,
    Black_popualtion_per_state,
    Pacific_popualtion_per_state,
    White_popualtion_per_state,
    Hispanic_popualtion_per_state,
    Asian_popualtion_per_state,
    Native_popualtion_per_state
)

st.set_page_config(page_title="Demographic Dashboard", page_icon=":bar_chart:", layout="wide")


@st.cache_data
def load_data():
    # Load the data using pandas
    df = pd.read_csv('Us_data.csv')
    df.dropna(inplace=True)
    return df

df = load_data()

# Sidebar for display options
display_option = st.sidebar.radio(
    "Display Option",
    (
        "Dataframe",
        "Plot",
        "Correlation Heatmap",
        "Unemployment Rate across different states",
        "Income Rate across the states",
        "Total population across different states",
        "Total Men Population across the states",
        "Total Women Population across the states",
        "Total Black Population across the states",
        "Total Pacific popualtion per state",
        "Total White Population across the states",
        "Total Hispanic Population across the states",
        "Total Asian Population across the states",
        "Total Native Population across the states"

        
    )
)


# Display the selected option
if display_option == "Dataframe":
    st.dataframe(df)
elif display_option == "Plot":
    for fig in general_histograms(df):
        st.pyplot(fig)  # Display the histogram in Streamlit app
elif display_option == "Correlation Heatmap":
    plt = generate_correlation_heatmap(df) 
    st.pyplot(plt)  # Display the correlation heatmap in Streamlit app

elif display_option=="Unemployment Rate across different states":
    plt=unemployment_rate_across_different_states(df)
    st.pyplot(plt) 

elif display_option=="Income Rate across the states":
    plt=income_rate_across_the_states(df)
    st.pyplot(plt) 

elif display_option=="Total population across different states":
    plt=total_pop_per_state(df)
    st.pyplot(plt) 

elif display_option=="Total Men Population across the states":
    plt= men_population_per_state(df)
    st.pyplot(plt) 

elif display_option=="Total Women Population across the states":
    plt= women_popualtion_per_state(df)
    st.pyplot(plt) 

elif display_option=="Total Black Population across the states":
    plt= Black_popualtion_per_state(df)
    st.pyplot(plt) 

elif display_option=="Total White Population across the states":
    plt= White_popualtion_per_state(df)
    st.pyplot(plt)

elif display_option=="Total Native Population across the states":
    plt= Native_popualtion_per_state(df)
    st.pyplot(plt)  

elif display_option=="Total Asian Population across the states":
    plt= Asian_popualtion_per_state(df)
    st.pyplot(plt) 

elif display_option=="Total Pacific Population across the states":
    plt= Pacific_popualtion_per_state(df)
    st.pyplot(plt) 

elif display_option=="Total Hispanic Population across the states":
    plt= Hispanic_popualtion_per_state(df)
    st.pyplot(plt) 



# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/KeerthiReddyyyy/DemographicApp.git
# git push -u origin main

