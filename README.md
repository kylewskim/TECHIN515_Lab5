# TECHIN515 Lab 5 - Edge-Cloud Offloading

## Description

This repository contains the implementation of an edge-cloud offloading strategy for gesture recognition using ESP32 and Microsoft Azure. The project performs inference locally on ESP32 and offloads to the cloud when confidence levels are low.

## Hardware Requirements

- ESP32-based Magic Wand from Lab 4
- MPU6050 sensor
- LED indicators
- USB cable for programming

## Software Requirements

- Arduino IDE with ESP32 board support
- Required Arduino Libraries:
  - Adafruit MPU6050
  - Adafruit Sensor
  - Wire (built-in)
- Microsoft Azure account
- Python 3.8 or newer
- Required Python packages (install via pip):
  ```bash
  pip install -r requirements.txt
  ```

## Project Structure

```
.
├── ESP32_to_cloud/             # ESP32 Arduino code
│   └── ESP32_to_cloud.ino      # Main ESP32 sketch
├── trainer_scripts/            # Scripts
│   ├── train.ipynb            # Model training script
│   └── model_register.ipynb   # Model register script
├── app/                       # Web app for model deployment
│   ├── wand_model.h5         # trained model
│   ├── app.py                # Script of web app
│   └── requirements.txt      # Dependencies required by web app
└── data/                     # Training data directory
    ├── O/                    # O-shape gesture samples
    ├── V/                    # V-shape gesture samples
    ├── Z/                    # Z-shape gesture samples
    └── some_class/          # Some other gesture samples
```

## Setup Instructions

1. Azure Setup

   - Create a Resource Group
   - Set up Azure Machine Learning workspace
   - Create a Compute Instance
   - Upload training data to Azure Blob storage
   - Train and register model
   - Deploy web app

2. ESP32 Setup
   - Flash the ESP32_to_cloud.ino sketch
   - Configure the server URL in the sketch
   - Set confidence threshold as needed

## Usage

1. Train the model using provided Jupyter notebooks in Azure
2. Deploy the web application:
   ```bash
   cd app
   python app.py
   ```
3. Program the ESP32 with the provided sketch
4. Monitor serial output for inference results

## Features

- Local inference on ESP32
- Cloud offloading when confidence is low
- Real-time gesture recognition
- Web API endpoint for cloud inference
- Configurable confidence threshold

## Technologies Used

- ESP32 microcontroller
- Microsoft Azure
- Azure Machine Learning
- Python Flask (Web App)
- TensorFlow/Keras
- Arduino IDE
