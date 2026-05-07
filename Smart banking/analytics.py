import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def show_graph():
    df = pd.read_csv("accounts.csv")

    if df.empty:
        print("No data to display")
        return

    balances = df["Balance"].values
    acc_numbers = df["AccNo"].values




    x = np.arange(len(acc_numbers))

    plt.bar(x, balances)
    plt.xticks(x, acc_numbers)
    plt.xlabel("Account Number")
    plt.ylabel("Balance")
    plt.title("Bank Account Balances")
    plt.show()