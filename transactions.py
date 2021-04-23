#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 18:59:26 2021

@author: tamires
"""

import pandas as pd
import matplotlib.pyplot as plt


transactions = pd.read_csv("transaction.csv", header=None, names=['Date', 'Transactions'])
transactions.drop(0)

transactions.head()
transactions.plot()
plt.show()