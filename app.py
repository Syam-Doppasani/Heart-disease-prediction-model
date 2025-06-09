import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("heart_model.pkl")
scaler = joblib.load("scaler.pkl")

# Page setup
st.set_page_config(layout="wide", page_title="❤️ Heart Health Guardian", page_icon="❤️")

# Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

:root {
    --primary: #ff4d4d;
    --secondary: #ff9999;
    --light-bg: #fff5f5;
    --dark-text: #2c3e50;
    --label-text: #333333;  /* Dark color for labels */
    --section-header: #2c3e50;  /* Dark color for section headers */
}

body {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #fff5f5 0%, #ffecec 100%);
}

.card {
    background: white;
    border-radius: 15px;
    padding: 1.5rem;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    margin-bottom: 1rem;
    border-left: 4px solid var(--primary);
}

/* Section headers - dark color */
.header {
    color: var(--section-header) !important;
    font-weight: 700;
    font-size: 1.5rem;
    margin-bottom: 1rem;
}

/* Label styling - dark colors */
label, .stNumberInput label, .stSelectbox label, .stTextInput label {
    color: var(--label-text) !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
}

/* Input values - white text on colored background */
.stNumberInput input, .stSelectbox select, .stTextInput input {
    color: white !important;
    font-weight: 500 !important;
    background-color: var(--primary) !important;
}

.stNumberInput input, .stSelectbox select {
    border: 1px solid #ffcccc !important;
    border-radius: 8px !important;
    padding: 8px 12px !important;
}

.stNumberInput>div>div>input, .stSelectbox>div>div>select {
    background-color: var(--primary) !important;
}

/* Dropdown options styling */
.stSelectbox div[data-baseweb="select"] > div > div {
    color: white !important;
    background-color: var(--primary) !important;
}

/* Dropdown menu items */
div[role="listbox"] div {
    color: var(--dark-text) !important;
    background-color: white !important;
}

div[role="listbox"] div:hover {
    background-color: #ffecec !important;
}

.stButton>button {
    background: linear-gradient(135deg, #ff4d4d 0%, #ff9999 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.5rem 1rem !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 6px rgba(255, 77, 77, 0.2) !important;
    transition: all 0.3s !important;
    width: 100% !important;
}

.stButton>button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 8px rgba(255, 77, 77, 0.3) !important;
}

