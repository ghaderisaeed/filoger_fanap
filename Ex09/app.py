import streamlit as st
import pandas as pd

from utils import load_models_transformers, is_valid_format, process_and_predict


## Loading models and transformers just once:
model_1, model_2, model_3, model_4, model_5, transform_1, transform_2 = load_models_transformers()


st.sidebar.image("./assets/logo.png", width=200)
st.sidebar.markdown("## __Loan Repayment Prediction__")

input_method = st.sidebar.radio("Choose input method:", 
                 ("Enter values in boxes", "Upload a file"))

st.sidebar.info(body= "An AI-based system by Data Visionaries", icon=None)

is_df = False

# Define the names of the input boxes
input_names = [
    "credit_policy", "purpose", "int_rate", "installment", "log_annual_in", 
    "dti", "fico", "days_with_cr_lin", "revol_bal", "revol_util", 
    "inq_last_6mths", "delinq_2yrs", "pub_rec"
]

if input_method == "Enter values in boxes":
    st.markdown("### Please enter the required information:")
    data = {}
    data["credit_policy"] = st.radio("Credit Policy:", (0, 1))
    data["purpose"] = st.selectbox("The purpose of the loan:", 
                 ('all_other', 'credit_card', 'debt_consolidation', 'educational', 'home_improvement', 'major_purchase', 'small_business'))
    data["int_rate"] = st.number_input("The interest rate of the loan:", 
                             min_value=0.04, max_value=2.2, step=0.01, format="%.2f")
    data["installment"] = st.number_input("The monthly installments owed by the borrower:", 
                             min_value=15.0, max_value=941.0, step=10.0, format="%.2f")
    data["log_annual_in"] = st.number_input("The natural log of the self-reported annual income of the borrower:", 
                             min_value=7.0, max_value=15.0, step=0.1, format="%.6f")
    data["dti"] = st.number_input("The debt-to-income ratio of the borrower:", 
                             min_value=0.0, max_value=30.0, step=10.0, format="%.2f")
    data["fico"] = st.number_input("The FICO credit score of the borrower:", 
                             min_value=610, max_value=830, step=5, format="%d")
    data["days_with_cr_lin"] = st.number_input("The number of days the borrower has had a credit line:", 
                             min_value=178.0, max_value=17640.0, step=50.0, format="%.3f")
    data["revol_bal"] = st.number_input("The borrower's revolving balance:", 
                             min_value=0, max_value=1207359, step=100, format="%d")
    data["revol_util"] = st.number_input("The borrower's revolving line utilization rate:", 
                             min_value=0.0, max_value=119.0, step=10.0, format="%.1f")
    data["inq_last_6mths"] = st.number_input("The borrower's number of inquiries by creditors in the last 6 months:", 
                             min_value=0, max_value=33, step=2, format="%d")
    data["delinq_2yrs"] = st.number_input("'delinq.2yrs' The number of times the borrower had been 30+ days past due on a payment in the past 2 years:",
                     min_value=0, max_value=13, step=1, format="%d")
    data["pub_rec"] = st.number_input("The borrower's number of derogatory public records:", 
                             min_value=0, max_value=5, step=1, format="%d")
    df = pd.Series(data).to_frame().T
    is_df = True

if input_method == "Upload a file":
    st.markdown("### Please Upload a file contain values:")
    ## Add file uploader
    uploaded_file = st.file_uploader(label= "Choose a file", type=["txt", "csv", "xlsx"], 
                                     help= "The columns should be in the following order: " +
                                     "credit_policy purpose int_rate installment log_annual_in dti fico " +
                                      "days_with_cr_lin revol_bal revol_util inq_last_6mths delinq_2yrs pub_rec" ) 
    ## Process file if uploaded
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.txt'):
            ## Read txt file
            df = pd.read_csv(uploaded_file, sep=' ', names = input_names)
           
        elif uploaded_file.name.endswith('.csv'):
            ## Read csv file
            df = pd.read_csv(uploaded_file, names = input_names)

        elif uploaded_file.name.endswith('.xlsx'):
            ## Read xlsx file
            df = pd.read_excel(uploaded_file, header=None)
            df.columns = input_names
            
        ## Show the dataframe
        st.dataframe(df)
        is_df = True

## Add a button to make prediction
if st.button('Predict') and is_df:
    ## Checking the validity of data format
    result = is_valid_format(df)
    if result is True:
        st.success("All inputs are valid.")
        ## Do preprocessing and make prediction
        data_pred = process_and_predict(df, model_1, model_2, model_3, model_4, model_5, transform_1, transform_2)
            
        st.markdown("##### 'pred = Yes/No' indicate the possibility of facing difficulties in repaying the loan")
        ## Show the dataframe
        st.dataframe(data_pred)
        
    else:
        # st.error("Errors: " + "; ".join(result))
        st.error("Errors:  \n" + "  \n".join(result))
