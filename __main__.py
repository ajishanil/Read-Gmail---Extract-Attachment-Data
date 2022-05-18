"""
Author: Ajish Anil
Date Created: 20 Apr 2022

info: This project is created as a part of initial interview process, for the company "Siemens"
"""

import folderStructureCreation
import os
import config
import extractTextFromImage
import emailDownloadAttachment
import SendMailWithAttachment


def main():
    print("______________________________Project Execution Started__________________________________________________\n")
    # Reading config values for folder path
    print("______________________________Reading configuration values from congig file______________________________\n")
    inputImageFolder, outputTextFolder, userEmailId, userGmailAppPass, emailSubject, emailOutputFolder, clientID = config.readConfig()

    # Get complete path of folders
    inputImageFolder = os.path.join(os.getcwd(), inputImageFolder)
    outputTextFolder = os.path.join(os.getcwd(), outputTextFolder)
    emailOutputFolder = os.path.join(os.getcwd(), emailOutputFolder)

    # Creating folders
    print("______________________________Creating Folder Structures_________________________________________________\n")
    folderStructureCreation.createProjectFolder(inputImageFolder, outputTextFolder, emailOutputFolder)

    # download emails with attachments into input folder
    print("______________________________Gathering Emails___________________________________________________________\n")
    emailDownloadAttachment.downloadAttachment(emailSubject)
    print("______________________________Downloaded Attachments from All Unread Emails______________________________\n")

    # Extracting images present in image folder into text in text folder
    print("______________________________Extracting Text data from Downloaded Images________________________________\n")
    extractTextFromImage.convertImages(inputImageFolder, outputTextFolder)
    print("______________________________Data Extraction Completed__________________________________________________\n")

    # Sending output to client email address from development email server.
    print("______________________________Sending Email to Client____________________________________________________\n")
    bodyOfOutputEmail = "The python file has successfully extracted data from all the received mails. Please find with this mail the attached copy of Outputs and Outputs"
    SendMailWithAttachment.sendOutputMail(userEmailId, clientID, bodyOfOutputEmail, userGmailAppPass, inputImageFolder,
                                          outputTextFolder, emailOutputFolder)
    print("______________________________Email to Client Send Successfully__________________________________________\n")

    print("______________________________Program Completed Successfully_____________________________________________\n")


if __name__ == "__main__":
    main()
