import os


def createProjectFolder(inputImageFolder, outputTextFolder,emailOutputFolder):
    # Creating folders for image extraction
    try:
        if os.path.exists(inputImageFolder):
            for eachfile in os.listdir(inputImageFolder):
                os.remove(os.path.join(inputImageFolder, eachfile))
            os.rmdir(inputImageFolder)
            os.mkdir(inputImageFolder)
        else:
            os.mkdir(inputImageFolder)
        if os.path.exists(outputTextFolder):
            for eachfile in os.listdir(outputTextFolder):
                os.remove(os.path.join(outputTextFolder, eachfile))
            os.rmdir(outputTextFolder)
            os.mkdir(outputTextFolder)
        else:
            os.mkdir(outputTextFolder)
        if os.path.exists(emailOutputFolder):
            for eachfile in os.listdir(emailOutputFolder):
                os.remove(os.path.join(emailOutputFolder, eachfile))
            os.rmdir(emailOutputFolder)
            os.mkdir(emailOutputFolder)
        else:
            os.mkdir(emailOutputFolder)
    except:
        print("Folder structure creation failed, exiting program")
        exit(0)
