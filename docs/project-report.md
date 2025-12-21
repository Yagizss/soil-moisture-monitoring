1\. Introduction



Indoor plants require proper watering to remain healthy.

However, incorrect watering practices such as overwatering or underwatering are common and may lead to plant damage or death.

This project aims to design an IoT-based soil moisture monitoring system that analyzes soil moisture data and assists users in making irrigation decisions.



The system combines sensor data analysis, machine learning, and a web-based dashboard to provide real-time insights into soil moisture conditions.



2\. Problem Definition



Manual monitoring of soil moisture is inefficient and unreliable, especially when multiple plants are involved.

Different plants and soil conditions exhibit different moisture behaviors, making a fixed threshold approach insufficient.



The main problems addressed in this project are:



Detecting low-moisture conditions accurately



Preventing unnecessary watering



Providing a clear and interpretable user interface



3\. System Overview



The system consists of three main components:



Data Collection Layer



Machine Learning Model



Visualization and Alert System



Soil moisture data is processed offline for training, and the trained model is then used by the dashboard to generate alerts.



4\. Sensors and Dataset Description



The dataset contains measurements from four capacitive soil moisture sensors, each placed in a separate pot.



moisture0: Control pot (soil only, no plant)



moisture1–3: Plant pots containing vegetation



The control pot provides a baseline reference to distinguish natural soil drying from plant-driven moisture consumption.



Sensor readings are normalized between 0 and 1, where higher values indicate higher moisture content.



The dataset includes timestamp information:



Year



Month



Day



Hour



Minute



5\. Machine Learning Approach



A supervised classification model is trained to detect low-moisture conditions.



Target Classes:



0: Soil moisture is sufficient



1: Soil moisture is low (watering recommended)



The model learns moisture patterns from historical data and outputs a binary decision used by the dashboard.



Model performance metrics include:



Precision



Recall



F1-score



Accuracy



The trained model is saved and reused without retraining during deployment.



6\. Dashboard and Alert System



A Streamlit-based dashboard visualizes soil moisture trends over time.



Key features:



Time-series visualization of all four sensors



Clear labeling of sensor roles



“WATER NOW” alert for low-moisture detection



The alert system is designed as an early-warning mechanism, prioritizing plant safety over delayed responses.



7\. Deployment



The application is deployed on an AWS EC2 (t3.micro) instance using the Free Tier.



Deployment details:



Operating System: Ubuntu 22.04



Web Framework: Streamlit



Open Port: 8501



Access via public IPv4 address



The instance can be stopped when not in use to reduce costs.



8\. Limitations



Sensor noise may affect readings



Dataset is not collected in real time



Thresholds may trigger conservative alerts



These limitations are acceptable within the scope of a prototype system.



9\. Future Work



Possible improvements include:



Real-time sensor integration



Adaptive thresholding per plant



Mobile notifications



Additional environmental sensors (temperature, humidity)



10\. Conclusion



This project demonstrates an effective IoT-based soil moisture monitoring system using machine learning and cloud deployment.

The system successfully identifies low-moisture conditions and provides user-friendly visualization and alerts, supporting better indoor plant care decisions.

