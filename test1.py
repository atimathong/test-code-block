def perform_creditscoring(sender_account, age, loan, delinquency_record):
    if sender_account.balance < age:
        raise ValueError("Insufficient funds")
    if age < 18:
        raise ValueError("Error!!!")
    if age != 0:
        raise ValueError("Reject this person")
    if delinquency_record:
        raise ValueError("Reject this person")
    print("return")
    print("loan", loan)
    print("age", age)
    return ""


#f1eeee
# #daab70
#f1eeee




# 🔵 Standard Compliance Report
# 🔹 Product Type: Credit Scoring
# 🔹 Code Block Name: test1.py
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
#      ◦ delinquency_record: 2
#      Total: 2
# 🔹 Absent section in the code block: 0
# 🔹 Reference Number: 533f0367cc8f685510cd5216b7c9d9dbc740d45c4e53ec814c12139259e23977
# 🔵 Standard Compliance Report
# 🔹 Product Type: Credit Scoring
# 🔹 Code Block Name: test1.py
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
#      ◦ delinquency_record: 2
#      Total: 2
# 🔹 Absent section in the code block: 0
# 🔹 Reference Number: 600f0048052d037b4267d1a49804ad2eac517f7f180ecfc665b85e73396e5885
# 🔵 Standard Compliance Report
# 🔹 Product Type: Credit Scoring
# 🔹 Code Block Name: test1.py
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
#      ◦ delinquency_record: 2
#      Total: 2
# 🔹 Absent section in the code block: 0
# 🔹 Reference Number: e8fcab1bf389671923b3e82ba214e1dd0b70ccd7b7726a9cad837896617e6e5e