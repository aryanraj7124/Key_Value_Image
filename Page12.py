# import re
# import json

# # Sample text input
# text = """
# CL>X
# CAPITAL
# End Use Letter
# Dated: 26/08/2024
# To,
# Clix Capital Services Pvt. Ltd
# 6th Floor, Good Earth Business Bay-2,
# Sector - 58, Gurugram, Haryana 122102
# Sub :- Application for Loan of Rs. 15,21,263 For working Capital
# ( end.use )
# I, SHYAM ENTERPRISES refer to the Application No: DSA3BL22705424 dated 02/08/2024 submitted by me to Clix Capital
# for the availing for Loan Against Property / Business Loan from Clix Capital
# As Stated in the said application form, the said loan is for the purpose of Working Capital
# I hereby represent, warrant and confirm that the aforesaid purpose is a valid purpose and is not speculative or illegal in any manner I further
# agree, confirm and undertake that the purpose of use of funds under the loan shall not be
# changed in any manner during the tenor of the Loan; or that such change in purpose shall take place
# only with the prior written permission of Clix Capital.
# Regards,
# 5
# For SHYAM ENTERPRISES
# SIGNED BY THE BORROWER
# SIGNED BY THE CO-BORROWER
# SIGNED FOR AND ON BEHALF OF
# 5
# 12418
# 5
# LENDER
# Prop
# """

# # Define regex patterns to match specific information
# date_pattern = r"Dated:\s*([\d/]+)"
# loan_amount_pattern = r"Loan of Rs\.\s*([\d,]+)"
# purpose_pattern = r"For\s+([\w\s]+)"
# applicant_name_pattern = r"I,\s*([\w\s]+)\s+refer to the Application"
# application_no_pattern = r"Application No:\s*(\w+)"
# application_date_pattern = r"dated\s*([\d/]+)"

# # Extract information using regex
# date = re.search(date_pattern, text).group(1) if re.search(date_pattern, text) else None
# loan_amount = re.search(loan_amount_pattern, text).group(1) if re.search(loan_amount_pattern, text) else None
# purpose = re.search(purpose_pattern, text).group(1) if re.search(purpose_pattern, text) else None
# applicant_name = re.search(applicant_name_pattern, text).group(1) if re.search(applicant_name_pattern, text) else None
# application_no = re.search(application_no_pattern, text).group(1) if re.search(application_no_pattern, text) else None
# application_date = re.search(application_date_pattern, text).group(1) if re.search(application_date_pattern, text) else None

# # Create a dictionary for JSON output
# output_data = {
#     "Dated": date,
#     "Loan Amount": loan_amount,
#     "Purpose": purpose,
#     "Applicant Name": applicant_name,
#     "Application Number": application_no,
#     "Application Date": application_date
# }

# # Convert dictionary to JSON
# json_output = json.dumps(output_data, indent=4)
# print(json_output)

import re
import json

def parse_end_use_letter(text):
    # Define regex patterns for extracting information
    date_pattern = r"Dated[:\s]*([\d/]+)"
    company_pattern = r"For\sLALAJI\s&\sCOMPANY"
    application_no_pattern = r"Application No[:\s]*([\w\d-]+)"
    loan_amount_pattern = r"Loan of Rs\.\s?([\d,]+)"
    purpose_pattern = r"the said loan is for the purpose of\s([\w\s]+)"
    
    # Use regex to find matches in the text
    date_match = re.search(date_pattern, text)
    company_match = re.search(company_pattern, text)
    application_no_match = re.search(application_no_pattern, text)
    loan_amount_match = re.search(loan_amount_pattern, text)
    purpose_match = re.search(purpose_pattern, text)
    
    # Extracting the values if the pattern matched
    date = date_match.group(1) if date_match else None
    company = "Lalaji & Company" if company_match else None
    application_no = application_no_match.group(1) if application_no_match else None
    loan_amount = loan_amount_match.group(1).replace(",", "") if loan_amount_match else None
    purpose = purpose_match.group(1).strip() if purpose_match else None

    # Create a dictionary to store the parsed information
    result = {
        "Date": date,
        "Company": company,
        "Application Number": application_no,
        "Loan Amount": loan_amount,
        "Purpose": purpose
    }
    
    # Return the result as a JSON object
    return json.dumps(result, indent=4)

# Example text input
text = """
CL>X
CAPITAL
End Use Letter
Dated: 24/8/24
To,
Clix Capital Services Pvt. Ltd
6th Floor, Good Earth Business Bay-2,
Sector - 58, Gurugram, Haryana 122102
Sub : - Application for Loan of Rs. 8,10,744 For Working Capital
.... ( end use )
Lalaji & Company
,24
refer to the Application No DSA3BL25088 dat
d 24/8/24
for the availing for Loan Against Property / Business Loan from Clix Capital
.. submitted by me to Clix Capital
As Stated in the said application form, the said loan is for the purpose of .
Working Capital
i hereby represent, warrant and confirm that the aforesaid purpose is a valid purpose and is not speculative or illegal in any manner I further
agree, confirm and undertake that the purpose of use of funds under the loan shall not be
changed in any manner during the tenor of the Loan; or that such change in purpose shall take place
only with the prior written permission of Clix Capital.
Regards,
For LALAJI & COMPANY
SIGNED BY THE BORROWER
SIGNED BY THE CO-BORROWER
--- --
SIGNED FOR AND ON BEHALF OF
Sonig.
LENDER
Proprietor
Soning
"""

# Parse the text
result = parse_end_use_letter(text)

# Print the result
print(result)



