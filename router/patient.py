'''import sqlite3
from datetime import date

conn = sqlite3.connect("clinic.db")
cursor = conn.cursor()

# Tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS patient(
patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
patient_name TEXT,
phone TEXT,
address TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS service(
service_id INTEGER PRIMARY KEY AUTOINCREMENT,
service_name TEXT,
price REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales(
sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
patient_id INTEGER,
sale_date TEXT,
total_amount REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales_items(
item_id INTEGER PRIMARY KEY AUTOINCREMENT,
sale_id INTEGER,
service_id INTEGER,
price REAL
)
""")

conn.commit()

# -------------------------
# ADD PATIENT
# -------------------------

name = input("Enter patient name: ")
phone = input("Enter phone: ")
address = input("Enter address: ")

cursor.execute(
"INSERT INTO patient (patient_name,phone,address) VALUES (?,?,?)",
(name,phone,address)
)

patient_id = cursor.lastrowid

# -------------------------
# CREATE BILL
# -------------------------

cursor.execute(
"INSERT INTO sales (patient_id,sale_date,total_amount) VALUES (?,?,?)",
(patient_id,str(date.today()),0)
)

sale_id = cursor.lastrowid
conn.commit()

total_bill = 0

# -------------------------
# ADD SERVICES
# -------------------------

while True:

    print("\n1. Dental Cleaning - ₹500")
    print("2. Tooth Extraction - ₹1000")
    print("3. Root Canal - ₹2000")

    cursor.execute("SELECT * FROM service")
    services = cursor.fetchall()

    for s in services:
        print(s[0], s[1], "₹", s[2])

    service_id = int(input("\nEnter service id: "))

    cursor.execute(
    "SELECT service_name,price FROM service WHERE service_id=?",
    (service_id,)
    )

    service = cursor.fetchone()

    service_name = service[0]
    price = service[1]

    cursor.execute(
    "INSERT INTO sales_items (sale_id,service_id,price) VALUES (?,?,?)",
    (sale_id,service_id,price)
    )

    total_bill += price

    print(service_name, "added to bill")

    more = input("Add another service? (y/n): ")

    if more.lower() != "y":
        break

conn.commit()

# update total bill
cursor.execute(
"UPDATE sales SET total_amount=? WHERE sale_id=?",
(total_bill,sale_id)
)

conn.commit()

# -------------------------
# PRINT BILL
# -------------------------

print("\n------ BILL ------")
print("Patient:", name)
print("Date:", date.today())

cursor.execute("""
SELECT se.service_name,si.price
FROM sales_items si
JOIN service se ON si.service_id = se.service_id
WHERE si.sale_id=?
""",(sale_id,))

rows = cursor.fetchall()

for r in rows:
    print(r[0], "= ₹", r[1])

print("\nTotal Bill: ₹", total_bill)

conn.close()'''