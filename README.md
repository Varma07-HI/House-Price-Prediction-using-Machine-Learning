# 🏡 House Price Prediction App

A complete **Machine Learning project** that predicts house prices using an **XGBoost Regressor**.  
The model is trained on housing data and deployed as an **interactive web app** using Streamlit.

🌐 **Live Demo:** [https://house-prices-predictions001.streamlit.app](https://house-prices-predictions001.streamlit.app)

---

## 📁 Project Structure
.
├── app.ipynb # Jupyter notebook (optional data exploration)
├── app.py # Model training and preprocessing script
├── dataset.csv # Dataset used for training
├── requirements.txt # Dependencies file
├── xgb_model.jb # Trained XGBoost model


---

## 🧠 Features

### 🔹 Model Training (`app.py`)
- Loads and cleans the dataset  
- Handles missing values and encodes categorical columns  
- Selects top correlated features with `SalePrice`  
- Trains an **XGBoost Regressor**  
- Evaluates model performance using:
  - **Mean Absolute Error (MAE)**
  - **R² Score**
- Saves the trained model as `xgb_model.jb`

### 🔹 Web App (Streamlit)
- User-friendly interface to predict house prices  
- Form-based input for property details  
- Real-time price prediction  
- Expander for viewing entered data  
- Balloons animation 🎈 after prediction  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/house-price-prediction.git
cd house-price-prediction


2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Train the model (optional)
python app.py

🚀 Run the App Locally

To launch the Streamlit app on your local machine:

streamlit run app.py


Then open the local URL (usually http://localhost:8501) in your browser.

Or visit the live deployed version directly at:
👉 https://house-prices-predictions001.streamlit.app
