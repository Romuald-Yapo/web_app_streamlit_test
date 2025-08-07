import streamlit as st
import streamlit_authenticator as stauth

# --- Define users ---
users = {
    "usernames": {
        "admin": {
            "name": "Admin",
            "password": stauth.Hasher(["mypassword"]).generate()[0]
        }
    }
}

authenticator = stauth.Authenticate(
    users,
    "auth_cookie",
    "auth_key",
    cookie_expiry_days=1
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    st.success(f"Welcome {name}!")

    # Place app code here

elif authentication_status is False:
    st.error("Invalid credentials")

elif authentication_status is None:
    st.warning("Please enter your username and password")
