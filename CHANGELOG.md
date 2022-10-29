# Changelog for ZeusOps Attendance Analysis


The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
The project uses semantic versioning (see [semver](https://semver.org)).

## [Unreleased]


## v0.2.0 - 2022-10-29

### Added
- Parse an attendance CSV file via `make attendance.db` (needs `attendance.csv`)
- Serve sqlite DB via `make serve`, using `datasette`


## v0.1.0 - 2022-10-28
### Added
- New python module `zeusops_attendance_analysis`, exposed as shell command `zeusops-attendance-analysis`
