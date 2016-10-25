from datetime import datetime


# data_extractor reads through Report_logfile and extracts important data
def data_extractor():
    # welcome message
    print("ObjetStudio Data Extractor Program")
    print("Please answer the questions below and follow the indicated steps. Thank you!")
    print("Every time you answer \'no\' to a question, the program will quit to let you make the required changes. "
          "Restart the program once you have completed the changes.\n")

    # check that no build tray is being built when exporting Report_logfile
    did_export = input("Did you export Report_logfile from ObjetStudio? (Y/N)\n")
    if did_export == 'Y' or did_export == 'y':
        print("Confirmed.\n")
    else:
        print("Go to the Job Manager tab in ObjetSudio. Under \'Tools\' (top right of screen), click on \'Report Log "
              "Files\'. Save the file in the same directory as this program under the default name \'Report_logfile\'.")
        quit()

    # check that no build tray is being built when exporting Report_logfile
    no_build_tray = input("Are you sure there was no build tray being built when you exported Report_logfile? (Y/N)\n")
    if no_build_tray == 'Y' or no_build_tray == 'y':
        print("Confirmed.\n")
    else:
        print("Please wait until the build tray is done building before exporting Report_logfile.")
        quit()

    # check that Report_logfile is in correct location
    correct_file_location = input("Have you placed Report_logfile in the same directory as this program? (Y/N)\n")
    if correct_file_location == 'Y' or correct_file_location == 'y':
        print("Confirmed.\n")
    else:
        print("Please place Report_logfile in the same directory.")
        quit()

    # check that Report_logfile has been unzipped
    unzipped_file = input("Have you unzipped Report_logfile? (Y/N)\n")
    if unzipped_file == 'Y' or unzipped_file == 'y':
        print("Confirmed. Starting file parsing...\n")
    else:
        print("Please unzip Report_logfile in the same directory as this program.")
        quit()

    # acquire date range from user
    while True:
        try:
            input_date = input("What start date do you want to use? (month/day/year)\n")
            date_list = input_date.split('/')
            month = date_list[0]
            if len(month) == 1:
                month = '0' + month
            day = date_list[1]
            if len(day) == 1:
                day = '0' + day
            year = date_list[2]
            if len(year) == 2:
                year = '20' + year
            input_date = month + '/' + day + '/' + year
            start_datetime = datetime.strptime(input_date.strip(), '%m/%d/%Y')
        except:
            print("Incorrect date format. Please try again.\n")
            continue
        else:
            print("Confirmed.")
            break

    # if so, create a new write CSV file, 'job_data.csv', to paste the extracted data
    output_file = open("job_data.csv", 'w')
    output_file.write("Job Name,Date,Model Consumption,Support Consumption\n")

    # open and read through Report_logfile (file address has been hardcoded)
    counter = 0
    with open("Report_logfile\ObjetJobDataCollection.txt", 'r') as my_file:
        for line in my_file:
            if counter == 0:
                counter += 1
            else:
                line_list = line.split(',')
                date = line_list[3].strip()
                compare_datetime = datetime.strptime(date, '%x')
                if compare_datetime.date() >= start_datetime.date():
                    job_name = line_list[8].strip()
                    model_consumption = line_list[12].strip()
                    support_consumption = line_list[13].strip()
                    output_file.write(job_name + ',' + date + ',' + model_consumption + ',' + support_consumption + '\n')

    # close write file
    output_file.close()


# run data_extractor method
data_extractor()
