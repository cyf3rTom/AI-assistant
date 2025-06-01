# Function 11: Update file with timestamp
def update_file_with_START_Datestamp_END_Datestamp(file_path, start, end):
    with open(file_path, 'r+') as f:
        data = json.load(f)
        for segment in data['segments']:
            if not segment.get('sent'):
                segment['start_date'] = start
                segment['end_date'] = end
                segment['sent'] = True
                break
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
 
                       
# Function 12: Higher-level segment planner
def function_to_plan_next_segment(user_email, data_file):
    segment = plan_next_segment(data_file)
    if segment:
        send_email(user_email, "Your Next Learning Segment", segment['content'])
        now = datetime.now().strftime("%Y-%m-%d")
        end = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        update_file_with_START_Datestamp_END_Datestamp(data_file, now, end)



# Function 8: Send email
def send_email(to, subject, content):
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = to

    with smtplib.SMTP('smtp.example.com') as server:
        server.starttls()
        server.login('your_email@example.com', 'your_password')
        server.send_message(msg)

# Function 9: Plan next segment
def plan_next_segment(data_file):
    with open(data_file, 'r') as f:
        data = json.load(f)
    for segment in data['segments']:
        if not segment.get('sent'):
            return segment
    return None