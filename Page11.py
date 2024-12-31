import re
import json

# Input text (your raw input)
input_text = """
CLXX
CAPITAL
SCHEDULE
FORM OF UTILISATION REQUEST
Dated: 09/09/24
From:
Universal Dyes & Intermediates
Plot No 136 GIDC Estate
Nandesari Vadodara - 391340
PARTNER
To:
Clix Capital Services Private Limited
Dear Sirs,
Sub: Facility Agreement dated
09/09/24 (the "Facility Agreement")
-
SS
1.
We refer to the Facility Agreement. This is a utilisation request made pursuant to the Facility Agreement. Terms defined in the Facility
Agreement shall have the same meaning in this utilisation request.
2.
We confirm that, at the date hereof, the representations set out in the Facility Agreement are true and correct and no Event of Default
has
occurred.
3.
We confirm that the proceeds of this Facility will be used for our business purpose.
UNIVERSAL DÕES AND INTERMEDIATES
4.
The proceeds of this Facility should be credited to the following Bank Account.
DISBURSEMENT REQUEST THROUGH RTGS/ NEFT
PARTICULARS
DETAILS
Loan Amount
1514449
Insurance Amount to be deducted fore Loan
ICICI - 8160
Amount and citta 'CIC! Prudential
oCARE Insurance ICICI Lombard ***
care - 6289
"Strike whichever .s not applicable
Disbursal Amount
Account Holder Name
Universal Dyes & Intermediates
----
Bank Namne
IDFC First Bank
Bank Address
Vadodara
Bank Account No:
10056867746
Bank Account Type
CA
YES AND INTERMEDIATES
SS
IFSC Code
IDFB0042381
Borrower E-Mail Address'
udidyes123@gmail.com
Borrower(s)
UNIVERSAL DYESAN
.By
Name
By
Name
UNIVERSIANER EY THE BORROWERATES
SIGNED BY THE CO-BORROWER
SIGNED FOR AND ON BEHALF OF
S.S.
SI
LENDER
PROUT
52 A
PARTNER
53
"""

# Define regex patterns to extract relevant data correctly
form_info_pattern = r'FORM OF UTILISATION REQUEST\s*Dated:\s*(.*)\nFrom:\s*(.*)\nPlot No\s*(.*)\nTo:\s*(.*)'
loan_info_pattern = r'Loan Amount\s*(\d+)\nInsurance Amount to be deducted fore Loan\s*(.*)\n.*\nCARE Insurance ICICI Lombard.*care\s*-\s*(\d+)'
bank_info_pattern = r'Account Holder Name\s*(.*)\nBank Namne\s*(.*)\nBank Address\s*(.*)\nBank Account No:\s*(\d+)\nBank Account Type\s*(.*)\nIFSC Code\s*(.*)\nBorrower E-Mail Address\s*(.*)'

# Extract the relevant parts using regex
form_info_match = re.search(form_info_pattern, input_text, flags=re.DOTALL)
loan_info_match = re.search(loan_info_pattern, input_text, flags=re.DOTALL)
bank_info_match = re.search(bank_info_pattern, input_text, flags=re.DOTALL)

# Check and organize the extracted data into a dictionary
output_data = {
    "Form of Utilisation Request Dated": form_info_match.group(1).strip() if form_info_match else "",
    "From": form_info_match.group(2).strip() if form_info_match else "",
    "Plot No": form_info_match.group(3).strip() if form_info_match else "",
    "To": form_info_match.group(4).strip() if form_info_match else "",
    "Loan Details": {
        "Loan Amount": loan_info_match.group(1).strip() if loan_info_match else "",
        "Insurance Amount to be deducted for Loan": loan_info_match.group(2).strip() if loan_info_match else "",
        "CARE Insurance ICICI Lombard": loan_info_match.group(3).strip() if loan_info_match else ""
    },
    "Bank Details": {
        "Account Holder Name": bank_info_match.group(1).strip() if bank_info_match else "",
        "Bank Name": bank_info_match.group(2).strip() if bank_info_match else "",
        "Bank Address": bank_info_match.group(3).strip() if bank_info_match else "",
        "Bank Account No": bank_info_match.group(4).strip() if bank_info_match else "",
        "Bank Account Type": bank_info_match.group(5).strip() if bank_info_match else "",
        "IFSC Code": bank_info_match.group(6).strip() if bank_info_match else "",
        "Borrower E-Mail Address": bank_info_match.group(7).strip() if bank_info_match else ""
    }
}

# Print the final structured JSON output
print(json.dumps(output_data, indent=4))
