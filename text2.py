import re

# Sample text from the provided content (Text 2)
text2 = """
CL>X CAPITAL
Facility
With insurance - INR 15,21,263 (Rupees Fifteen Lakh Twenty One thousand two hundred sixty three only)
Without insurance - INR 15,00,000 (Rupees fifteen lakh only)
Insurance premium ** - INR 21263 (Rupees Twenty One thousand two hundred sixty three only)
Purpose General business purposes/ working capital
Tenure 24 [months/years]
Frequency of Repayment Monthly
Interest Rate (Fixed) 22.58% per annum 22.50%
Instalment Due Date 2nd of every month
Default Rate 36% per annum
Instalment(s) INR 79296 (Rupees Seventy nine thousand two hundred ninety six only) payable as per the Repayment Schedule.
Processing fees (non-refundable) 2.25% on Loan Amount
Credit Admin Charges (CAC) 0.20% on Loan Amount
Dishonour Charges INR 1000 + Applicable Taxes, if any
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
    "Interest Rate (%)": r"Interest Rate\s*\(Fixed\)\s*(\d+\.\d+)%\s*.*?(\d+\.\d+)%",  # Handling fixed and alternative interest rates
    "Instalment Due Date": r"Instalment Due Date\s*(\d+\w+)",
    "Default Rate (%)": r"Default Rate\s*(\d+)%\s*\(.*?\)",
    "Instalment(s) INR": r"Instalment\(s\)\s*INR\s*([\d,]+)",
    "Processing fees (%)": r"Processing fees\s*\(non-refundable\)\s*(.*?)\s*\+.*",
    "Credit Admin Charges (%)": r"Credit Admin Charges\s*\(CAC\)\s*(.*?)\s*\+.*",
    "Dishonour Charges INR": r"Dishonour Charges\s*INR\s*([\d,]+)",
    "Prepayment Charges (%)": r"Prepayment Charges\s*<12 months\s*-\s*(.*?)\s*of.*"
}

# Dictionary to store extracted data
extracted_data_text2 = {}

# Extracting data using regex
for key, pattern in patterns.items():
    match = re.search(pattern, text2, re.IGNORECASE)
    if match:
        extracted_data_text2[key] = match.group(1).replace(',', '')  # Removing commas from numbers

# Output the extracted dictionary
print(extracted_data_text2)
