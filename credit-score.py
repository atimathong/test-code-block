def perform_creditscoring(sender_account, age, loan, delinquency_record):
    if sender_account.balance < age:
        raise ValueError("Insufficient funds")
    if age < 18:
        raise ValueError("Error!!!")
    if age != 0:
        raise ValueError("Reject this person")
    print("return")
    print("loan", loan)
    print("age", age)
    return ""


# 🔵 Standard Compliance Report
# 🔹 Product Type: Credit-Scoring
# 🔹 Code Block Name: credit-score.py
# 🔹 Analysis Result:
#   1. Standard => Credit Information Business Act, B.E.2545
#   ⦿ Section: 3
#    ⁃ Count of standard compliance in the code block:
#      ◦ perform_creditscoring: 1
#      ◦ sender_account: 2
#      ◦ age: 6
#      ◦ loan: 3
#      Total: 12
#    ⁃ Count of standard violation in the code block:
#      ◦ delinquency_record: 1
#      Total: 1
#   ⦿ Section: 10
#    ⁃ Count of standard compliance in the code block: 0
#    ⁃ Count of standard violation in the code block:
#      ◦ delinquency_record: 1
#      Total: 1
# 🔹 Absent standard in the code block: 0
# 🔹 Reference Number: 77150d5731dd4b92e09277525511265a936deac9a9c6403b600b44cec76bfaa1
# 🔵 Standard Compliance Report
# 🔹 Product Type: Credit-Scoring
# 🔹 Code Block Name: credit-score.py
# 🔹 Analysis Result:
#   1. Standard => ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices
#   ⦿ Section: Preparation of Credit Information no.8.2
#    ⁃ Count of standard compliance in the code block:
#      ◦ perform_creditscoring: 1
#      Total: 1
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Definition of Credit Scoring
#    ⁃ Count of standard compliance in the code block:
#      ◦ perform_creditscoring: 1
#      Total: 1
#    ⁃ Count of standard violation in the code block: 0
# 🔹 Absent section in the code block:
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Implementation of Credit Scoring System I
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Credit Scoring Development
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Preparation of Credit Information no.8.6
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Implementation of Credit Scoring System II
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Verification of the Applicant’s Information
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Preparation of Credit Information no.8.3
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Overrides in Credit Approval
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Construction of Credit Scoring
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Preparation of Credit Information no.8.1
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Testing of the Reliability of Separation and/or Accuracy of Prediction Power of Credit Scoring
# 🔹 Reference Number: 91167d771f432b632988ad2a80a4b4599ab0c2415a24aa921cffc8129b30879e

# 🔵 Standard Compliance Report
# 🔹 Product Type: Credit Scoring
# 🔹 Code Block Name: credit-score.py
# 🔹 Analysis Result: 
#   1. Standard => ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices
#   ⦿ Section: Preparation of Credit Information no.8.2
#    ⁃ Count of standard compliance in the code block: 
#      ◦ perform_creditscoring: 1
#      Total: 1
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Definition of Credit Scoring
#    ⁃ Count of standard compliance in the code block: 
#      ◦ perform_creditscoring: 1
#      Total: 1
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Implementation of Credit Scoring System I
#    ⁃ Count of standard compliance in the code block: 
#      ◦ return: 1
#      Total: 1
#    ⁃ Count of standard violation in the code block: 0
# 🔹 Absent section in the code block: 
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Credit Scoring Development
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Preparation of Credit Information no.8.6
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Implementation of Credit Scoring System II
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Verification of the Applicant’s Information
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Preparation of Credit Information no.8.3
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Overrides in Credit Approval
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Construction of Credit Scoring
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Preparation of Credit Information no.8.1
#  ◦ ThorPorTor. SorGorSor. (03) Wor. 277/2548 Re: Guidelines for Risk Management Practices at section Testing of the Reliability of Separation and/or Accuracy of Prediction Power of Credit Scoring
# 🔹 Reference Number: dd78aa78f8a48dba4cbce40f7af8777ff2477a1cfd0fe5229fbd8c37faf279fe