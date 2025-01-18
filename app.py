import streamlit as st
import pickle
import pandas as pd
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page configuration
st.set_page_config(
    page_title="Life Expectancy Predictor",
    page_icon="🌍",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        height: 3rem;
    }
    .stSlider > div > div > div {
        background-color: #f0f2f6;
    }
    .st-emotion-cache-16idsys p {
        font-size: 1.1rem;
        margin-bottom: 1rem;
    }
    .prediction-box {
        padding: 1rem;
        border-radius: 10px;
        background-color: #f8f9fa;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    .metric-card {
        background-color: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: #1f77b4;
    }
    </style>
""", unsafe_allow_html=True)

# Load the saved model
model_filename = "models/life_expectancy_model.pkl"

if not os.path.exists(model_filename):
    st.error("⚠️ Model file not found. Please check the model location.", icon="🚫")
    st.stop()

with open(model_filename, "rb") as file:
    Linear_model = pickle.load(file)

def create_gauge_chart(value, title):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': title, 'font': {'size': 24}},
        gauge={
            'axis': {'range': [None, 100], 'tickwidth': 1},
            'bar': {'color': "#1f77b4"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 50], 'color': '#ffebee'},
                {'range': [50, 75], 'color': '#e3f2fd'},
                {'range': [75, 100], 'color': '#e8f5e9'}
            ]
        }
    ))
    
    fig.update_layout(
        height=200,
        margin=dict(l=10, r=10, t=40, b=10),
        paper_bgcolor="white",
    )
    return fig

def create_comparison_chart(predicted_value):
    # Sample global averages (you can replace these with actual data)
    global_data = {
        'Global Average': 72.0,
        'Developed Countries': 80.0,
        'Developing Countries': 65.0,
        'Prediction': predicted_value
    }
    
    fig = go.Figure(go.Bar(
        x=list(global_data.keys()),
        y=list(global_data.values()),
        marker_color=['#90caf9', '#81c784', '#ffb74d', '#1f77b4'],
        text=[f'{value:.1f}' for value in global_data.values()],
        textposition='auto',
    ))
    
    fig.update_layout(
        title="Life Expectancy Comparison",
        height=250,
        margin=dict(l=10, r=10, t=40, b=10),
        paper_bgcolor="white",
        plot_bgcolor="white",
        showlegend=False,
        yaxis_title="Years",
        xaxis_title=None
    )
    return fig

def main():
    # Header section
    st.markdown("""
        <h1 style='text-align: center; color: #1f77b4; margin-bottom: 2rem;'>
            🌍 Life Expectancy Regression
        </h1>
    """, unsafe_allow_html=True)

    # Create columns for layout
    col1, col2 = st.columns([2, 1])

    with col1:
        # Input tabs
        tabs = st.tabs(["🏥 Health Factors", "💰 Economic Factors", "🌎 Country & Status"])

        with tabs[0]:
            st.markdown("### Health Indicators")
            col_h1, col_h2 = st.columns(2)
            
            with col_h1:
                adult_mortality = st.slider(
                    "Adult Mortality Rate 🏥",
                    min_value=0.0, max_value=500.0, value=164.0,
                    help="Deaths per 1000 adult population"
                )
                alcohol = st.slider(
                    "Alcohol Consumption 🍷",
                    min_value=0.0, max_value=20.0, value=4.6,
                    help="Liters per capita per year"
                )
                hepatitis_b = st.slider(
                    "Hepatitis B Coverage 💉",
                    min_value=0.0, max_value=100.0, value=80.94,
                    help="Immunization coverage among 1-year-olds (%)"
                )

            with col_h2:
                hiv_aids = st.slider(
                    "HIV/AIDS Prevalence 🔬",
                    min_value=0.0, max_value=50.0, value=0.1,
                    help="Prevalence among adults aged 15-49 years"
                )
                bmi = st.slider(
                    "Average BMI 📊",
                    min_value=0.0, max_value=50.0, value=38.32,
                    help="Average Body Mass Index of the population"
                )

        with tabs[1]:
            st.markdown("### Economic Indicators")
            col_e1, col_e2 = st.columns(2)
            
            with col_e1:
                gdp = st.number_input(
                    "GDP per Capita 💰",
                    min_value=0.0, max_value=100000.0, value=7483.16,
                    help="Gross Domestic Product per capita in USD",
                    format="%.2f"
                )
                schooling = st.slider(
                    "Years of Schooling 📚",
                    min_value=0.0, max_value=20.0, value=11.99,
                    help="Average years of education received"
                )

            with col_e2:
                total_expenditure = st.slider(
                    "Healthcare Expenditure 🏥",
                    min_value=0.0, max_value=100.0, value=5.94,
                    help="Percentage of GDP spent on healthcare"
                )

        with tabs[2]:
            st.markdown("### Geographic Information")
            country = st.selectbox(
                "Select Country 🌍",
                ["Afghanistan", "Albania", "Algeria", "Angola", "Argentina", "Australia", "Zimbabwe"],
                help="Choose the country for prediction"
            )
            developed_status = st.selectbox(
                "Development Status 📈",
                ["Developed", "Developing"],
                help="Select the country's development status"
            )

    with col2:
        # Prediction section with improved styling
        st.markdown("""
            <div class='prediction-box'>
                <h3 style='text-align: center; color: #1f77b4; margin-bottom: 1rem;'>Prediction Analysis</h3>
            </div>
        """, unsafe_allow_html=True)
        
        # Create prediction DataFrame
        user_input = pd.DataFrame({
            'Year': [2023],
            'Adult Mortality': [adult_mortality],
            'Alcohol': [alcohol],
            'Hepatitis B': [hepatitis_b],
            'BMI': [bmi],
            'HIV/AIDS': [hiv_aids],
            'GDP': [gdp],
            'Total expenditure': [total_expenditure],
            'Schooling': [schooling],
            country: [1],
            developed_status: [1]
        })

        # Add missing columns and make prediction
        for feature in Linear_model.feature_names_in_:
            if feature not in user_input.columns:
                user_input[feature] = 0
        user_input = user_input[Linear_model.feature_names_in_]

        try:
            prediction = Linear_model.predict(user_input)[0]
            
            # Display prediction in a compact card
            st.markdown("""
                <div class='metric-card'>
                    <h4 style='margin: 0; color: #666;'>Predicted Life Expectancy</h4>
                    <div class='metric-value'>{:.1f} years</div>
                </div>
            """.format(prediction), unsafe_allow_html=True)

            # Add gauge chart
            health_index = min(100, max(0, (prediction - 50) * 2))  # Convert life expectancy to 0-100 scale
            gauge_fig = create_gauge_chart(health_index, "Health Index")
            st.plotly_chart(gauge_fig, use_container_width=True)

            # Add comparison chart
            comparison_fig = create_comparison_chart(prediction)
            st.plotly_chart(comparison_fig, use_container_width=True)

            # Add key insights
            st.markdown("""
                <div style='background-color: #e3f2fd; padding: 1rem; border-radius: 8px; margin-top: 1rem;'>
                    <h4 style='margin: 0; color: #1976d2;'>Key Insights</h4>
                    <ul style='margin: 0.5rem 0 0 0; padding-left: 1.2rem;'>
                        <li>Above/below global average by {:.1f} years</li>
                        <li>Comparable to {}</li>
                        <li>Key factors: GDP, Healthcare access</li>
                    </ul>
                </div>
            """.format(
                prediction - 72.0,
                "developed nations" if prediction > 75 else "developing nations"
            ), unsafe_allow_html=True)

        except Exception as e:
            st.error(f"⚠️ Prediction Error: {str(e)}", icon="🚫")

if __name__ == "__main__":
    main()