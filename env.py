import os

PROJECT_PATH = '/root/mounted/projects/home_credit_default'
DATA_PATH = os.path.join(PROJECT_PATH, 'data')

ORIGINAL_DATA_PATH = os.path.join(DATA_PATH, 'original')
APPLICATION_TRAIN_CSV = os.path.join(ORIGINAL_DATA_PATH, 'application_train.csv')
APPLICATION_TEST_CSV = os.path.join(ORIGINAL_DATA_PATH, 'application_test.csv')
BUREAU_CSV = os.path.join(ORIGINAL_DATA_PATH, 'bureau.csv')
BUREAU_BALANCE_CSV = os.path.join(ORIGINAL_DATA_PATH, 'bureau_balance.csv')
CREDIT_CARD_BALANCE_CSV = os.path.join(ORIGINAL_DATA_PATH, 'credit_card_balance.csv')
HOMECREDIT_COLUMNS_DESCRIPTION_CSV = os.path.join(ORIGINAL_DATA_PATH, 'HomeCredit_columns_description.csv')
INSTALLMENTS_PAYMENTS_CSV = os.path.join(ORIGINAL_DATA_PATH, 'installments_payments.csv')
POS_CASH_BALANCE_CSV = os.path.join(ORIGINAL_DATA_PATH, 'POS_CASH_balance.csv')
PREVIOUS_APPLICATION_CSV = os.path.join(ORIGINAL_DATA_PATH, 'previous_application.csv')
SAMPLE_SUBMISSION_CSV = os.path.join(ORIGINAL_DATA_PATH, 'sample_submission.csv')


EDA_DATA_PATH = os.path.join(DATA_PATH, 'eda')
PREPROCESSING_DATA_PATH = os.path.join(DATA_PATH, 'preprocessing')
FEATURES_DATA_PATH = os.path.join(DATA_PATH, 'features')