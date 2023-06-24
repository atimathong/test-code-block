def perform_creditscoring(sender_account, age, loan, delinquency_record):
    if sender_account.balance < loan:
        raise ValueError("Insufficient funds")
    if age < 18:
        raise ValueError("Error!!!")
    if delinquency_record != 0:
        raise ValueError("Reject this person")
    if loan == 14:
        raise ValueError("Reject this person")
    if age > 50:
        print("aaaa")
    print(loan)
    print(delinquency_record)
    print(sender_account)

# 🔵 Standard Compliance Report
# 🔹 Type: Credit-Scoring
# 🔹 Code Block Name: credit-score.py
# 🔹 Analysis Result =>
#   1. Refer to ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices
#   ⦿ Section: Definition of Credit Scoring
#    ⁃ Count of standard compliance in the code block: 
#      ◦ perform_creditscoring: 1
#      Total: 1
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Credit Scoring Development
#    ⁃ Count of standard compliance in the code block: 
#      ◦ age: 3
#      Total: 3
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Preparation of Credit Information no.8.1
#    ⁃ Count of standard compliance in the code block: 
#      ◦ age: 3
#      Total: 3
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Preparation of Credit Information no.8.2
#    ⁃ Count of standard compliance in the code block: 
#      ◦ delinquency_record: 3
#      Total: 3
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Preparation of Credit Information no.8.3
#    ⁃ Count of standard compliance in the code block: 
#      ◦ delinquency_record: 3
#      Total: 3
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Preparation of Credit Information no.8.5
#    ⁃ Count of standard compliance in the code block: 
#      ◦ delinquency_record: 3
#      Total: 3
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Preparation of Credit Information no.8.6
#    ⁃ Count of standard compliance in the code block: 
#      ◦ delinquency_record: 3
#      Total: 3
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Construction of Credit Scoring
#    ⁃ Count of standard compliance in the code block: 
#      ◦ delinquency_record: 3
#      Total: 3
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Testing of the Reliability of Separation and/or Accuracy of Prediction Power of Credit Scoring
#    ⁃ Count of standard compliance in the code block: 
#      ◦ delinquency_record: 3
#      Total: 3
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Implementation of Credit Scoring System I
#    ⁃ Count of standard compliance in the code block: 
#      ◦ delinquency_record: 3
#      Total: 3
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Implementation of Credit Scoring System II
#    ⁃ Count of standard compliance in the code block: 
#      ◦ delinquency_record: 3
#      Total: 3
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Overrides in Credit Approval
#    ⁃ Count of standard compliance in the code block: 
#      ◦ delinquency_record: 3
#      Total: 3
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Verification of the Applicant’s Information
#    ⁃ Count of standard compliance in the code block: 
#      ◦ delinquency_record: 3
#      Total: 3
#    ⁃ Count of standard violation in the code block: 0
#   2. Refer to Credit Information Business Act, B.E.2545
#   ⦿ Section: 3
#    ⁃ Count of standard compliance in the code block: 
#      ◦ age: 3
#      ◦ loan: 4
#      Total: 7
#    ⁃ Count of standard violation in the code block: 
#      ◦ delinquency_record: 3
#      Total: 3
# 🔹 Absent standard in the code block: 0
# 🔹 Reference Number: d8aca700d20c500f922630cd93ffb4a5d598c5902a506e459dcdcd81e89fe92c
# 🔵 Standard Compliance Report
# 🔹 Type: Credit-Scoring
# 🔹 Code Block Name: credit-score.py
# 🔹 Analysis Result =>
#   1. Refer to ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices
#   ⦿ Section: Definition of Credit Scoring
#    ⁃ Count of standard compliance in the code block: 
#      ◦ perform_creditscoring: 2
#      Total: 2
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Credit Scoring Development
#    ⁃ Count of standard compliance in the code block: 
#      ◦ age: 6
#      ◦ Management: 1
#      ◦ Information: 7
#      Total: 14
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Preparation of Credit Information no.8.1
#    ⁃ Count of standard compliance in the code block: 
#      ◦ age: 6
#      ◦ Management: 1
#      Total: 7
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Preparation of Credit Information no.8.2
#    ⁃ Count of standard compliance in the code block: 
#      ◦ delinquency_record: 14
#      Total: 14
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Preparation of Credit Information no.8.3
#    ⁃ Count of standard compliance in the code block: 
#      ◦ delinquency_record: 14
#      Total: 14
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Preparation of Credit Information no.8.5
#    ⁃ Count of standard compliance in the code block: 
#      ◦ delinquency_record: 14
#      Total: 14
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Preparation of Credit Information no.8.6
#    ⁃ Count of standard compliance in the code block: 
#      ◦ delinquency_record: 14
#      Total: 14
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Construction of Credit Scoring
#    ⁃ Count of standard compliance in the code block: 
#      ◦ delinquency_record: 14
#      Total: 14
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Testing of the Reliability of Separation and/or Accuracy of Prediction Power of Credit Scoring
#    ⁃ Count of standard compliance in the code block: 
#      ◦ delinquency_record: 14
#      Total: 14
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Implementation of Credit Scoring System I
#    ⁃ Count of standard compliance in the code block: 
#      ◦ delinquency_record: 14
#      Total: 14
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Implementation of Credit Scoring System II
#    ⁃ Count of standard compliance in the code block: 
#      ◦ delinquency_record: 14
#      Total: 14
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Overrides in Credit Approval
#    ⁃ Count of standard compliance in the code block: 
#      ◦ delinquency_record: 14
#      Total: 14
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Verification of the Applicant’s Information
#    ⁃ Count of standard compliance in the code block: 
#      ◦ delinquency_record: 14
#      Total: 14
#    ⁃ Count of standard violation in the code block: 0
#   2. Refer to Credit Information Business Act, B.E.2545
#   ⦿ Section: 3
#    ⁃ Count of standard compliance in the code block: 
#      ◦ age: 6
#      ◦ loan: 5
#      ◦ Management: 1
#      Total: 12
#    ⁃ Count of standard violation in the code block: 
#      ◦ delinquency_record: 14
#      Total: 14
# 🔹 Absent standard in the code block: 0
# 🔹 Reference Number: 593793d6fb4b19e8cdb70e5e309678f57c223ac40a890af025f1e26552aadbb4