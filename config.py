"""
packages:
        pip install xlrd==1.2.0
            => other versions have error reading Excel file, this version works perfectly for the below code
"""

# package for reading excel
import xlrd
# os for location access
import os


def readConfig():
    # variable values to be read from config file
    # folder location of input images
    inputImageFolder = ''
    # folder location for output text file
    outputTextFolder = ''
    # Email id
    userEmailId = ''
    # App password for gmail
    userGmailAppPass = ''
    # Subject for email with attachment
    emailSubject = ''
    # Output folder containing attachments of email
    emailOutput=''
    # Client email for sending output mail
    clientID=''

    # location of Excel file
    xlFileLoc = os.path.join(os.getcwd(), 'config.xlsx')

    try:

        # reading Excel file
        pathOfConfig = (xlFileLoc)
        try:
            # gathering required data from Excel file
            workbook = xlrd.open_workbook(pathOfConfig)
            sheet = workbook.sheet_by_name('config')

            # Matching variable name before taking value
            if sheet.cell_value(1, 0) == 'inputImageFolder':
                inputImageFolder = sheet.cell_value(1, 1)
            if sheet.cell_value(2, 0) == 'outputTextFolder':
                outputTextFolder = sheet.cell_value(2, 1)
            if sheet.cell_value(3, 0) == 'Email_ID':
                userEmailId = sheet.cell_value(3, 1)
            if sheet.cell_value(4, 0) == 'App_Password':
                userGmailAppPass = sheet.cell_value(4, 1)
            if sheet.cell_value(5, 0) == 'EmailSubject':
                emailSubject = sheet.cell_value(5, 1)
            if sheet.cell_value(6, 0) == 'outputEmailFolder':
                emailOutput = sheet.cell_value(6, 1)
            if sheet.cell_value(7, 0) == 'Client_Email_id':
                clientID = sheet.cell_value(7, 1)

            # returning gathered variable name
            return inputImageFolder, outputTextFolder, userEmailId, userGmailAppPass, emailSubject,emailOutput,clientID

        # exception for failing to open excel
        except:
            print("Failed to read config file")
            exit(0)

    # Exception for config file corrupted or missing
    except FileNotFoundError:
        print("Config File is not present/corrupted, exiting program!!!")
        exit(0)

