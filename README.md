Liver Disease Prediction Using Machine Learning
Project Overview
This project demonstrates a machine learning approach to classifying liver disease using patient information and liver function test parameters.
A Random Forest classifier was developed and deployed through a Streamlit web application.
Technologies Used
	•	Python
	•	Pandas and NumPy
	•	Scikit-learn
	•	Matplotlib and Seaborn
	•	Streamlit
	•	Joblib
	•	Jupyter Notebook
Machine Learning Workflow
	1	Data collection and understanding
	2	Exploratory Data Analysis (EDA)
	3	Data cleaning and missing-value treatment
	4	Feature engineering and preprocessing
	5	Model training and comparison
	6	Hyperparameter tuning
	7	Feature selection
	8	Model evaluation using cross-validation and ROC-AUC
	9	Model serialization using Joblib
	10	Streamlit application development
Models Evaluated
	•	Logistic Regression
	•	Random Forest
	•	Decision Tree
	•	K-Nearest Neighbors
	•	Support Vector Machine
	•	Gradient Boosting
Best Model
Tuned Random Forest Classifier.
Preliminary Evaluation Results
	•	Test Accuracy: 77.8%
	•	Test Balanced Accuracy: 77.4%
	•	Test ROC-AUC: 82.8%
	•	5-Fold CV Balanced Accuracy: 68.4%
These results are preliminary and based on a small dataset.
Application
The Streamlit application accepts patient parameters and displays the model's predicted class and estimated disease probability.
Disclaimer
This project is intended strictly for educational and research demonstration purposes. It is not a clinically validated diagnostic system and must not be used for medical decisions.
