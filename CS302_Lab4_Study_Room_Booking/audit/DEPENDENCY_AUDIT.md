# Dependency audit — final code

**Scope:** Every import in both inner layers, `entities` and `use_cases`, including package `__init__.py` files (which have no imports).

**Initial intentionally inserted failure:** 7 imports / 1 violation; `study_room_booking/use_cases/book_study_room.py:5` imported an outer concrete gateway. Removed as documented in `audit/evidence/violation_fix.diff`.

**Final state:** 6 imports / 0 violations. Python `dataclasses` and `typing` are stable standard-library types and are permitted under page 3 of the lab handout.

| File | Line | Import | Which circle? | Verdict |
|---|---:|---|---|---|
| study_room_booking/entities/study_room_reservation.py | 3 | from dataclasses import dataclass | stable Python standard library | inward / stable - OK |
| study_room_booking/use_cases/book_study_room.py | 3 | from study_room_booking.entities.study_room_reservation import StudyRoomReservation | inner - entities | inward / stable - OK |
| study_room_booking/use_cases/book_study_room.py | 4 | from study_room_booking.use_cases.boundaries import BookingRequest, BookingResponse, BookingGateway, BookingOutputBoundary | use cases | inward / stable - OK |
| study_room_booking/use_cases/boundaries.py | 3 | from dataclasses import dataclass | stable Python standard library | inward / stable - OK |
| study_room_booking/use_cases/boundaries.py | 4 | from typing import Protocol | stable Python standard library | inward / stable - OK |
| study_room_booking/use_cases/boundaries.py | 5 | from study_room_booking.entities.study_room_reservation import StudyRoomReservation | inner - entities | inward / stable - OK |

**Argument from the table:** The entity only imports `dataclasses`; the interactor imports entity and use-case boundary modules; and the use-case boundary imports stable Python utilities and the entity. No inner-layer import names `interface_adapters` or `frameworks_and_drivers`. The real persistence class is supplied by the outer composition root.
