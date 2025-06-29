from flask import Flask, request, jsonify
from flask_cors import CORS
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
from email_utils import send_weekly_mail

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"], supports_credentials=True)

@app.route('/api/process', methods=['POST'])
def process_input():
    try:
        data = request.get_json()
        email = data.get("email")
        username = data.get("username")
        project_name = data.get("projectName")

        if not all([email, username, project_name]):
            return jsonify({"status": "error", "message": "Missing required fields"}), 400

        debug = 2
        user_data = collect_user_inputs(email, username, project_name, debug=debug) #add debug=2 for debuging

        # Step 2: Check/Create project directory
        if not check_directory_exists(project_name, debug=debug):
            create_directory(project_name, debug=debug) #add debug=2 for debuging

        # Step 3: Check for sub-chapter CSV
        csv_path = os.path.join(project_name, "sub_chapter_tasks.csv")
        if not check_file_exists(csv_path, debug=debug):
            return jsonify({"status": "error", "message": f"Missing file at {csv_path}"}), 404 #add debug=2 for debuging

        # Step 4: Read CSV
        sub_chapters = read_from_csv(csv_path, debug=0) #add debug=2 for debuging
        all_segments = []

        # Step 5: Process each sub-chapter
        for chapter in sub_chapters:
            chapter_name = chapter["Chaptername"]
            task_prompt = chapter["Task"]

            chapter_dir = os.path.join(project_name, chapter_name)
            if not check_directory_exists(chapter_dir, debug=debug):
                create_directory(chapter_dir, debug=debug) #add debug=2 for debuging

            llm_data_file = os.path.join(chapter_dir, "Sub-Chapter_LLM_Data.log")

            if not (os.path.exists(llm_data_file) and os.path.getsize(llm_data_file) > 0):
                main_prompt = f"Share a data concept wise for {chapter_name} by adding Start: <concept name> and END: <concept name>"
                llm_response = fetch_data_from_llm(main_prompt, debug=debug) #add debug=2 for debuging
                if llm_response:
                    write_to_file(llm_data_file, [llm_response], debug=0) #add debug=2 for debuging
            else:
                segments = function_to_plan_next_segment(
                    fileName=llm_data_file,
                    startPattern=r"Start: .*",
                    endPattern=r"END: .*",
                    numSegments=2,
                    waitPeriod=1,
                    debug=debug
                ) #add debug=2 for debuging
                if segments:
                    for segment in segments:
                        send_weekly_mail(email, segment, debug=0) #add debug=2 for debuging
                    update_file_with_datestamp(llm_data_file, segments, debug=debug)
                    all_segments.extend(segments)

        return jsonify({
            "status": "success",
            "user_data": user_data,
            "processed_segments": all_segments
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
