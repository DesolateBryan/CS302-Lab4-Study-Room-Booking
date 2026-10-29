# Study Room Booking — CS302 Lab 4

A tiny, runnable Clean Architecture application for **booking a study room**. The feature is purposefully narrow: book a room for a given date, start hour, and one- or two-hour duration; reject overlapping reservations. 
## Why this folder structure?

The root package and its files shout **study room booking**, not Flask, Django, SQL, or some generic template. The four circles are:

```text
study_room_booking/
├── entities/                 StudyRoomReservation: validation + overlapping-time policy
├── use_cases/                BookingRequest/Response, input/output boundaries, gateway port, interactor
├── interface_adapters/       BookingController, BookingPresenter, BookingViewModel
└── frameworks_and_drivers/   InMemoryBookingGateway, console view, main composition root
```

The Dependency Rule is stated at the top of each layer's Python source files. The central rule is **inner layers cannot depend on outer implementation details**. The outer in-memory adapter implements the gateway port defined by the use-case layer.

## Run the complete vertical slice

Requires **Python 3.10 or later**; no packages to install (standard library only). From the project root:

```bash
python -m study_room_booking.frameworks_and_drivers.main
```

Expected output:

```text
[SUCCESS] Study room reserved.
  Confirmation: SR-0001 | Room: LIB-201 | Date: 2026-10-29 | Time: 14:00-16:00
[FAILED] That study room is already booked for those hours.
  No reservation created.
```

The first flow is: `main → BookingController → BookingInputBoundary (interactor) → StudyRoomReservation → BookingOutputBoundary → BookingPresenter → BookingViewModel → print_view`. The second demonstrates a conflict.

## Tests (including optional presenter-only tests)

```bash
python -m unittest discover -s tests -v
```

Six tests cover success, conflict, different room, invalid duration, and both presenter states. The two presenter tests import **no UI module**. The successful run is saved at `audit/evidence/test_run.txt`.

## Dependency audit

```bash
python audit/check_dependency_rule.py --csv
```

The script enumerates every `import` and `from ... import` in the **entities** and **use_cases** layers and classifies the named circle. Final results: **6 imports audited, 0 violations**. The violation was an import of concrete in-memory storage inside `book_study_room.py` **at line 5**. It was caught and deleted; see `audit/evidence/first_audit_before_fix.txt`, `audit/evidence/book_study_room_BEFORE_FIX.py`, `audit/evidence/violation_fix.diff`, and `audit/evidence/final_audit_after_fix.txt`.

The violation was **deliberately inserted for the audit exercise**, as allowed by Lab Part 3 when the scaffold would otherwise be clean. It wasn't a natural AI error; the memo says so plainly.

## Assignment deliverables

- `CS302_Lab4_Audit_Memo.pdf` — one-page audit memo (GitHub URL field to fill after publishing).
- `audit/DEPENDENCY_AUDIT.md`, `audit/dependency_audit.csv`, `CS302_Lab4_Audit_Table.pdf` — all final inner-layer imports and their verdicts.
- `PROMPT_APPENDIX.md`, `CS302_Lab4_Prompt_Appendix.pdf` — ordered, attributed self-directed AI prompts.
- `SCAFFOLD_PLAN.md` — structure explanation produced **before** writing code.
- `audit/evidence/` — before/after source, caught violation, patch, tests, console output.

## Publish to GitHub and submit

1. On GitHub, create a new public or private repository named `study-room-booking-cs302-lab4` (as permitted by your professor).
2. Extract the downloaded ZIP. Upload the **contents** of `CS302_Lab4_Study_Room_Booking/` to the repository root (do not upload the ZIP as one file).
3. Copy the GitHub repository URL into the memo at the indicated placeholder before submitting it, and re-export the memo PDF if you edit its source text.
4. Submit the **GitHub repo link + one-page memo + audit table + prompt appendix** in Blackboard.

Alternatively, with Git installed and a new empty GitHub repo already created:

```bash
git init
git add .
git commit -m "CS302 Lab 4: study room booking Clean Architecture"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/study-room-booking-cs302-lab4.git
git push -u origin main
```

