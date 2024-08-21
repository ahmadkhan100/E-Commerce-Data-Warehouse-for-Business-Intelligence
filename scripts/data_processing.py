import pandas as pd
import psycopg2

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="ecommerce_db",
            user="your_username",
            password="your_password",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def load_data():
    conn = connect_to_db()
    if conn:
        query = """
        SELECT * FROM ecommerce.orders o
        JOIN ecommerce.order_items oi ON o.order_id = oi.order_id
        JOIN ecommerce.products p ON oi.product_id = p.product_id;
        """
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    else:
        return None

def process_data(df):
    # Example processing: Calculate total sales per product
    sales_per_product = df.groupby('product_name')['price'].sum().reset_index()
    return sales_per_product

if __name__ == "__main__":
    data = load_data()
    if data is not None:
        processed_data = process_data(data)
        print(processed_data)
    else:
        print("No data to process.")
