from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt  # plotting
import numpy as np  # linear algebra
import os  # accessing directory structure
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns  # visualization tool
import json  # for parse "properties" parameter
import warnings
warnings.filterwarnings('ignore')

# Function for maping datasets.
# We will change all 'consider' value to 1, and 'clear' = 0 for **map_encode_docs** list


def result_encode(features, dataset):
    for feature in features:
        dataset[feature] = dataset[feature].map(result_map)

# function for clean and prepare dataframe


def prepare_data(dataframe):
    dataframe.created_at = pd.to_datetime(dataframe.created_at,
                                          errors='coerce',
                                          format='%Y-%m-%d %H:%M:%S')
    dataframe.fillna(np.nan)


map_encode_all = ['result_doc',
                  "visual_authenticity_result_doc",
                  "image_integrity_result",
                  "face_detection_result",
                  "image_quality_result",
                  "supported_document_result",
                  'conclusive_document_quality_result',
                  'colour_picture_result',
                  'data_validation_result',
                  'data_consistency_result',
                  'data_comparison_result',
                  'police_record_result',
                  'compromised_document_result',
                  'face_comparison_result',
                  'facial_image_integrity_result',
                  'visual_authenticity_result_face',
                  'result_face']

result_map = {"consider": 1, "clear": 0, 'unidentified': 1}
doc = pd.read_csv('../input/kyc_challenge/doc_reports.csv', delimiter=',')
doc.dataframeName = 'doc_reports.csv'
prepare_data(doc)
doc.head(5)
mb = pd.merge(doc, face, on='Unnamed: 0', how='left',
              suffixes=('_doc', '_face'), validate='one_to_one')
mb = mb.drop(['Unnamed: 0', 'user_id_face', 'attempt_id_doc', 'attempt_id_face',
             'created_at_face', 'sub_result', 'properties_face',], axis=1)
suspected_params = ["image_integrity_result",
                    'facial_image_integrity_result', 'image_quality_result']
# cleaning
mb.properties_doc = mb.properties_doc.apply(
    lambda row: row.replace('None', "\"NaN\""))
mb['properties_doc'] = mb.properties_doc.apply(
    lambda x: x.strip("\'<>()").replace('\'', '\"'))
# loading
mb['properties_doc'] = mb['properties_doc'].apply(json.loads)
# parsing
mb = mb.drop('properties_doc', 1).assign(
    **pd.DataFrame(mb.properties_doc.values.tolist()))
# and get dates from new columns
mb.date_of_expiry = pd.to_datetime(
    mb.date_of_expiry, errors='coerce', format='%Y-%m-%d')
mb.issuing_date = pd.to_datetime(
    mb.issuing_date, errors='coerce', format='%Y-%m')
suspect_data[suspect_data['image_integrity_result'] ==
             1]['issuing_country'].value_counts()[:10].plot(kind='bar')
suspect_data[suspect_data['image_integrity_result'] ==
             1]['nationality'].value_counts()[:10].plot(kind='bar')
suspect_data[suspect_data['image_integrity_result'] ==
             1]['document_type'].value_counts()[:10].plot(kind='bar')


# 🔵 Standard Compliance Report
# 🔹 Product Type: Know-Your-Customer Process
# 🔹 Code Block Name: kyc.py
# 🔹 Analysis Result: 
#   Standard => Bank of Thailand Notification No. SorNorChor. 1/2563 Re: Regulations on Know Your Customer (KYC) For e-Money Service Activation
#   ⦿ Section: Regulations on Know Your Customer
#    ⁃ Count of standard compliance in the code block: 
#      ◦ image_integrity_result: 5
#      ◦ face_detection_result: 1
#      ◦ image_quality_result: 2
#      ◦ face_comparison_result: 1
#      ◦ facial_image_integrity_result: 2
#      ◦ visual_authenticity_result_face: 1
#      ◦ result_face: 1
#      ◦ face: 1
#      ◦ _face: 1
#      ◦ user_id_face: 1
#      ◦ attempt_id_face: 1
#      ◦ created_at_face: 1
#      ◦ properties_face: 1
#      Total: 19
#    ⁃ Count of standard violation in the code block: 0
# 🔹 Absent section in the code block: 0
# 🔹 Create Date: Mon, 04 Sep 2023 18:20:24 GMT
# 🔹 Reference Number: b27f521eda7ef8dcdb2810f6f1528ab00ed69ab314b81b83bd5586e4cfa8bcaf

# 🔵 Standard Compliance Report
# 🔹 Product Type: Know-Your-Customer Process
# 🔹 Code Block Name: kyc.py
# 🔹 Analysis Result: 
#   Standard => Notification of the Bank of Thailand No. FPG. 19/2562 Re: Regulations on Know Your Customer (KYC) for deposit-account opening at financial institutions
#   ⦿ Section: Regulations on Know-Your-Customer
#    ⁃ Count of standard compliance in the code block: 
#      ◦ preprocessing: 1
#      ◦ processing: 1
#      ◦ errors: 3
#      ◦ face_detection_result: 1
#      ◦ data_comparison_result: 1
#      ◦ face_comparison_result: 1
#      ◦ facial_image_integrity_result: 2
#      Total: 10
#    ⁃ Count of standard violation in the code block: 0
#   ⦿ Section: Principle
#    ⁃ Count of standard compliance in the code block: 
#      ◦ dataframeName: 1
#      ◦ Unnamed: 2
#      Total: 3
#    ⁃ Count of standard violation in the code block: 0
# 🔹 Absent section in the code block: 0
# 🔹 Create Date: Mon, 04 Sep 2023 18:22:27 GMT
# 🔹 Reference Number: a9b045db6337c5f89784a3e37f8e2471539e9f8a8ab28e39f87fec96cf7ac97e