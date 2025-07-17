import streamlit as st
import pickle
import numpy as np

# Load model and encoders
model = pickle.load(open("placement_model.pkl", "rb"))
label_encoders = pickle.load(open("label_encoders.pkl", "rb"))

st.title("🎓 Student Placement Prediction")
st.subheader("Created by Prasanth Bunga 🎓")

# Input fields
gender = st.selectbox("Gender", ["M", "F"])
ssc_p = st.number_input("SSC Percentage (10th)", min_value=0.0, max_value=100.0)
hsc_p = st.number_input("HSC Percentage (12th)", min_value=0.0, max_value=100.0)
degree_p = st.number_input("Degree Percentage", min_value=0.0, max_value=100.0)
etest_p = st.number_input("Employment Test %", min_value=0.0, max_value=100.0)
mba_p = st.number_input("MBA Percentage", min_value=0.0, max_value=100.0)

ssc_b = st.selectbox("SSC Board", ["Central", "Others"])
hsc_b = st.selectbox("HSC Board", ["Central", "Others"])
hsc_s = st.selectbox("HSC Stream", ["Science", "Commerce", "Arts"])
degree_t = st.selectbox("Degree Type", ["Sci&Tech", "Comm&Mgmt", "Others"])
workex = st.selectbox("Work Experience", ["Yes", "No"])
specialisation = st.selectbox("MBA Specialisation", ["Mkt&Fin", "Mkt&HR"])

# Convert inputs to model format
input_dict = {
    "gender": gender,
    "ssc_p": ssc_p,
    "ssc_b": ssc_b,
    "hsc_p": hsc_p,
    "hsc_b": hsc_b,
    "hsc_s": hsc_s,
    "degree_p": degree_p,
    "degree_t": degree_t,
    "workex": workex,
    "etest_p": etest_p,
    "specialisation": specialisation,
    "mba_p": mba_p
}

# Encode categorical fields
for col in label_encoders:
    if col in input_dict:
        input_dict[col] = label_encoders[col].transform([input_dict[col]])[0]

features = np.array(list(input_dict.values())).reshape(1, -1)

# Predict button
if st.button("Predict Placement"):
    prediction = model.predict(features)
    result = "✅ Placed" if prediction[0] == 1 else "❌ Not Placed"
    st.success(f"Prediction: {result}")

# Footer section
st.markdown("---")
st.subheader("📌 Project by Prasanth Bunga")
st.caption("© 2025 | Built for Academic Submission 🎓")
st.markdown("📧 Contact: prasanthbunga07@gmail.com")
st.success("Thank you for using this app! 😊")