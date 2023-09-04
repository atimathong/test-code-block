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
    age = 13
    return ""

# 🔵 Standard Compliance Report
# 🔹 Product Type: Credit Scoring
# 🔹 Code Block Name: credit-score.py
# 🔹 Analysis Result:
#   1. Standard => Credit Information Business Act B.E.2545
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
# 🔹 Absent section in the code block: 0
# 🔹 Reference Number: 440d7e6f83615f337aa5df2bd9c946741fc62212863cdafe5edf966d10c1901b
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
# 🔹 Reference Number: f338a6127ca85428bd91f76ad351898ddc0086508078b0052c068dc88a26f4d4
