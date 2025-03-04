# Setup Virtual Environment

```python
conda create -n fastapi-env python=3.11
conda activate fastapi-env
pip install -r requirements.txt
```

# Running the server
`uvicorn main:app --reload`

The command `uvicorn main:app` refers to:
- main: the file main.py (the Python "module").
- app: the object created inside of main.py with the line app = FastAPI().
- --reload: make the server restart after code changes. Only use for development.


## JSON Response

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "Gender": 0,
  "Married": 0,
  "Dependents": 0,
  "Education": 0,
  "Self_Employed": 0,
  "LoanAmount": 0,
  "Loan_Amount_Term": 0,
  "Credit_History": 0,
  "Property_Area": 0,
  "TotalIncome": 0
}'

```

```json
Yes
```