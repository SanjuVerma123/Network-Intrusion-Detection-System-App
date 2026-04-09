# 🚀 Network Intrusion Detection System (NIDS)

A Machine Learning-based Network Intrusion Detection System that detects malicious network activities and classifies them as normal or attack using advanced ML models.

## 📌 Project Overview
This project analyzes network traffic data and predicts whether a connection is normal or an intrusion (attack) using Machine Learning.

## It is built using:
Data preprocessing & feature engineering
Encoding categorical variables
Model training (XGBoost)
Deployment using Streamlit

## 🧠 Features
✅ Detects network intrusions in real-time
✅ Uses trained ML model for prediction
✅ Handles categorical encoding using saved encoders
✅ Streamlit-based interactive UI
✅ Ready for deployment

## 📂 Project Structure
├── app.py                      # Streamlit web app
├── model.pkl                   # Trained ML model
├── encoders.pkl                # Label encoders
├── columns.pkl                 # Feature columns
├── KDDTrain+.txt               # Dataset
├── Network_Intrusion_detection_System.ipynb  # Training notebook
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation

## ⚙️ Installation & Setup
#### 1️⃣ Clone Repository
git clone https://github.com/SanjuVerma123/Network-Intrusion-Detection-System-App.git
cd Network-Intrusion-Detection-System-App

#### 2️⃣ Install Dependencies
pip install -r requirements.txt

#### 3️⃣ Run the App
streamlit run app.py

## 📊 Machine Learning Model
Algorithm: XGBoost Classifier
Handles imbalance and complex patterns efficiently
Trained on KDD Dataset

## 🔮 How It Works
User inputs network features
Data is preprocessed using saved encoders
Features aligned using columns.pkl
## Model predicts:
Normal
Attack

## 🖥️ Tech Stack
Python 🐍
Pandas & NumPy
Scikit-learn
XGBoost
Streamlit

## 📸 Screenshots
Add your app screenshots here
![App Screenshot](screenshots/app.png)

🚀 Future Improvements
🔥 Add SHAP Explainability
📡 Real-time packet capture
☁️ Deploy on cloud (AWS / Render)
📈 Improve model accuracy
👨‍💻 Author

#### Sanju Verma

GitHub: https://github.com/SanjuVerma123
LinkedIn: https://www.linkedin.com/in/sanju123

## ⭐ Contribute
Feel free to fork this repo and improve it!

## 📜 License
This project is open-source and available under the MIT License.
