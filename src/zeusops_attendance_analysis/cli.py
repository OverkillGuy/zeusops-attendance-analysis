"""Command line entrypoint for zeusops-attendance-analysis"""
import argparse
import sys
from typing import Optional

from zeusops_attendance_analysis import csv, database


def parse_arguments(arguments: list[str]) -> argparse.Namespace:
    """Parse generic arguments, given as parameters"""
    parser = argparse.ArgumentParser(
        "zeusops-attendance-analysis",
        description="Data analysis on the Zeusops ArmA unit attendance sheet",
    )
    parser.add_argument(
        "attendance_csv",
        help="Attendance sheet CSV file",
        type=argparse.FileType(mode="r"),
    )
    parser.add_argument("attendance_db", help="Name of the database file to create")
    return parser.parse_args(arguments)


def cli(arguments: Optional[list[str]] = None):
    """Run the zeusops_attendance_analysis cli"""
    if arguments is None:
        arguments = sys.argv[1:]
    args = parse_arguments(arguments)
    main(args.attendance_csv, args.attendance_db)


def main(attendance_csv, attendance_db):
    """Run the program's main command"""
    headers, second_line, users = csv.read(attendance_csv)
    dates = csv.process_operations(headers, second_line, users)
    database.populate(attendance_db, users, dates)
