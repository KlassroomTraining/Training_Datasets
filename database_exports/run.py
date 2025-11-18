import pandas as pd

# 🔹 Replace with your Excel file path
excel_file = r"C:\Users\user\Desktop\Jemit\Practicals\telecom_ml_project\data\database_exports\telecom_db_tables.xlsx"

def list_sheet_names(file_path):
    try:
        # Using pandas ExcelFile object
        xls = pd.ExcelFile(file_path)
        print(f"\n📘 File: {file_path}")
        print("📄 Sheet names found:\n")
        for sheet in xls.sheet_names:
            print(f"✅ {sheet}")
    except Exception as e:
        print(f"⚠️ Error reading {file_path}: {e}")

if __name__ == "__main__":
    list_sheet_names(excel_file)
