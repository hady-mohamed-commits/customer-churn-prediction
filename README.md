📊 Customer Churn Prediction

An end-to-end Machine Learning project that predicts whether a customer is likely to churn based on customer demographics, services, contract information, and billing details.

🚀 Live Demo

Customer Churn Prediction App

💻 GitHub Repository

GitHub Repository

⸻

🎯 Project Objective

Customer churn is an important business problem. Predicting customers who are likely to leave a service can help businesses identify high-risk customers and take appropriate retention actions.

The goal of this project is to build a classification model that predicts customer churn and provides the estimated probability of churn.

⸻

📂 Dataset

The dataset contains customer information related to:

* Demographics
* Customer tenure
* Services
* Internet services
* Contract type
* Payment method
* Monthly charges
* Total charges

The target variable represents whether the customer churned.

⸻

🔎 Project Workflow

The project follows an end-to-end Machine Learning workflow:

1. Data Loading
2. Exploratory Data Analysis
3. Data Cleaning
4. Missing Values Analysis
5. Duplicate Analysis
6. Outlier Analysis
7. Feature Engineering
8. Feature Selection
9. Data Preprocessing
10. Train/Test Split
11. Model Training
12. Cross-Validation
13. Hyperparameter Tuning
14. Model Evaluation
15. Model Saving
16. Streamlit Deployment

⸻

🤖 Models

Several classification models were evaluated:

* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting

The models were compared using 5-Fold Cross-Validation with ROC-AUC.

Cross-Validation Results

Model	Mean ROC-AUC
Logistic Regression	0.846
Decision Tree	0.818
Random Forest	0.841
Gradient Boosting	0.848

A tuned Random Forest model was selected as the final deployment model.

⸻

⚙️ Hyperparameter Tuning

GridSearchCV with 5-Fold Cross-Validation was used to tune the Random Forest model.

The optimization metric was:

ROC-AUC

The tuned model was then evaluated on the test set.

⸻

📈 Final Model Performance

The tuned Random Forest achieved the following test-set results:

* Accuracy: 78.85%
* Precision: 66.81%
* Recall: 40.37%
* F1-Score: 50.33%
* ROC-AUC: 84.01%

The ROC-AUC indicates that the model has good ability to distinguish between customers who churn and customers who do not churn.

⸻

🛠️ Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Streamlit
* GitHub

⸻

🌐 Deployment

The application was deployed using Streamlit Community Cloud.

Users can enter customer information through the web interface and receive:

* Churn prediction
* Churn probability

Live Application

Open Customer Churn Prediction

⸻

📁 Project Structure

customer-churn-prediction/
│
├── app.py
├── churn_model.pkl
├── requirements.txt
└── README.md

⸻

▶️ Run Locally

Clone the repository:

git clone https://github.com/hady-mohamed-commits/customer-churn-prediction.git

Navigate to the project:

cd customer-churn-prediction

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

⸻

👨‍💻 Project

Hady Mohamed

AI & Machine Learning Developer

Built as an end-to-end Machine Learning project combining model development, evaluation, deployment, and web application development.
