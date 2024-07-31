import joblib
import numpy as np
import streamlit as st


MODEL_FILE = "./RF_Loan_model.joblib"
model = joblib.load(MODEL_FILE)


def predict(
        Gender,
        Married,
        Dependants,
        Education,
        Self_Employed,
        ApplicantIncome,
        CoapplicantIncome,
        LoanAmount,
        Loan_Amount_Term,
        Credit_History,
        Property_Area
):
    Gender = 1 if Gender == "Male" else 0
    Married = 1 if Married == "Yes" else 0
    Education = 1 if Education == "Graduate" else 0
    Self_Employed = 1 if Self_Employed == "Yes" else 0
    Credit_History = 1 if Credit_History == "Outstanding Loan" else 0

    if Property_Area == "Rural":
        Property_Area = 0
    elif Property_Area == "Semi Urban":
        Property_Area = 1  
    else:
        Property_Area = 2

    Total_Income = np.log(ApplicantIncome + CoapplicantIncome)

    prediction = model.predict([[
        Gender,
        Married,
        Dependants,
        Education,
        Self_Employed,
        LoanAmount,
        Loan_Amount_Term,
        Credit_History,
        Property_Area,
        Total_Income
    ]])

    print(prediction)
    return "Rejected" if prediction == 0 else "Approved"



# Front End
def main():
    st.title("Welcome to the Loan Eligibility Check application!")
    st.header("Please enter your details to get a prediction.")

    Gender = st.selectbox("Gender", ("Male", "Female"))
    Married = st.selectbox("Married", ("Yes", "No"))
    Dependants = st.number_input("Number of Dependants")
    Education = st.selectbox("Education", ("Graduate", "Not Graduate"))
    Self_Employed = st.selectbox("Self Employed", ("Yes", "No"))
    ApplicantIncome = st.number_input("Applicant Income")
    CoapplicantIncome = st.number_input("Coapplicant Income")
    LoanAmount = st.number_input("Loan Amount")
    Loan_Amount_Term = st.number_input("Loan Amount Term")
    Credit_History = st.selectbox("Credit History", ("Outstanding Loan", "No Outstanding Loan"))
    Property_Area = st.selectbox("Property Area", ("Rural", "Urban", "Semi Urban"))

    if st.button("Predict"):
        result = predict(
            Gender,
            Married,
            Dependants,
            Education,
            Self_Employed,
            ApplicantIncome,
            CoapplicantIncome,
            LoanAmount,
            Loan_Amount_Term,
            Credit_History,
            Property_Area
        )

        if result == "Approved":
            st.success("Your loan application might be approved.")
        else:
            st.warning("Your loan application might be rejected.")


if __name__ == "__main__":
    main()