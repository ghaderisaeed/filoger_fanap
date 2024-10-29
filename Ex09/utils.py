import streamlit as st
import pickle
from keras.models import load_model

import numpy as np
import pandas as pd


@st.cache_resource  # Add the caching decorator
def load_models_transformers():
    model_paths = {
        'model_1': './models/knn_model.pkl', # a machine learning model
        'model_2': './models/dl_model_simple.keras', # a deep learning keras model
        # 'model_3': './models/dl_model_mch.keras', # a deep learning keras model
        'model_3': './models/dl_model_mch1.keras', # a deep learning keras model
        'model_4': './models/svm_model.pkl', # a machine learning model
        'model_5': './models/xgb_model.pkl', # a machine learning model
    }

    transform_paths = {
        'transform_1': './transformers/ct_ohe.h5', # a one-hot encoding transformer
        'transform_2': './transformers/scaler.h5', # a scaling transformer
    }

    ## Loading the first model
    with open(model_paths['model_1'], 'rb') as file:
        model_1 = pickle.load(file)

    with open(model_paths['model_4'], 'rb') as file:
        model_4 = pickle.load(file)

    with open(model_paths['model_5'], 'rb') as file:
        model_5 = pickle.load(file)
        
    ## Loading the second model
    model_2 = load_model(model_paths['model_2'])

    ## Loading the third model
    model_3 = load_model(model_paths['model_3'])

    ## Loading transformers for preprocessing data
    with open(transform_paths['transform_1'], 'rb') as f:
        transform_1 = pickle.load(f)

    with open(transform_paths['transform_2'], 'rb') as f:
        transform_2 = pickle.load(f)
    

    return model_1, model_2, model_3, model_4, model_5, transform_1, transform_2 


def is_valid_format(data):
    error_messages = []
    try:
        int(data.get("credit_policy")[0])
    except ValueError:
        error_messages.append("credit_policy must be a valid integer.")

    if data.get("purpose")[0] not in ['all_other', 'credit_card', 'debt_consolidation', 'educational', 'home_improvement', 'major_purchase', 'small_business']:
        error_messages.append("purpose: Invalid purpose selected.")
        
    try:
        float(data.get("int_rate")[0])
    except ValueError:
        error_messages.append("int_rate must be a valid number.")
    try:
        float(data.get("installment")[0])
    except ValueError:
        error_messages.append("installment must be a valid number.")
    try:
        float(data.get("log_annual_in")[0])
    except ValueError:
        error_messages.append("log_annual_in must be a valid number.")
    try:
        float(data.get("dti")[0])
    except ValueError:
        error_messages.append("dti must be a valid number.")
    try:
        int(data.get("fico")[0])
    except ValueError:
        error_messages.append("fico must be a valid integer.")
    try:
        float(data.get("days_with_cr_lin")[0])
    except ValueError:
        error_messages.append("days_with_cr_lin must be a valid number.")
    try:
        int(data.get("revol_bal")[0])
    except ValueError:
        error_messages.append("revol_bal must be a valid integer.")
    try:
        float(data.get("revol_util")[0])
    except ValueError:
        error_messages.append("revol_util must be a valid number.")
    try:
        int(data.get("inq_last_6mths")[0])
    except ValueError:
        error_messages.append("inq_last_6mths must be a valid integer.")
    try:
        int(data.get("delinq_2yrs")[0])
    except ValueError:
        error_messages.append("delinq_2yrs must be a valid integer.")
    try:
        int(data.get("pub_rec")[0])
    except ValueError:
        error_messages.append("pub_rec must be a valid integer.")

    if error_messages:
        return error_messages
    else:
        return True


def process_and_predict(data_test, model_1, model_2, model_3, model_4, model_5, transform_1, transform_2):
    ## Convert valid dataframe to numpy array:
    X_test = data_test.iloc[:,:].values

    ## Do preprocessing on data:
    X_test = transform_1.transform(X_test)
    X_test = transform_2.transform(X_test)

    ## Make predictions:
    pred_1 = model_1.predict(X_test)
    pred_2 = model_2.predict(X_test)
    pred_3 = model_3.predict([X_test[:,:9], X_test[:,9:]])
    pred_4 = model_4.predict(X_test)
    pred_5 = model_5.predict(X_test)

    ## Assigning thresholds for deep learning models acquired during the model design phase:
    thr_2 = 0.5 # Threshold for model_2
    thr_3 = 0.5 # Threshold for model_3
    
    ## Converting predictions to Yes/No with confidence number:
    ## Might they struggle with repaying the loan? pred = Yes/No
    pred_1 = np.where(pred_1 == 1, 'Yes', 'No')
    confid_2 = np.round(np.where(pred_2 >= thr_2, pred_2, 1-pred_2), decimals=2)
    pred_2 = np.where(pred_2 >= thr_2, 'Yes', 'No')
    confid_3 = np.round(np.where(pred_3 >= thr_3, pred_3, 1-pred_3), decimals=2)
    pred_3 = np.where(pred_3 >= thr_3, 'Yes', 'No')
    pred_4 = np.where(pred_4 == 1, 'Yes', 'No')
    pred_5 = np.where(pred_5 == 1, 'Yes', 'No')

    ## append predictions and confidence numbers to the test dataframe:
    data_test["ML_pred"] = pred_1.flatten()
    data_test["DL_1_pred"] = pred_2.flatten()
    data_test["DL_1_confid"] = confid_2.flatten()
    data_test["DL_2_pred"] = pred_3.flatten()
    data_test["DL_2_confid"] = confid_3.flatten()
    data_test["SVM_pred"] = pred_4.flatten()
    data_test["XGB_pred"] = pred_5.flatten()
    
    return data_test
 