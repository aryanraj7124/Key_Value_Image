
import re
import json

# Text 3 from the provided content
text3 = """
CLXX CAPITAL
Facility
With insurance - INR 151449 (Rupees fifteen lakh fourteen Thousand four Hundred forty Nine only)
Without insurance - INR 15,00,000 (Rupees fifteen Lakh only)
Insurance premium ** - INR 14449 (Rupees fourteen Thousand four Hundred forty Nine only)
Purpose General business purposes/ working capital
Tenure (tick whichever 361 [months/ years] is applicable)
Frequency of Repayment Monthly
Interest Rate (Fixed) 19% (Nineteen Percent per annum)
Instalment Due Date 2nd of every month
Default Rate 36% (Thirty Six Percent per annum)
Instalment(s) INR 55514 (Rupees Fifty five Thousand five Hundred fourteen only) payable as per the Repayment Schedule.
Processing fees (non-refundable) 2%- TEST on loan Amount
Credit Admin Charges (CAC) 0.20%+EST on loan Amount
Dishonour Charges INR 1000 + Applicable Taxes, if any
Prepayment Charges <12 months - 6% of future principal outstanding
12 months to less than 24 months - 5% of future principal outstanding
24 months to less than 48 months - 4% of future principal outstanding
"""

# Regex patterns for key-value pairs
patterns = {
    "Facility (With insurance) INR": r"With insurance\s*-\s*INR\s*([\d,]+)",
    "Facility (Without insurance) INR": r"Without insurance\s*-\s*INR\s*([\d,]+)",
    "Insurance premium INR": r"Insurance premium\s*\*\*\s*-\s*INR\s*([\d,]+)",
    "Purpose": r"Purpose\s*(.*?)(?:\n|$)",
    "Tenure (months)": r"Tenure\s*\(.*?\)\s*(\d+)\s*\[.*?\]",
    "Frequency of Repayment": r"Frequency of Repayment\s*(\w+)",
    "Interest Rate (%)": r"Interest Rate\s*\(Fixed\)\s*(\d+)%\s*\(.*?\)",
    "Instalment Due Date": r"Instalment Due Date\s*(\d+\w+)",
    "Default Rate (%)": r"Default Rate\s*(\d+)%\s*\(.*?\)",
    "Instalment(s) INR": r"Instalment\(s\)\s*INR\s*([\d,]+)",
    "Processing fees (%)": r"Processing fees\s*\(non-refundable\)\s*(.*?)\s*\+.*",
    "Credit Admin Charges (%)": r"Credit Admin Charges\s*\(CAC\)\s*(.*?)\s*\+.*",
    "Dishonour Charges INR": r"Dishonour Charges\s*INR\s*([\d,]+)",
    "Prepayment Charges (%)": r"Prepayment Charges\s*<12 months\s*-\s*(.*?)\s*of.*"
}

# Dictionary to store extracted data
extracted_data_text3 = {}

# Extracting data using regex
for key, pattern in patterns.items():
    match = re.search(pattern, text3, re.IGNORECASE)
    if match:
        extracted_data_text3[key] = match.group(1).replace(',', '')  # Removing commas from numbers

# Convert the extracted data to JSON format
json_data_text3 = json.dumps(extracted_data_text3, indent=4)

# Output the JSON formatted data
print(json_data_text3)
