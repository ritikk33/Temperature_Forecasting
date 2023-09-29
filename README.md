# Temperature Forecasting

This project focuses on predicting temperature values using a Long Short-Term Memory (LSTM) neural network. Time series analysis is employed to model historical temperature data and make accurate temperature forecasts.

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Results](#results)
- [Dependencies](#dependencies)
- [Contributing](#contributing)

## Introduction

Temperature prediction plays a crucial role in various fields, from weather forecasting to climate research. This project demonstrates the use of LSTM neural networks for time series forecasting, specifically for predicting temperature values based on historical data.

## Getting Started

To get started with this project, follow these steps:

## Usage

# Clone the repository:

git clone https://github.com/abhigyan02/temperature-prediction.git
cd temperature-prediction

install dependencies 

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Prepare your data:

Ensure your temperature data is in the format expected by the script.
Modify the file path in the code to point to your data.

# Run
python temperature_prediction.py
The script will output training progress and display the test set results, including a mean squared error score.

## Results
The LSTM model architecture is defined in the script, leveraging Keras for implementation.
The model is trained on historical temperature data and evaluated on a test set.
The test set predictions are visualized alongside the actual temperature data using Matplotlib.

![image](https://github.com/abhigyan02/temperature-prediction/assets/75851981/e2e3bdde-ce3f-4a89-943d-3a56b13a14f2)

## Dependencies
Python 3.x
NumPy
pandas
Matplotlib
scikit-learn
Keras
Install the required dependencies using the provided requirements.txt file:

pip install -r requirements.txt


## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to create a pull request.
