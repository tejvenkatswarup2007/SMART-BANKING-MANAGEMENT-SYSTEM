# data_handler.py

import pandas as pd
import os

7
FILE = "accounts.csv"


def load_data():
    if not os.path.exists(FILE):
        df = pd.DataFrame(columns=["Name", "AccNo", "Pin", "Balance"])
        df.to_csv(FILE, index=False)
    return pd.read_csv(FILE)


def save_account(account):
    df = load_data()
    new_data = pd.DataFrame([[account.name, account.acc_no, account.pin,
                              account.balance]],
                            columns=df.columns)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(FILE, index=False)


def update_account(account):
    df = load_data()
    df.loc[df["AccNo"] == account.acc_no, "Balance"] = account.balance
    df.to_csv(FILE, index=False)


def authenticate(acc_no, pin):
    df = load_data()
    user = df[(df["AccNo"] == acc_no) & (df["Pin"] == pin)]
    if not user.empty:
        row = user.iloc[0]
        return row
    return None