.result-card {
    background: white;
    border-radius: 15px;
    padding: 2rem;
    margin: 1rem 0;
    text-align: center;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    border-top: 5px solid var(--primary);
    animation: fadeIn 0.5s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.healthy {
    color: #4CAF50;
    font-weight: 700;
}

.risk {
    color: var(--primary);
    font-weight: 700;
}

.tip {
    font-size: 0.9rem;
    color: #666;
    font-style: italic;
    margin-top: 0.5rem;
}

.app-header {
    text-align: center;
    margin-bottom: 2rem;
    padding: 1.5rem;
    background: linear-gradient(135deg, #ff4d4d 0%, #ff9999 100%);
    color: white;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(255, 77, 77, 0.3);
}

.app-header h1 {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
}

.app-header p {
    font-size: 1.1rem;
    opacity: 0.9;
}

/* Help text styling */
[data-testid="stHelp"] {
    color: #666 !important;
    font-size: 0.85rem !important;
}
</style>
""", unsafe_allow_html=True)

# App header
st.markdown("""
<div class="app-header">
    <h1>❤️ Heart Health Guardian</h1>
    <p>Assess your heart disease risk with our AI-powered screening tool</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin-bottom: 2rem;">
    <p style="color: #666;">Complete the form below to receive your personalized heart health assessment. 
    All information is kept confidential and used solely for prediction purposes.</p>
</div>
""", unsafe_allow_html=True)

# Input Form in Cards
with st.container():
    col1, col2, col3 = st.columns([1,1,1], gap="large")
    
    with col1:
        st.markdown("<div class='card'><h3 class='header'>Personal Information</h3>", unsafe_allow_html=True)
        age = st.number_input("Age (years)", min_value=18, max_value=120, value=45, step=1, 
                            help="Enter your current age")
        sex = st.selectbox("Gender", ["Female", "Male"], 
                         help="Biological sex is an important factor in heart health")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='card'><h3 class='header'>Blood Metrics</h3>", unsafe_allow_html=True)
        resting_bp = st.number_input("Resting Blood Pressure (mmHg)", min_value=80, max_value=200, value=120, step=1,
                                   help="Measured at rest, in millimeters of mercury")
        cholesterol = st.number_input("Cholesterol Level (mg/dL)", min_value=100, max_value=600, value=200, step=1,
                                    help="Your total serum cholesterol level")
        fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", ["No", "Yes"],
                                help="High fasting blood sugar indicates diabetes risk")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='card'><h3 class='header'>Heart Activity</h3>", unsafe_allow_html=True)
        max_hr = st.number_input("Maximum Heart Rate (bpm)", min_value=60, max_value=220, value=150, step=1,
                               help="Highest heart rate achieved during exercise")
        resting_ecg = st.selectbox("Resting ECG Results", 
                                  ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"],
                                  help="Results from your last electrocardiogram")
        st_slope = st.selectbox("ST Segment Slope", 
                               ["Upward", "Flat", "Downward"],
                               help="Slope of ST segment during peak exercise")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='card'><h3 class='header'>Exercise Factors</h3>", unsafe_allow_html=True)
        exercise_angina = st.selectbox("Exercise-Induced Chest Pain", ["No", "Yes"],
                                      help="Chest pain during physical activity")
        oldpeak = st.number_input("Old peak", min_value=0.0, max_value=10.0, value=1.0, step=0.1,
                                help="ST segment depression induced by exercise relative to rest")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div class='card'><h3 class='header'>Symptoms</h3>", unsafe_allow_html=True)
        chest_pain = st.selectbox("Chest Pain Type", 
                                ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"],
                                help="Description of any chest pain experienced")
        
        # Heart illustration
        st.markdown("""
        <div style="text-align: center; margin: 1.5rem 0;">
            <svg width="120" height="120" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 21.35L10.55 20.03C5.4 15.36 2 12.28 2 8.5C2 5.42 4.42 3 7.5 3C9.24 3 10.91 3.81 12 5.09C13.09 3.81 14.76 3 16.5 3C19.58 3 22 5.42 22 8.5C22 12.28 18.6 15.36 13.45 20.03L12 21.35Z" fill="#ff4d4d"/>
            </svg>
            <p style="color: #666; font-size: 0.9rem;">Your heart health matters</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Prediction button
        if st.button("🔍 Analyze My Heart Health", use_container_width=True):
            # Convert inputs to model format
            sex_num = 1 if sex == "Male" else 0
            chest_pain_num = ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"].index(chest_pain) + 1
            fasting_bs_num = 1 if fasting_bs == "Yes" else 0
            resting_ecg_num = ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"].index(resting_ecg)
            exercise_angina_num = 1 if exercise_angina == "Yes" else 0
            st_slope_num = ["Upward", "Flat", "Downward"].index(st_slope) + 1
            
            input_data = np.array([[
                age,
                sex_num,
                chest_pain_num,
                resting_bp,
                cholesterol,
                fasting_bs_num,
                resting_ecg_num,
                max_hr,
                exercise_angina_num,
                oldpeak,
                st_slope_num
            ]])
            
            input_scaled = scaler.transform(input_data)
            prediction = model.predict(input_scaled)[0]
            
            # Show result
            with st.container():
                if prediction == 1:
                    st.markdown(f"""
                    <div class='result-card'>
                        <h2 style="color: #ff4d4d;">⚠️ Potential Risk Detected</h2>
                        <p>Our analysis indicates <span class='risk'>possible signs of heart disease</span> based on your inputs.</p>
                        <p class='tip'>This doesn't replace professional medical advice. We recommend consulting a cardiologist for a comprehensive evaluation.</p>
                        <p>❤️ Your heart matters - take action today.</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class='result-card'>
                        <h2 style="color: #4CAF50;">✅ Healthy Heart Indicators</h2>
                        <p>Our analysis shows <span class='healthy'>no significant signs of heart disease</span> based on your inputs.</p>
                        <p class='tip'>Continue maintaining a heart-healthy lifestyle with regular exercise and balanced nutrition.</p>
                        <p>❤️ Keep up the good work!</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Additional resources
            with st.expander("💡 Heart Health Tips"):
                st.markdown("""
                - **Eat heart-healthy foods**: Focus on fruits, vegetables, whole grains, and lean proteins
                - **Stay active**: Aim for at least 150 minutes of moderate exercise per week
                - **Manage stress**: Practice relaxation techniques like meditation or deep breathing
                - **Regular check-ups**: Visit your doctor for annual physicals and screenings
                - **Avoid smoking**: Smoking significantly increases heart disease risk
                
                *Remember: This tool provides estimates, not medical diagnoses. Always consult with healthcare professionals.*
                """)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 3rem; color: #888; font-size: 0.8rem;">
    <hr style="border: 0.5px solid #ffcccc;">
    <p>❤️ Heart Health Guardian | This tool is for informational purposes only | Not a substitute for professional medical advice</p>
</div>
""", unsafe_allow_html=True)
