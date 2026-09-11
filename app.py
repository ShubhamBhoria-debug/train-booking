import json
import os
from datetime import datetime
import streamlit as st

DATA_FILE = "train_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    return data
        except Exception:
            pass
    return {"rect": [], "transaction": [], "stc": 0, "sct": 0}

def save_data():
    data = {
        "rect": st.session_state.rect,
        "transaction": st.session_state.transaction,
        "stc": st.session_state.stc,
        "sct": st.session_state.sct
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

saved_data = load_data()

if 'rect' not in st.session_state:
    st.session_state.rect = saved_data["rect"]
if 'transaction' not in st.session_state:
    st.session_state.transaction = saved_data["transaction"]
if 'stc' not in st.session_state:
    st.session_state.stc = saved_data["stc"]
if 'sct' not in st.session_state:
    st.session_state.sct = saved_data["sct"]

class Train:
    def __init__(self):
        pass

    def render(self):
        st.title("TICKET BOOKING CENTER")

        menu = st.sidebar.selectbox(
            "How would you like to proceed?",
            [
                "1. Want to reservation of a ticket",
                "2. Want to cancelation of a ticket",
                "3. Want to check history",
                "4. Want to check total reservation done by customer",
                "5. Want to check total cancelation done by customer",
                "6. Want to exit",
            ],
            key="main_menu_selectbox"
        )

        if menu.startswith("1"):
            self.reservation()
        elif menu.startswith("2"):
            self.cancelation()
        elif menu.startswith("3"):
            self.hst()
        elif menu.startswith("4"):
            self.total_reservation()
        elif menu.startswith("5"):
            self.total_cancelation()
        elif menu.startswith("6"):
            st.subheader("Exiting the server")
            st.info("You can close the tab")

    def total_reservation(self):
        st.subheader("Total Reservation Summary")
        st.metric(label="Total Reservation Today", value=st.session_state.stc)

    def total_cancelation(self):
        st.subheader("Total Cancelation Summary")
        st.metric(label="Total Cancelation Today", value=st.session_state.sct)

    def reservation(self):
        st.subheader("Ticket Reservation Portal")

        temp = st.number_input(
            "Enter how many tickets you want", min_value=1, step=1, max_value=10, key="num_tickets"
        )
        
        name_input = st.text_input("Enter your name:", key="res_name")
        train_input = st.text_input("Enter a train name from which you want to travel:", key="res_train")

        if st.button("Confirm Booking", key="confirm_booking_btn"):
            if name_input and train_input:
                rec = f"{name_input} and {train_input}"
                st.session_state.rect.append(rec)
                st.session_state.stc += 1

                current_time = datetime.now().strftime("%d-%m-%y %H:%M:%S")
                record = f"{current_time} - {name_input} booked {train_input}"
                st.session_state.transaction.append(record)

                save_data()

                st.success(f"Successfully booked ticket for {name_input} on {train_input}")
            else:
                st.warning("Please fill out both customer name and train name.")

    def cancelation(self):
        st.subheader("Ticket Cancelation Portal")
        if st.button("Cancel Last Booking", key="cancel_booking_btn"):
            if st.session_state.rect:
                cancel_tct = st.session_state.rect.pop()
                st.session_state.sct += 1

                save_data()

                st.success(f"Your last booking was cancelled successfully: {cancel_tct}")

                current_time = datetime.now().strftime("%d-%m-%y %H:%M:%S")
                record = f"{current_time} - Canceled {cancel_tct}"
                st.session_state.transaction.append(record)
                save_data()
            else:
                st.info("No Active Booking to cancel!")

    def hst(self):
        st.subheader("Transaction History")
        if not st.session_state.transaction:
            st.info("No bookings held in the past few days.")
        else:
            re = st.session_state.transaction[-10:]
            for tx in re:
                st.write(tx)

rt = Train()
rt.render()