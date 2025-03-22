Forest Fire Prediction Project

This project predicts the burned area of forest fires using a Random Forest Regressor model. It includes a Jupyter Notebook for training the model, a Streamlit app for making predictions, and a CSV dataset.

---

### **Project Structure**
1. `forest_fire_prediction.ipynb`: Jupyter Notebook for training the model.
2. `app.py`: Streamlit app for making predictions.
3. `forest_fires.csv`: Dataset containing forest fire data.
4. `model.pkl`: Pickle file containing the trained model.
5. `README.txt`: This file.

---

### **Dataset**
The dataset (`forest_fires.csv`) contains the following columns:
- X: X-axis spatial coordinate (1-9)
- Y: Y-axis spatial coordinate (2-9)
- month: Month of the year (1-12)
- day: Day of the week (1-7)
- FFMC: Fine Fuel Moisture Code
- DMC: Duff Moisture Code
- DC: Drought Code
- ISI: Initial Spread Index
- temp: Temperature in Celsius
- RH: Relative Humidity
- wind: Wind speed in km/h
- rain: Rainfall in mm
- area: Burned area of the forest (target variable)

---

### **Steps to Run the Project**

1. **Install Required Libraries**
   Run the following command to install the required libraries:

2. **Train the Model**
- Open `forest_fire_prediction.ipynb` in Jupyter Notebook.
- Run all cells to train the model and save it as `model.pkl`.

3. **Run the Streamlit App**
- Open a terminal in the project directory.
- Run the following command to start the Streamlit app:
  ```
  streamlit run app.py
  ```
- Open the provided URL in your browser to interact with the app.

4. **Make Predictions**
- Use the input fields in the Streamlit app to enter feature values.
- Click the "Predict" button to see the predicted burned area.

---

### **Dependencies**
- Python 3.x
- pandas
- numpy
- scikit-learn
- streamlit

---

### **Author**
Your Vijay Raj M

---

### **License**
This project is licensed under the MIT License. See the LICENSE file for details.