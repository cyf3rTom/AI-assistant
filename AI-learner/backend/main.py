# File: main2.py
import os
import re
from collect_user_inputs import collect_user_inputs
from check_directory_exists import check_directory_exists
from create_directory import create_directory
from check_file_exists import check_file_exists
from write_to_file import write_to_file
from read_from_csv import read_from_csv
from fetch_data_from_llm import fetch_data_from_llm
from function_to_plan_next_segment import function_to_plan_next_segment
from update_file_with_datestamp import update_file_with_datestamp
from email_utils import send_weekly_mail


def main():
    # Step 1: Collect user input interactively
    email = input("Enter your email ID: ").strip()
    username = input("Enter your name: ").strip()
    project_name = input("Enter your project/subject name: ").strip()

    user_data = collect_user_inputs(email, username, project_name, debug=2)

    # Step 2: Check/Create project directory
    if not check_directory_exists(project_name, debug=2):
        create_directory(project_name, debug=2)
        if debug:
            print(f"Created directory {project_name}")
        return

    # Step 3: Check for sub-chapter CSV
    csv_path = os.path.join(project_name, "sub_chapter_tasks.csv")
    if not check_file_exists(csv_path, debug=2):
        print(f"ERROR: Please provide the file at {csv_path}")
        return

    # Step 4: Read CSV
    sub_chapters = read_from_csv(csv_path, debug=2)

    # Step 5: Process each sub-chapter
    for chapter in sub_chapters:
        chapter_name = chapter["Chaptername"]
        task_prompt = chapter["Task"]
        if debug >= 2:
            print(f"Processing chapter: {chapter_name}")

        chapter_dir = os.path.join(project_name, chapter_name)
        if not check_directory_exists(chapter_dir, debug=2):
            create_directory(chapter_dir, debug=2)

        llm_data_file = os.path.join(chapter_dir, "Sub-Chapter_LLM_Data.log")

        # If no existing log, fetch and write
        if not (os.path.exists(llm_data_file) and os.path.getsize(llm_data_file) > 0):
            if debug >= 1:
                print(f"Fetching initial LLM data for {chapter_name}")
            main_prompt = input(f"Enter the main prompt for {chapter_name}: ")
            llm_response = fetch_data_from_llm(main_prompt, debug=2)
            if llm_response:
                write_to_file(llm_data_file, [llm_response], debug=2)
        else:
            if debug >= 1:
                print(f"Existing log found for {chapter_name}, planning segments")
            segments = function_to_plan_next_segment(
                fileName=llm_data_file,
                startPattern=r"Start: .*",
                endPattern=r"END: .*",
                numSegments=2,
                waitPeriod=1,
                debug=2
            )
            if segments:
                for segment in segments:
                    if debug >= 1:
                        print(f"Sending email with segment: {segment[:30]}...")
                    send_weekly_mail(email, segment, debug=2)
                # After emails, update log with datestamps
                update_file_with_datestamp(llm_data_file, segments, debug=2)

if __name__ == "__main__":
    # You can set debug here if desired
    debug = 2
    main()




# #main.py
# import os
# from collect_user_inputs import collect_user_inputs
# from check_directory_exists import check_directory_exists
# from create_directory import create_directory
# from check_file_exists import check_file_exists
# from write_to_file import write_to_file
# from read_from_csv import read_from_csv
# from fetch_data_from_llm import fetch_data_from_llm
# from function_to_plan_next_segment import function_to_plan_next_segment
# from update_file_with_datestamp import update_file_with_datestamp
# from app import app
# from email_utils import send_weekly_mail
# #from send_email import send_email
# #from send_email import s

# #from utils.send_email import send_email
# #from utils.send_email import s


# import os
# print(os.getcwd())

# # user_mail = app.user_email



# def main():
#     # Step 1: Collect user input interactively
#     email = input("Enter your email ID: ")
#     username = input("Enter your name: ")
#     project_name = input("Enter your project/subject name: ")

#     user_data = collect_user_inputs(email, username, project_name, debug=2)

#     # Step 2: Check/Create project directory
#     if not check_directory_exists(project_name, debug=2):
#         create_directory(project_name, debug=2)
#         main_prompt = input("Enter the main prompt for LLM: ")
#         # print("Please provide sub-chapter CSV file in the directory.")
#         return

#     # Step 3: Check for sub-chapter CSV
#     csv_path = os.path.join(project_name, "sub_chapter_tasks.csv")
#     if not check_file_exists(csv_path, debug=2):
#         print(f"ERROR: Please provide the file at {csv_path}")
#         return

#     # Step 4: Read CSV
#     sub_chapters = read_from_csv(csv_path, debug=2)

#     # Step 5: Process each sub-chapter
#     for chapter in sub_chapters:
#         chapter_name = chapter["Chaptername"]
#         task_prompt = chapter["Task"]
#         print(f"Chapter_name:-",chapter_name)
#         print(f"Task_prompt:-",task_prompt)

#         chapter_dir = os.path.join(project_name, chapter_name)

#         if not check_directory_exists(chapter_dir, debug=2):
#             print(f"Creating Chapter directory as it does not exists",chapter_dir)
#             create_directory(chapter_dir, debug=2)

#         llm_data_file = os.path.join(chapter_dir, "Sub-Chapter_LLM_Data.log")

#         if not check_file_exists(llm_data_file, debug=2):
#          print(f"Checking llm_data_file file",llm_data_file)
#         if not (os.path.exists(llm_data_file) and os.path.getsize(llm_data_file) > 0):
#             print(f"Creating llm_data_file",llm_data_file) 
#             main_prompt = input(f"Enter the main prompt for {chapter_name}: ")
#             #llm_response = fetch_data_from_llm(task_prompt, debug=2)
#             llm_response = fetch_data_from_llm(main_prompt, debug=2)
#             print(llm_response)

#             print("Herer llm_data_file")
#             write_to_file(llm_data_file, [llm_response], debug=2)
#         else:
#             print(f"File llm_data_file exist",llm_data_file) 
#             segments = function_to_plan_next_segment(
#                 fileName=llm_data_file,
#                 startPattern=r"Start: .*",
#                 endPattern=r"END: .*",
#                 numSegments=2,
#                 waitPeriod=1,
#                 debug=2
#             )
#             if segments:
#                 for segment in segments:
#                     send_weekly_mail(email, segment, debug=2)
#                     print("Senidng email", email, segment)
#                 update_file_with_datestamp(llm_data_file, segments, debug=2)

# if __name__ == "__main__":
#     main()
