📦 Streamlit Inventory Management System README

---

## PROJECT OVERVIEW

A simple, user-friendly **Inventory Management System** built using **Streamlit** and **Pandas**. It allows you to track product stock, quantity, and value, with data persistently stored in a local CSV file.

---

## ✨ FEATURES

* **View Inventory:** Display a table of all current products.
* **Search & Filter:** Easily search the inventory by **Product Name** or **Category**.
* **Inventory Metrics:** Calculates and displays the **Total Items in Stock** and **Total Inventory Value** (in Rs.).
* **Add Product:** Quickly add new products with auto-generated unique Product IDs (e.g., P1, P2).
* **Update Product:** Modify details (Name, Category, Quantity, Price) of an existing product.
* **Delete Product:** Remove products from the inventory.
* **Persistent Storage:** All inventory data is saved to a local file (**inventory.csv**), ensuring data persists between sessions.

---

## 🛠️ INSTALLATION AND SETUP

### Prerequisites
You need **Python 3.x** installed on your system.

### Steps

1.  **Save the Code:**
    Save the provided Python code into a file named **`app.py`**.

2.  **Install Dependencies:**
    Open your terminal or command prompt and run the following command to install the required libraries:
    
    pip install streamlit pandas

---

## 🚀 USAGE

1.  **Run the Streamlit Application:**
    Navigate to the directory containing your **`app.py`** script and run:
    
    streamlit run app.py

2.  **Access the App:**
    Streamlit will automatically open the application in your default web browser, usually at **http://localhost:8501**.

3.  **Navigate the Menu:**
    Use the **Sidebar Menu** on the left side of the screen to choose between:
    * View Inventory
    * Add Product
    * Update Product
    * Delete Product

---

## 📁 KEY FILES

* **app.py:** The main Python script containing the Streamlit application logic.
* **inventory.csv:** (Created on first run) The CSV file used to store all inventory data persistently. **Do not delete this file if you want to keep your data.**

---
