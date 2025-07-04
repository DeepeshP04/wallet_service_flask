import streamlit as st
import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:5000"

st.set_page_config(page_title="Wallet Admin Dashboard", layout="centered")
st.title("Wallet Admin Dashboard")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Choose a page",
    ["Wallet Operations", "Reports"]
)

if page == "Wallet Operations":
    st.header("Wallet Operations")
    
    # Wallet Activation Section
    st.subheader("Activate Wallet")
    with st.form("activate_wallet_form"):
        user_id = st.number_input("User ID", min_value=1, value=1, step=1)
        currency = st.selectbox("Currency", ["INR", "USD", "EUR", "GBP"], index=0)
        
        if st.form_submit_button("Activate Wallet"):
            try:
                response = requests.post(
                    f"{BASE_URL}/wallet/init",
                    json={"user_id": user_id, "currency": currency},
                    headers={"Content-Type": "application/json"}
                )
                
                if response.status_code == 201:
                    st.success("Wallet activated successfully!")
                    st.json(response.json())
                else:
                    st.error(f"Error: {response.json()}")
            except requests.exceptions.RequestException as e:
                st.error(f"Connection error: {e}")
    
    st.divider()
    
    # Add Money Section
    st.subheader("Add Money to Wallet")
    with st.form("add_money_form"):
        add_user_id = st.number_input("User ID", min_value=1, value=1, step=1, key="add_user_id")
        amount = st.number_input("Amount", min_value=0.01, value=100.0, step=0.01, key="add_amount")
        
        if st.form_submit_button("Add Money"):
            try:
                response = requests.post(
                    f"{BASE_URL}/wallet/add_money",
                    json={"user_id": add_user_id, "amount": amount},
                    headers={"Content-Type": "application/json"}
                )
                
                if response.status_code == 200:
                    st.success("Money added successfully!")
                    st.json(response.json())
                else:
                    st.error(f"Error: {response.json()}")
            except requests.exceptions.RequestException as e:
                st.error(f"Connection error: {e}")
    
    st.divider()
    
    # Hold Money Section
    st.subheader("Hold Money")
    with st.form("hold_money_form"):
        hold_user_id = st.number_input("User ID", min_value=1, value=1, step=1, key="hold_user_id")
        hold_amount = st.number_input("Amount", min_value=0.01, value=50.0, step=0.01, key="hold_amount")
        
        if st.form_submit_button("Hold Money"):
            try:
                response = requests.post(
                    f"{BASE_URL}/wallet/hold_money",
                    json={"user_id": hold_user_id, "amount": hold_amount},
                    headers={"Content-Type": "application/json"}
                )
                
                if response.status_code == 200:
                    st.success("Money held successfully!")
                    st.json(response.json())
                else:
                    st.error(f"Error: {response.json()}")
            except requests.exceptions.RequestException as e:
                st.error(f"Connection error: {e}")
    
    st.divider()
    
    # Release Holds Section
    st.subheader("Release Holds")
    if st.button("Release All Eligible Holds"):
        try:
            response = requests.post(f"{BASE_URL}/wallet/release_hold")
            
            if response.status_code == 200:
                st.success("Holds released successfully!")
                st.json(response.json())
            else:
                st.error(f"Error: {response.json()}")
        except requests.exceptions.RequestException as e:
            st.error(f"Connection error: {e}")
    
    st.divider()
    
    # Reverse Hold Section
    st.subheader("Reverse Hold")
    with st.form("reverse_hold_form"):
        reverse_user_id = st.number_input("User ID", min_value=1, value=1, step=1, key="reverse_user_id")
        hold_id = st.number_input("Hold ID", min_value=1, value=1, step=1, key="hold_id")
        
        if st.form_submit_button("Reverse Hold"):
            try:
                response = requests.post(
                    f"{BASE_URL}/wallet/reverse_hold",
                    json={"user_id": reverse_user_id, "hold_id": hold_id},
                    headers={"Content-Type": "application/json"}
                )
                
                if response.status_code == 200:
                    st.success("Hold reversed successfully!")
                    st.json(response.json())
                else:
                    st.error(f"Error: {response.json()}")
            except requests.exceptions.RequestException as e:
                st.error(f"Connection error: {e}")

elif page == "Reports":
    st.header("Reports")
    
    # Wallet Balance Report
    st.subheader("Wallet Balance Report")
    with st.form("balance_report_form"):
        balance_user_id = st.number_input("User ID", min_value=1, value=1, step=1, key="balance_user_id")
        
        if st.form_submit_button("Get Balance"):
            try:
                response = requests.get(
                    f"{BASE_URL}/report/wallet_balance",
                    json={"user_id": balance_user_id},
                    headers={"Content-Type": "application/json"}
                )
                
                if response.status_code == 200:
                    st.success("Balance fetched successfully!")
                    st.json(response.json())
                else:
                    st.error(f"Error: {response.json()}")
            except requests.exceptions.RequestException as e:
                st.error(f"Connection error: {e}")
    
    st.divider()
    
    # Hold Report
    st.subheader("Hold Report")
    with st.form("hold_report_form"):
        col1, col2 = st.columns(2)
        with col1:
            use_global_hold = st.checkbox("Get Global Report (All Users)", key="global_hold_check")
        with col2:
            hold_report_user_id = st.number_input("User ID", min_value=1, value=1, step=1, key="hold_report_user_id", disabled=use_global_hold)
        
        if st.form_submit_button("Get Hold Report"):
            try:
                if use_global_hold:
                    # Send empty JSON for global report
                    response = requests.get(
                        f"{BASE_URL}/report/hold_report",
                        json={},
                        headers={"Content-Type": "application/json"}
                    )
                else:
                    # Send user_id for specific user report
                    response = requests.get(
                        f"{BASE_URL}/report/hold_report",
                        json={"user_id": hold_report_user_id},
                        headers={"Content-Type": "application/json"}
                    )
                
                if response.status_code == 200:
                    st.success("Hold report fetched successfully!")
                    st.json(response.json())
                else:
                    st.error(f"Error: {response.json()}")
            except requests.exceptions.RequestException as e:
                st.error(f"Connection error: {e}")
    
    st.divider()
    
    # Wallet Operation Report
    st.subheader("Wallet Operation Report")
    with st.form("operation_report_form"):
        col1, col2 = st.columns(2)
        with col1:
            use_global_operation = st.checkbox("Get Global Report (All Users)", key="global_operation_check")
        with col2:
            operation_user_id = st.number_input("User ID", min_value=1, value=1, step=1, key="operation_user_id", disabled=use_global_operation)
        
        if st.form_submit_button("Get Operation Report"):
            try:
                if use_global_operation:
                    # Send empty JSON for global report
                    response = requests.get(
                        f"{BASE_URL}/report/wallet_operation_report",
                        json={},
                        headers={"Content-Type": "application/json"}
                    )
                else:
                    # Send user_id for specific user report
                    response = requests.get(
                        f"{BASE_URL}/report/wallet_operation_report",
                        json={"user_id": operation_user_id},
                        headers={"Content-Type": "application/json"}
                    )
                
                if response.status_code == 200:
                    st.success("Operation report fetched successfully!")
                    st.json(response.json())
                else:
                    st.error(f"Error: {response.json()}")
            except requests.exceptions.RequestException as e:
                st.error(f"Connection error: {e}")

# Footer
st.divider()
st.markdown("---")
st.markdown("*Wallet Service Admin Dashboard*")