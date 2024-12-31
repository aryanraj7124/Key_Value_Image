import re
import json

def format_number(num_str):
    """Format a number string with commas."""
    return '{:,}'.format(int(num_str.replace(',', '').strip()))

def extract_key_value_pairs(text):
    # Define regex patterns for key-value extraction
    patterns = {
        "Facility (With insurance) INR": r"With insurance\s*-\s*INR\s*([\d,]+)",
        "Facility (Without insurance) INR": r"Without insurance\s*-\s*INR\s*([\d,]+)",
        "Insurance premium INR": r"Insurance premium\s*-\s*INR\s*([\d,]+)",
        "Purpose": r"Purpose\s*([^\n]+)",
        "Frequency of Repayment": r"Frequency\s*of\s*([^\n]+)",
        "Interest Rate (%)": r"Interest Rate\s*\(Fixed\)\s*([\d]+)%",
        "Instalment Due Date": r"Instalment Due Date\s*([^\n]+)",
        "Default Rate (%)": r"Default Rate\s*(\d+)%",  
        "Instalment(s) INR": r"Instalment\(s\)\s*INR\s*([\d,]+)",
        "Processing fees (%)": r"Processing fees\s*\(non-refundable\)\s*INR\s*([\d\.]+)%?\s*\+gst",  
        "Credit Admin Charges (%)": r"Credit Admin Charges\s*INR\s*([\d\.]+)%?\s*\+EST",  
        "Dishonour Charges INR": r"Dishonour Charges\/Cheque Bounce\/NACH return charge\s*INR\s*([\d,]+)",
        "Prepayment Charges (%)": r"<12 months\s*-\s*(\d+)% of future principal outstanding"
    }

    # Dictionary to store extracted data
    extracted_data = {}

    # Extracting data using regex
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            extracted_value = match.group(1)
            if key in ["Facility (With insurance) INR", "Facility (Without insurance) INR", "Instalment(s) INR", "Dishonour Charges INR"]:
                extracted_value = format_number(extracted_value)  # Format with commas
            else:
                extracted_value = extracted_value.replace(',', '').strip()
            extracted_data[key] = extracted_value

    return extracted_data

# Input text
text = """
CLXX
CAPITAL
4.
Facility
With insurance - INR 151449 (Rupees fifteen lakh fourteen
Thousand four Hundred forty Nine only)
Without insurance - INR 1500000 Rupees fifteen Lakh only
Insurance premium ** - INR 14449 (Rupees fourteen Thousand four Hundred forty Nine only)
5.
Purpose
General business purposes/ working capital
6.
Tenure (tick whichever
361
[months/ years]
is applicable)
UNIVERSAL DYES AND INTERMEDIATES
7.
Frequency
of
Monthly
Repayment
19%( Nineteen per annum Percent Interest Rate (Fixed)
Instalment Due Date
2nd of every month
PARTNER
Percent
36% (Thirty Six) per annum
10.
Default Rate
11.
Instalment(s)
INR 55514 (Rupees Fifty five Thousand five Hundred fourteen only) payable as per the Repayment Schedule.
The estimated aggregate Instalments for the tenure of the Facility shall be INR
(Rupees only).
12.
Processing fees (non-
INR
(Rupees 2%- TEST on loan Amount UNIVERSAL DYES AND INTERMEDIATES refundable)
only)
Credit Admin Charges INR (Rupees 0.20%+EST on loan Amount PARTNER (CAC) only)
Dishonour Charges INR 1000 + Applicable Taxes, if any
Cheque Bounce/ NACH return charge
15.
Prepayment Charges
<12 months - 6% of future principal outstanding
12 months to less than 24 months - 5% of future principal outstanding
Prepayment is permissible only after expiry of 3 (three) months from the date of disbursal.
UNIVERSAL DYES AND INTERMEDIATES
"""

# Extract data
extracted_data = extract_key_value_pairs(text)

# Convert to JSON format
json_output = json.dumps(extracted_data, indent=4)

# Print the extracted data in JSON format
print(json_output)
