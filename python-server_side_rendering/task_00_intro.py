def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return
    
    if not template:
        print("The template is empty, no output files generated")
        return
    if not attendees:
        print("No data provided, no output files generated")
        return
    for i, attendee in enumerate(attendees, start=1):
        output_content = template.format(
            name=attendee.get('name', 'N/A'),
            event_title=attendee.get('event_title', 'N/A'),
            event_date=attendee.get('event_date', 'N/A'),
            event_location=attendee.get('event_location', 'N/A')
        )

        output_filename = f'output_{i}.txt'
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(output_content)
            print(f"Generated {output_filename}")
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")

    if __name__ == "__main__":
        with open('template.txt', 'r') as file:
            template_content = file.read()
    
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    generate_invitations(template_content, attendees)