import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    if not isinstance(attendees, list):
        for attendee in attendees:
            if not isinstance(attendee, dict):
                print("Error: Attendees should be a list of dictionaries.")
                return

    if not template:
        print("Error: The template is empty, no output files generated.")
        return
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        invitation = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key) or "N/A"
            placeholder = "{" + key + "}"
            invitation = invitation.replace(placeholder, value)
        
        output_filename = f"output_{index}.txt"
        
        if os.path.exists(output_filename):
            print(f"Error: The file {output_filename} already exists.")
            continue
        
        try:
            with open(output_filename, 'w') as file:
                file.write(invitation)
        except Exception as e:
            print(f"Error: Impossible to write to the file {output_filename}. Exception: {e}")
