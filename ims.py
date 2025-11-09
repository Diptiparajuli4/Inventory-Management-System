import streamlit as st
import pandas as pd
import os

# File to store inventory data
INVENTORY_FILE = "inventory.csv"

# Load inventory from CSV
def load_inventory():
    if os.path.exists(INVENTORY_FILE):
        df = pd.read_csv(INVENTORY_FILE)
        df = df.fillna({"ID": "", "Name": "", "Category": "", "Quantity": 0, "Price": 0.0})
        df["ID"] = df["ID"].astype(str)
        return df
    else:
        return pd.DataFrame(columns=["ID", "Name", "Category", "Quantity", "Price"])

# Save inventory to CSV
def save_inventory(inventory_df):
    inventory_df.to_csv(INVENTORY_FILE, index=False)

# Generate unique product ID
def generate_product_id(inventory_df):
    if inventory_df.empty:
        return "P1"
    else:
        ids = inventory_df["ID"].astype(str).str.extract(r'(\d+)')
        ids = ids.dropna().astype(int)
        if ids.empty:
            return "P1"
        last_num = ids.max()[0]
        return f"P{last_num + 1}"

# Streamlit App
def main():
    st.set_page_config(page_title="Inventory Management", page_icon="📦", layout="centered")
    st.title("📦 Inventory Management System")

    inventory_df = load_inventory()

    # Sidebar Menu
    menu = ["View Inventory", "Add Product", "Update Product", "Delete Product"]
    choice = st.sidebar.radio("Menu", menu)

    # 1. View Inventory
    if choice == "View Inventory":
        st.subheader("Current Inventory")
        if inventory_df.empty:
            st.warning("⚠️ Inventory is empty!")
        else:
            search_term = st.text_input("🔍 Search by Name or Category").strip().lower()
            if search_term:
                filtered_df = inventory_df[
                    inventory_df["Name"].str.lower().str.contains(search_term) |
                    inventory_df["Category"].str.lower().str.contains(search_term)
                ]
            else:
                filtered_df = inventory_df

            if filtered_df.empty:
                st.warning("⚠️ No products match your search!")
            else:
                filtered_df["Total Value"] = filtered_df["Quantity"] * filtered_df["Price"]
                st.dataframe(filtered_df)
                total_items = filtered_df["Quantity"].sum()
                total_value = filtered_df["Total Value"].sum()
                st.info(f"📦 Total Items in Stock: **{total_items}**")
                st.info(f"💰 Total Inventory Value: **Rs.{total_value:.2f}**")

    # 2. Add Product
    elif choice == "Add Product":
        st.subheader("Add New Product")
        with st.form("add_form"):
            product_id = generate_product_id(inventory_df)
            st.text_input("Product ID (Auto)", value=product_id, disabled=True)
            name = st.text_input("Enter product name")
            category = st.text_input("Enter product category")
            quantity = st.number_input("Enter quantity", min_value=0, step=1)
            price = st.number_input("Enter price", min_value=0.0, format="%.2f")
            submit = st.form_submit_button("Add Product")

        if submit:
            new_product = {"ID": product_id, "Name": name, "Category": category, "Quantity": quantity, "Price": price}
            inventory_df = pd.concat([inventory_df, pd.DataFrame([new_product])], ignore_index=True)
            save_inventory(inventory_df)
            st.success(f"✅ Product **{name}** added successfully!")

    # 3. Update Product
    elif choice == "Update Product":
        st.subheader("Update Product")
        if inventory_df.empty:
            st.warning("⚠️ No products to update.")
        else:
            product_id = st.selectbox("Select Product ID", inventory_df["ID"].tolist())
            product_row = inventory_df[inventory_df["ID"] == product_id]

            if not product_row.empty:
                product = product_row.iloc[0]
                new_name = st.text_input("Update product name", value=product["Name"])
                new_category = st.text_input("Update category", value=product["Category"])
                new_qty = st.number_input("Enter new quantity", min_value=0, step=1, value=int(product["Quantity"]))
                new_price = st.number_input("Enter new price", min_value=0.0, format="%.2f", value=float(product["Price"]))

                if st.button("Update"):
                    inventory_df.loc[inventory_df["ID"] == product_id, ["Name", "Category", "Quantity", "Price"]] = [
                        new_name, new_category, new_qty, new_price
                    ]
                    save_inventory(inventory_df)
                    st.success(f"✅ Product **{new_name}** updated successfully!")
            else:
                st.error("❌ Product not found!")

    # 4. Delete Product
    elif choice == "Delete Product":
        st.subheader("Delete Product")
        if inventory_df.empty:
            st.warning("⚠️ No products to delete.")
        else:
            product_id = st.selectbox("Select Product ID to delete", inventory_df["ID"].tolist())
            product_row = inventory_df[inventory_df["ID"] == product_id]

            if not product_row.empty:
                product_name = product_row["Name"].values[0]
                if st.button("Delete"):
                    inventory_df = inventory_df[inventory_df["ID"] != product_id]
                    save_inventory(inventory_df)
                    st.success(f"🗑️ Product **{product_name}** deleted successfully!")
            else:
                st.error("❌ Product not found!")

if __name__ == "__main__":
    main()
