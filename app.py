import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Expense Tracker Pro",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Expense Tracker Pro")
st.markdown("Track expenses and monitor your budget")

budget = st.sidebar.number_input(
    "Set Monthly Budget (₹)",
    min_value=1000,
    value=5000,
    step=500
)

uploaded_file = st.file_uploader(
    "Upload Expense CSV",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    total_expense = df["Amount"].sum()
    remaining = budget - total_expense

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Expense", f"₹{total_expense}")
    col2.metric("Budget", f"₹{budget}")
    col3.metric("Remaining", f"₹{remaining}")

    st.subheader("📋 Expense Records")
    st.dataframe(df, use_container_width=True)

    category_expense = df.groupby("Category")["Amount"].sum()

    col4, col5 = st.columns(2)

    with col4:
        st.subheader("🥧 Expense Distribution")

        fig1, ax1 = plt.subplots()
        category_expense.plot(
            kind="pie",
            autopct="%1.1f%%",
            ax=ax1
        )
        ax1.set_ylabel("")
        st.pyplot(fig1)

    with col5:
        st.subheader("📊 Category Comparison")

        fig2, ax2 = plt.subplots()
        category_expense.plot(
            kind="bar",
            ax=ax2
        )
        st.pyplot(fig2)

    if total_expense > budget:
        st.error("⚠️ Budget Exceeded!")
    else:
        st.success("✅ You are within budget")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download Expense Report",
        csv,
        "expense_report.csv",
        "text/csv"
    )
