import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Expense Tracker Dashboard")

uploaded_file = st.file_uploader("Upload Expense CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Expense Data")
    st.write(df)

    total = df["Amount"].sum()
    st.success(f"Total Expenses: ₹{total}")

    category_expense = df.groupby("Category")["Amount"].sum()

    st.subheader("Expense Distribution")

    fig, ax = plt.subplots()
    category_expense.plot(kind="pie", autopct="%1.1f%%", ax=ax)
    ax.set_ylabel("")
    st.pyplot(fig)

    st.subheader("Expenses by Category")

    fig2, ax2 = plt.subplots()
    category_expense.plot(kind="bar", ax=ax2)
    st.pyplot(fig2)

    budget = 2000

    if total > budget:
        st.error("Budget Exceeded!")
    else:
        st.success("Within Budget")