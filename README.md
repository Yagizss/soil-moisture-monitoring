# Soil Moisture Monitoring (IoT)

## Project Overview
This project implements an IoT-based soil moisture monitoring system for indoor plant care.
The system monitors soil moisture levels using multiple sensors and provides irrigation
recommendations based on learned moisture patterns.

## Problem Definition
Incorrect watering is one of the main reasons for indoor plant health issues.
Overwatering can cause root rot, while underwatering leads to dehydration.
This project aims to automatically detect low-moisture conditions and notify the user
when irrigation is needed.

## Sensors and Data Description
The dataset contains readings from four capacitive soil moisture sensors:

- **moisture0**: Control pot (soil only, no plant)
- **moisture1–3**: Plant pots with active vegetation

Sensors are placed in separate pots to capture different moisture dynamics.
All values are normalized between 0 and 1.

## Dataset
The dataset was collected at a regular sampling frequency and includes timestamps
(year, month, day, hour, minute) and moisture readings.
The control pot is used as a baseline reference.

## Machine Learning Model
A supervised classification model is trained to detect low-moisture conditions.
The model outputs a binary decision:
- 0: Sufficient moisture
- 1: Irrigation needed

The trained model is saved and reused by the dashboard.

## Dashboard
A Streamlit dashboard visualizes moisture trends and displays a **WATER NOW**
alert when low moisture conditions are detected.

The alert is designed as an early-warning system.

## How to Run Locally
```bash
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py src/train.py
py -m streamlit run dashboard/app.py



