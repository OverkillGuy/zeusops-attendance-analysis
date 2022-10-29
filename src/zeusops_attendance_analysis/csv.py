"""Processing the attendance sheet as CSV"""

import csv
from datetime import date

GLOBAL_FIELDS = [
    "All attendance",
    "Name",
    "Member since",
    "Years #",
    "Country",
    "Apex",
    "Previous Rank",
    "Total %",
    "Signoff %",
    "Overall Attendance",
    "Overall Signoffs",
    "Overall ABSENT",
    "Overall T1 roles",
    "Overall T2 roles",
    "Month %",
    "T1",
    "T1+T2",
    "Rank Δ",
]
USER_FIELDS_COUNT = 5  # First X fields of headers are immutable details of the user
DATE_FIELDS_START_INDEX = len(GLOBAL_FIELDS)

# User = NamedTuple("User", ["name", "rank", "member_since" "country"])
# Operation = NamedTuple("Operation", ["date", "attendance_counts", "attendance_recorded" "attendance_details"])


def read(csv_file):
    """Read the given CSV"""
    users = {}
    reader = csv.DictReader(csv_file)
    headers = list(next(reader).keys())
    second_line = list(next(reader).values())
    for row in reader:
        users[row["Name"]] = row
    return headers, second_line, users


def process_operations(headers, second_line, users):
    """Iterate over each operation's attendance sheet"""
    op_dates_str = headers[DATE_FIELDS_START_INDEX:]
    attendees_total = second_line[DATE_FIELDS_START_INDEX:]
    dates = {}
    for op_date_str, op_attendees in zip(op_dates_str, attendees_total):
        day, month, year = op_date_str.split("/")
        op_date = date(int(year), int(month), int(day))
        dates[op_date] = {"recorded_attendees": op_attendees, "attendees": {}}
        for user_name, data in users.items():
            user_at_op = data[op_date_str]
            if user_at_op not in ["", "ABSENT", "ON LEAVE"]:  # FIXME: Any other weird?
                dates[op_date]["attendees"][user_name] = user_at_op
        dates[op_date]["computed_attendees"] = str(len(dates[op_date]["attendees"]))
        if dates[op_date]["computed_attendees"] != dates[op_date]["recorded_attendees"]:
            top_row, counted_present = (
                dates[op_date]["recorded_attendees"],
                dates[op_date]["computed_attendees"],
            )
            print(
                f"Mismatched attendees for {op_date.isoformat()}: "
                f"header says {top_row}, but counted {counted_present}"
            )
    return dates
