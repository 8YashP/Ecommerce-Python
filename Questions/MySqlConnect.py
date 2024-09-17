import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
import numpy as np

db = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "Torque@120810",
    database = "ecomm"
)

# cur = db.cursor()