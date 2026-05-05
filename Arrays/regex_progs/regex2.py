
import re
import os
from collections import Counter

class A:

    def parse_log_line(self, line):

        """

            Parses a single log line and extracts timestamp, level, component, and message.

            Example line: '2023-10-26 10:00:15 ERROR Engine: High temperature alert! Temp=105C.'

            Returns a dictionary or None if parsing fails.

            Example: {'timestamp': '2023-10-26 10:00:01', 'component': 'Engine', 'level': 'INFO', 'message': 'Engine started successfully.'}

            """

        pattern = re.compile(

            r'^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) '

            r'(?P<level>[A-Z]+) '

            r'(?P<component>[^:]+): '

            r'(?P<message>.+)$'

        )

        match = pattern.match(line)

        if match:

            return match.groupdict()

        return None


    def analyze_component_errors(self, log_entries):
        # Example Output: {'Engine': 2, 'Infotainment': 1, 'Brakes': 5}

        if log_entries["component"]=='Engine':



        pass

    def get_events_by_level(log_entries, level):

        """

        Filters a list of log entries and returns a new list containing only

        entries that match the specified log level.

        The 'level' parameter should be case-insensitive (e.g., 'error' should match 'ERROR').

        Returns a list of dictionaries (log entries).

        """
        

    pass

    def read_log_file(self, filepath):
        # component_counts = Counter()
       
        """

        Reads a log file, parses each line, and returns a list of parsed log entries.

        Ignores lines that cannot be parsed.

        Example Output: [{'timestamp': '2023-10-26 10:00:01', 'component': 'Engine', 'level': 'INFO', 'message': 'Engine started successfully.'},{...},{...}]

        """    
        with open(filepath, 'r') as f:
            for line in f:
                log1=self.parse_log_line(line)
                # print(log1)
        
        self.analyze_component_errors(log1)

        #         # Remove whitespace and split line into words

        #         parts = line.strip().split()

        #         # Check if line has at least 3 parts (date, time, component)

        #         if len(parts) >= 3:

        #         # Extract the component name (3rd word)

        #             component = parts[2]
        #             # print(component)

        #         # # Add 1 to this component's count

        #             component_counts[component] += 1
        # print(component_counts)
        # # Loop through components sorted by count (highest first)

        # for component, count in component_counts.most_common():

        #     # Print each component and its count

        #     print(f"{component}: {count}")




if __name__ == "__main__":
    
    # Get the folder path where this script is saved
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Build the full path to the log file
    log_file_path = os.path.join(script_dir, 'error.txt')

    a=A()
    a.read_log_file(log_file_path)

   