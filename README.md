
# 🎓 Student Placement Prediction Using Machine Learning and Streamlit

## 📌 Project Overview
This project predicts whether a student will be placed or not based on their academic details using a machine learning model.  
It uses Logistic Regression and is deployed using a **Streamlit web app** for real-time user input and predictions.

## 🧠 Problem Statement
Many colleges lack tools to analyze which students are likely to get placed. This project uses historical student data to build a predictive model to help institutions identify students who may need training and support.

## 🚀 Technologies Used
- Python  
- Pandas, NumPy  
- Scikit-learn (for ML)  
- Streamlit (for web app)  
- Pickle (for saving models)  

## 📂 Dataset Features
- `gender`, `ssc_p`, `hsc_p`, `degree_p`, `etest_p`, `mba_p`  
- `ssc_b`, `hsc_b`, `hsc_s`, `degree_t`, `workex`, `specialisation`  
- `status` (Target: Placed / Not Placed)

Dataset source: [Kaggle](https://www.kaggle.com/datasets/benroshan/factors-affecting-campus-placement)

## 🛠️ How It Works
1. Dataset is cleaned and preprocessed (Label Encoding)
2. Logistic Regression model is trained on training data
3. Model and encoders are saved using Pickle
4. A Streamlit app is created for user input and prediction
5. The app shows “✅ Placed” or “❌ Not Placed” instantly

## 📷 Streamlit App Screenshots

### 👇 Input Form  
![Screenshot 1](screenshot1.png)

### ✅ Prediction: Placed  
![Screenshot 2](screenshot2.png)

### ❌ Prediction: Not Placed  
![Screenshot 3](screenshot3.png)

## ▶️ How to Run
```bash
# Step 1: Clone this repository
git clone https://github.com/prasanth07m/placement-predictor

# Step 2: Install requirements
pip install -r requirements.txt

# Step 3: Run the Streamlit app
streamlit run app.py
```

## ✅ Prediction Output
The app returns one of the following results:
- ✅ Placed  
- ❌ Not Placed  

## 📈 Model Accuracy
The Logistic Regression model achieved around **85–90% accuracy** on test data.

## 👨‍💻 Contributors
- Prasanth Bunga (2023-2415224)  
- S. Lavankumar (2023-2415218)  
- K. S S Navadeep (2023-2415216)  
- M. Mahesh (2023-2415227)  
- K. Sai Teja (2023-2415197)

## 📬 Contact
📧 prasanthbunga07@gmail.com
