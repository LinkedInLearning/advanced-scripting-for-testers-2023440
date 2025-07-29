import random
from datetime import datetime, timedelta

import openpyxl
from faker import Faker
from openpyxl.chart import BarChart, Reference

wb = openpyxl.Workbook()
worksheet = wb.active

headers = [
    "Username",
    "Email",
    "DateJoined",
    "LastLogin",
    "IsActive",
    "LoginCount",
    "loginAttempts",
]

worksheet.append(headers)

num_users = 50
for i in range(num_users):
    fake = Faker()
    username = fake.user_name()
    email = fake.email()
    date_joined = datetime.now() - timedelta(days=random.randint(1, 365))
    last_login = date_joined + timedelta(days=random.randint(0, 30))
    is_active = random.choice([True, False])
    login_count = random.randint(0, 500)
    login_attempts = round(login_count * (1 + random.random()))
    worksheet.append(
        [
            username,
            email,
            date_joined,
            last_login,
            is_active,
            login_count,
            login_attempts,
        ]
    )

chart = BarChart()
chart.title = "User Login Statistics"
chart.x_axis.title = "Users"
chart.y_axis.title = "Login Count"
data = Reference(
    worksheet,
    min_col=6,  # LoginCount column
    min_row=1,
    max_row=num_users + 1,
)
chart.add_data(data, titles_from_data=True)
worksheet.add_chart(chart, "K2")
file_path = "dummy_data.xlsx"
wb.save(file_path)
