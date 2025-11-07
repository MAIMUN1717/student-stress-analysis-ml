<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0d1117&height=140&section=header&text=Student%20Stress%20Analysis%20Using%20Machine%20Learning&fontSize=30&fontColor=58a6ff&animation=scaleIn" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=22&pause=1000&duration=3000&color=58A6FF&center=true&vCenter=true&width=700&lines=Welcome+to+the+Student+Stress+Analysis+Project!;A+Complete+End-to-End+Machine+Learning+Solution;With+EDA+%7C+Classification+%7C+Clustering+%7C+Streamlit+App;Project+By+MAIMUN+BANU" />
</p>

<br>

<p align="center">
  <img src="https://img.shields.io/badge/Author-MAIMUN%20BANU-58a6ff?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Dataset-1000%20Students-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Accuracy-94.5%25-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/App-Streamlit-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Languages-Python-yellow?style=flat-square&logo=python" />
  <img src="https://img.shields.io/badge/Algorithms-Logistic%20Regression%20%7C%20Random%20Forest-darkgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/Clustering-KMeans-blueviolet?style=flat-square" />
  <img src="https://img.shields.io/badge/Notebook-Jupyter-orange?style=flat-square&logo=jupyter" />
</p>

<br>

<p align="center">
  <sub style="color:#8b949e;">A beautifully crafted ML project showcasing real data analysis, visualizations, predictive modeling, clustering insights, and a full Streamlit Web Application.</sub>
</p>

<br>


# 🎓 Student Stress Level Analysis Using Machine Learning

This project predicts the **stress level of students (Low, Medium, High)** using machine learning techniques based on academic, social, lifestyle, and behavioral factors.  
It also includes a **Streamlit web application** for real-time stress prediction.

---

## ✅ Project Overview
The goal of this project is to:

- Analyze factors influencing student stress  
- Predict stress levels using classification models  
- Discover hidden behavioral patterns using clustering  
- Build a user-friendly Streamlit app for predictions  
- Provide insights via intuitive visualizations  

This is a complete **end-to-end machine learning project**, suitable for academic submission, portfolio display, or practical ML demonstrations.

---

## ✅ Project Structure

student_stress_project/
│
├── student_stress_analysis.ipynb → Main project notebook
├── student_stress.csv → Dataset
│
├── streamlit_app.py → Streamlit prediction app
├── stress_prediction.py → Standalone prediction script
│
├── models/ → Saved ML models
│ ├── logreg_pipeline.joblib → Logistic Regression pipeline (best model)
│ ├── random_forest.joblib → Random Forest model (optional)
│ ├── label_encoder.joblib → Label encoder (Low/Medium/High)
│ ├── scaler_for_kmeans.joblib → Scaler used for clustering
│ ├── kmeans_k3.joblib → K-Means clustering model (k=3)
│ └── pca_2d.joblib → PCA transformer (2 components)
│
└── README.md → Project documentation

yaml
Copy code

---

## ✅ Dataset Description

The dataset contains **1000 student entries**, each with the following features:

| Feature | Description |
|--------|-------------|
| sleep_hours | Average sleep hours per day |
| study_hours | Study time per day |
| academic_pressure | Academic pressure (1–10) |
| peer_pressure | Peer influence (1–10) |
| financial_stress | Financial stress (1–10) |
| physical_activity | Exercise time per day (hours) |
| diet_quality | Diet score (1–5) |
| screen_time | Daily screen time (hours) |
| attendance | Attendance percentage |
| social_support | Emotional/Social support score (1–10) |
| stress_level | Target label (Low, Medium, High) |

Dataset contains **no missing values** and is ready for model training.

---

## ✅ Machine Learning Models Used

### ✅ 1. Logistic Regression (Best Model)
- Accuracy: **94.5%**
- Excellent classification of High and Low stress levels
- Balanced F1-score across all classes
- Used in Streamlit app for predictions

### ✅ 2. Random Forest Classifier
- Accuracy: **77%**
- Good interpretability via feature importance
- Key contributors: academic pressure, financial stress, peer pressure

### ✅ 3. K-Means Clustering (k = 3)
Cluster insights:
- **Cluster 1:** High stress students → high peer pressure & financial stress
- **Cluster 2:** Low stress students → good sleep, low screen time, low academic pressure
- **Cluster 0:** Mixed group → moderate stress

---

## ✅ Visualizations Included
- Stress Level Distribution Bar Chart  
- Histograms (Sleep Hours, Academic Pressure, Financial Stress)  
- Correlation Heatmap  
- Feature Importance Bar Chart  
- PCA 2D Cluster Visualization  

These graphs help understand stress patterns and model behavior.

---

## ✅ Running the Streamlit App

### 1️⃣ Install Streamlit
pip install streamlit

shell
Copy code

### 2️⃣ Go to the project folder
cd student_stress_project

shell
Copy code

### 3️⃣ Run the app
streamlit run streamlit_app.py

yaml
Copy code

Your browser will open the Student Stress Predictor interface.

---

## ✅ Running the Python Prediction Script

Run:
python stress_prediction.py

lua
Copy code

Example output:
Predicted Stress Level: High

yaml
Copy code

---

## ✅ Requirements

Create a `requirements.txt` with:

pandas
numpy
scikit-learn
streamlit
joblib
matplotlib

yaml
Copy code

Install everything:
pip install -r requirements.txt

yaml
Copy code

---

## ✅ Conclusion

This project successfully:

- Predicts student stress with **94.5% accuracy**
- Identifies key stress contributors (academic, financial, peer pressure)
- Discovers student groups using clustering
- Provides a real-time prediction app using Streamlit
- Demonstrates complete end-to-end machine learning workflow

It is fully suitable for academic submission, portfolio display, or deployment.

---

## ✅ Future Enhancements
- Collect real student survey data  
- Add more psychological features (motivation, anxiety score)  
- Train advanced models like XGBoost or Neural Networks  
- Deploy Streamlit app online  
- Add database integration for logs & monitoring  

---

**✅ Project Completed Successfully.**

---

---

<br>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=wave&color=0d1117&height=120&section=footer" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=58A6FF&center=true&vCenter=true&width=700&lines=Thank+You+for+Viewing+This+Project!;Student+Stress+Analysis+%7C+Machine+Learning+%7C+Streamlit+App;Made+with+Care+by+MAIMUN+BANU+" />
</p>

<br>

<p align="center">
  <img src="https://img.shields.io/badge/Project%20Status-Completed-2ea043?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Advanced-1f6feb?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Built%20With-Python-FFD43B?style=for-the-badge&logo=python&logoColor=white" />
</p>

<br>

<p align="center" style="color:#58a6ff; font-weight:bold; font-size:18px;">
  Connect With Me
</p>

<p align="center">
  <a href="https://github.com/MAIMUN1717" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
  &nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/maimun-banu" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  &nbsp;&nbsp;
  <a href="mailto:maimunr17@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
</p>

<br>

<p align="center" style="color:#8b949e;">
  © 2025 <strong>MAIMUN BANU</strong> • All Rights Reserved.
</p>

<p align="center" style="color:#8b949e;">
  ⭐ If you found this project helpful, please consider giving it a star!
</p>

<br>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=wave&color=0d1117&height=100&section=footer" />
</p>
