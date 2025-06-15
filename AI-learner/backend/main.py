#main.py
import os
from collect_user_inputs import collect_user_inputs
from check_directory_exists import check_directory_exists
from create_directory import create_directory
from check_file_exists import check_file_exists
from write_to_file import write_to_file
from read_from_csv import read_from_csv
from fetch_data_from_llm import fetch_data_from_llm
from function_to_plan_next_segment import function_to_plan_next_segment
from update_file_with_datestamp import update_file_with_datestamp
from app import app
from email_utils import send_weekly_mail
#from send_email import send_email
#from send_email import s

#from utils.send_email import send_email
#from utils.send_email import s


import os
print(os.getcwd())

# user_mail = app.user_email



def main():
    # Step 1: Collect user input interactively
    email = input("Enter your email ID: ")
    username = input("Enter your name: ")
    project_name = input("Enter your project/subject name: ")

    user_data = collect_user_inputs(email, username, project_name, debug=2)

    # Step 2: Check/Create project directory
    if not check_directory_exists(project_name, debug=2):
        create_directory(project_name, debug=2)
        main_prompt = input("Enter the main prompt for LLM: ")
        # print("Please provide sub-chapter CSV file in the directory.")
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
        print(f"Chapter_name:-",chapter_name)
        print(f"Task_prompt:-",task_prompt)

        chapter_dir = os.path.join(project_name, chapter_name)

        if not check_directory_exists(chapter_dir, debug=2):
            print(f"Creating Chapter directory as it does not exists",chapter_dir)
            create_directory(chapter_dir, debug=2)

        llm_data_file = os.path.join(chapter_dir, "Sub-Chapter_LLM_Data.log")

        #if not check_file_exists(llm_data_file, debug=2)
        print(f"Checking llm_data_file file",llm_data_file)
        if not (os.path.exists(llm_data_file) and os.path.getsize(llm_data_file) > 0):
            print(f"Creating llm_data_file",llm_data_file) 
            main_prompt = input(f"Enter the main prompt for {chapter_name}: ")
            llm_response = fetch_data_from_llm(task_prompt, debug=2)
            print(llm_response)
            
#             llm_response = """ \n
#             **moderate summary** of CMOS basics from both **VLSI (Very-Large-Scale Integration)** and **semiconductor** perspectives, structured concept-wise with clear **Start** and **End** tags for each concept:\n
# Start: CMOS Technology\n
# **CMOS (Complementary Metal-Oxide-Semiconductor)** is a technology used to construct integrated circuits, including microprocessors, microcontrollers, memory chips, and other digital logic circuits. It uses a combination of **p-type** and **n-type** MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors).\n
# **Key Feature**: Low static power consumption power is only consumed during switching.\n
# **Why "Complementary"**: It uses both NMOS and PMOS transistors in a complementary way to achieve logic functions.\n
# **Example**: In a CMOS inverter, when the input is high, the NMOS conducts and pulls the output low; when the input is low, the PMOS conducts and pulls the output high.\n
# End: CMOS Technology\n
# Start: MOSFET Basics\n
# MOSFETs are the building blocks of CMOS. There are two types:\n
# **NMOS**: Conducts when gate voltage is high.\n
# **PMOS**: Conducts when gate voltage is low.\n
# Each MOSFET has:\n
# **Gate**: Controls the transistor.\n
# **Source** and **Drain**: Current flows from source to drain.\n
# **Substrate**: The body of the transistor (p-type for NMOS, n-type for PMOS).\n
# **Example**: In an NMOS, applying a positive voltage to the gate creates an inversion layer allowing electrons to flow from source to drain.\n
# End: MOSFET Basics\n
# """
            print("Herer llm_data_file")
            write_to_file(llm_data_file, [llm_response], debug=2)
        else:
            print(f"File llm_data_file exist",llm_data_file) 
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
                    send_weekly_mail(email, segment, debug=2)
                    print("Senidng email", email, segment)
                update_file_with_datestamp(llm_data_file, segments, debug=2)

if __name__ == "__main__":
    main()
