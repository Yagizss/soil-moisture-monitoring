\# Soil Moisture Monitoring (IoT)



This project monitors soil moisture sensor data and classifies low-moisture states to decide whether irrigation is needed.



\## How to run

```bash

py -m venv .venv

.\.venv\Scripts\Activate.ps1

py -m pip install -r requirements.txt

py src/train.py

py -m streamlit run dashboard/app.py




