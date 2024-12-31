import re

# Sample text from the provided content
text = """
Facility
With insurance - INR 151449 (Rupees fifteen lakh fourteen Thousand four Hundred forty Nine only)
Without insurance - INR 15,00,000 (Rupees fifteen Lakh only)
Insurance premium ** - INR 14449 (Rupees fourteen Thousand four Hundred forty Nine only)
Purpose General business purposes/ working capital
Tenure 36 [months/years]
Frequency of Repayment Monthly
Interest Rate 19%( Nineteen Percent per annum)
Instalment Due Date 2nd of every month
Default Rate 36% (Thirty Six) per annum
Instalment(s) INR 55514 (Rupees Fifty five Thousand five Hundred fourteen only)
Processing fees (non-refundable) 2% + GST on loan Amount
Credit Admin Charges 0.20%+EST on loan Amount
Dishonour Charges INR 1000 + Applicable Taxes
Prepayment Charges <12 months - 6% of future principal outstanding
"""

# Regex patterns for key-value pairs
patterns = {
    "Facility (With insurance) INR": r"With insurance\s*-\s*INR\s*([\d,]+)",
    "Facility (Without insurance) INR": r"Without insurance\s*-\s*INR\s*([\d,]+)",
    "Insurance premium INR": r"Insurance premium\s*\*\*\s*-\s*INR\s*([\d,]+)",
    "Purpose": r"Purpose\s*(.*?)(?:\n|$)",
    "Tenure (months)": r"Tenure\s*(\d+)\s*\[.*?\]",
    "Frequency of Repayment": r"Frequency of Repayment\s*(\w+)",
    "Interest Rate (%)": r"Interest Rate\s*(\d+)%\s*\(.*?\)",
    "Instalment Due Date": r"Instalment Due Date\s*(\d+\w+)",
    "Default Rate (%)": r"Default Rate\s*(\d+)%\s*\(.*?\)",
    "Instalment(s) INR": r"Instalment\(s\)\s*INR\s*([\d,]+)",
    "Processing fees (%)": r"Processing fees\s*\(non-refundable\)\s*(.*?)\s*\+.*",
    "Credit Admin Charges (%)": r"Credit Admin Charges\s*(.*?)\s*\+.*",
    "Dishonour Charges INR": r"Dishonour Charges\s*INR\s*([\d,]+)",
    "Prepayment Charges (%)": r"Prepayment Charges\s*<12 months\s*-\s*(.*?)\s*of.*"
}

# Dictionary to store extracted data
extracted_data = {}

# Extracting data using regex
for key, pattern in patterns.items():
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        extracted_data[key] = match.group(1).replace(',', '')  # Removing commas from numbers

# Output the extracted dictionary
print(extracted_data)
