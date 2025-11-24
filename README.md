# URL Phishing Detection Using Machine Learning

## Overview
This project predicts whether a given URL is **phishing** or **legitimate** using machine learning.  
It extracts 15+ handcrafted features from each URL and uses a Random Forest classifier.

## How to Run

### 1. Create virtual environment
```
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies
```
pip install -r api/requirements.txt
```

### 3. Train the model
```
python -m src.train --data data/raw/urls.csv --out models/rf_model.pkl
```

### 4. Start API
```
python api/app.py
```

### 5. Predict using API
Example (PowerShell):
```
curl -Method POST -Uri http://localhost:5000/predict
 -Body (@{url="http://bit.ly/freegift"}
 | ConvertTo-Json) -ContentType "application/json"
```

## Features Extracted
- URL length  
- Number of dots  
- Number of hyphens  
- Number of `@`  
- Is IP address  
- Number of digits  
- Number of subdirectories  
- Suspicious words  
- Uses HTTPS  
- Shortening services  
- Entropy  
- Has "www"  
- TLD length  
- Path length  
- Number of query parameters  

## Model Used
- **Random Forest (150 trees)**
- Balanced class weights
- Predicts probability of phishing

## Output Example
```
{
"prediction": 1,
"probability": 0.91
}
```

## Folder Structure
```
phishing-detector/
src/
api/
models/
data/
...
```

## Author
*Rishit Dangeti*