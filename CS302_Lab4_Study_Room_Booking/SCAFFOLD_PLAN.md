# Structure explanation — written before the source code

**Use case:** A student reserves a study room for a date and one- or two-hour window. This is a standalone sandbox, not the team CuraAI project.

**Dependency Rule:** Source-code dependencies point inward only. Entities know no other project layer. Use cases know entities and their own input/output contracts, not concrete storage or UI. Interface adapters depend on the use-case contracts, translating console strings to requests and results to a view model. Frameworks and drivers implement persistence and run the console.

Four circles, from inside out:

1. `study_room_booking/entities/` — `StudyRoomReservation` validates booking details and detects time overlap, without knowing storage or console.
2. `study_room_booking/use_cases/` — `BookStudyRoomInteractor` runs the booking policy through input/output boundaries. `BookingGateway` is a storage interface **defined here**, not in the outer storage layer.
3. `study_room_booking/interface_adapters/` — `BookingController` converts console inputs to a request; `BookingPresenter` converts a response to `BookingViewModel`.
4. `study_room_booking/frameworks_and_drivers/` — `InMemoryBookingGateway` stores reservations; `console_view` prints the view model; `main` wires dependencies together.

**Vertical slice:** console main → BookingController → BookStudyRoomInteractor (input boundary) → StudyRoomReservation → BookingOutputBoundary → BookingPresenter → BookingViewModel → console view.

**Expected result:** First booking succeeds. Rebooking an overlapping window for the same room/day fails. There is no framework dependency in the entity or interactor, and all storage is in memory.

This explanation was established before writing the files below, in response to the adapted class scaffold prompt (see `PROMPT_APPENDIX.md`).
