import sqlite3
import pandas as pd

# Load the SQL data
conn = sqlite3.connect("retail.db")
df = pd.read_sql_query("SELECT * FROM retail_data", conn)  # replace with your table name

# Compute correlations
corr_returns = df['Net_Sales'].corr(df['Returns'])
corr_avg_basket = df['Net_Sales'].corr(df['Avg_Basket'])
corr_returns_basket = df['Returns'].corr(df['Avg_Basket'])

# Store correlations in a dict
correlations = {
    "Net_Sales-Returns": corr_returns,
    "Net_Sales-Avg_Basket": corr_avg_basket,
    "Returns-Avg_Basket": corr_returns_basket
}

# Determine strongest correlation
strongest = max(correlations.items(), key=lambda x: abs(x[1]))

# Output JSON structure
result = {
    "pair": strongest[0],
    "correlation": round(strongest[1], 4)
}

# Save to file
import json
with open("correlation-result.json", "w") as f:
    json.dump(result, f, indent=2)

print("✅ JSON generated:", result)
