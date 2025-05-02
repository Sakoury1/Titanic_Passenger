import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

with open("Model_ClasS1.pkl", "rb") as file:
    model = pickle.load(file)

with open("ScaleR_0.pkl", "rb") as file:
    scaler_data = pickle.load(file)

scaler = scaler_data["scaler"]
scaler_columns = scaler_data["columns"]


st.header("🚢 Titanic Survival Prediction")

pclass = st.selectbox("Passenger Class", [1, 2, 3])
age = st.number_input("Age", min_value=1, max_value=100, value=30)
sibsp = st.number_input("Siblings/Spouses Aboard", min_value=0, max_value=10, value=0)
parch = st.number_input("Parents/Children Aboard", min_value=0, max_value=10, value=0)
fare = st.number_input("Fare", min_value=0.0, value=32.0)
embarked = st.selectbox("Embarked", ["Southampton", "Queenstown", "Cherbourg"])
sex = st.radio("Sex", ["Male", "Female"])

sex_encoded = 1 if sex == "Male" else 0
embarked_mapping = {"Southampton": 2, "Queenstown": 0, "Cherbourg": 1}
embarked_encoded = embarked_mapping[embarked]

input_data = pd.DataFrame([[pclass, sex_encoded ,age, sibsp, parch, fare, embarked_encoded]],
                          columns=["Pclass", "Sex" ,"Age", "SibSp", "Parch", "Fare", "Embarked"])


input_data_scaled = pd.DataFrame(scaler.transform(input_data), columns=scaler_columns)

if st.button("Predict Survival"):
    prediction = model.predict(input_data_scaled)

    if prediction[0] in [1, "Yes"]:
       st.success(" Survived ✅")
    elif prediction[0] in [0, "No"]:
        st.error( " Did Not Survive ❌")
    else:
        result = f"⚠️ Unexpected Output: {prediction[0]}"



with st.sidebar:

    st.markdown(
        """
        <div style="display: flex; gap: 20px; align-items: center;">
            <a href="https://www.linkedin.com/in/zyad-sakoury-135405261/" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="40"/>
            </a>
            <a href="https://www.facebook.com/zyad.ahmedsakoury" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" alt="Facebook" width="40"/>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
