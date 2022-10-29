"""Generate a database from the csv-parsed data"""

import sqlite_utils


def create_tables(db):
    """Create the DB tables for attendance"""
    db["users"].create(
        {"name": str, "rank": str, "member_since": str, "country": str}, pk="name"
    )
    db["operations"].create(
        {
            "date": str,
            "attendance_counts": bool,  # For Anniversary, Xmas...
            "attendance_recorded": str,  # Per above, str even if should be integer
        },
        pk="date",
    )
    db["attendance"].create(
        {"operation_date": str, "user": str, "role": str},
        pk=("operation_date", "user"),
        foreign_keys=[
            ("operation_date", "operations", "date"),
            ("user", "users", "name"),
        ],
    )


def populate(db_path, users, dates):
    """Populate the database of users"""
    db = sqlite_utils.Database(db_path)
    create_tables(db)
    for user_name, user_details in users.items():
        db["users"].insert(
            {
                "name": user_name,
                # FIXME Remove need for CSV header (interface to CSV)
                "rank": user_details["All attendance"],
                "member_since": user_details["Member since"],
                "country": user_details["Country"],
            }
        )
    for op_date, op_details in dates.items():
        db["operations"].insert(
            {
                "date": op_date.isoformat(),
                "attendance_counts": op_details["recorded_attendees"].isdigit(),
                "attendance_recorded": op_details["recorded_attendees"],
            }
        )
        for user_name, user_role in op_details["attendees"].items():
            db["attendance"].insert(
                {
                    "operation_date": op_date.isoformat(),
                    "user": user_name,
                    "role": user_role,
                }
            )
