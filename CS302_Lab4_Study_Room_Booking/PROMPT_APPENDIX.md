# CS302 Lab 4 — Prompt Appendix (in order)


## Prompt 1 — Adapted class scaffold prompt

> Scaffold a project for **booking a study room** with four layers: entities, use cases, interface adapters, frameworks & drivers. State the Dependency Rule as a comment at the top of each layer. No framework imports inside the inner two layers. Use an in-memory gateway implementation for persistence. **Explain the structure before writing the code.** 

**Response / result:** The four-layer structure, dependency direction, and intended round trip were explained in `SCAFFOLD_PLAN.md` **before** writing the Python source files. The folder and file names use study-room-booking vocabulary. **No framework-template redirection was needed.**

## Prompt 2 — Implement one thin vertical slice

> Write the minimal working path: console → booking controller → input boundary → book-study-room interactor → reservation entity → output boundary → booking presenter → view model → console print. Use a replaceable `BookingGateway` protocol in the use-case layer and an in-memory implementation in the outer layer. Show a successful booking and reject an overlapping booking.

**Response / result:** `study_room_booking/` contains the working slice. Its captured output is `audit/evidence/console_run.txt`.

## Prompt 3 — Include optional humble-presenter tests

> Make plain `unittest` tests for the presenter that do not import a GUI or console module. Also test a successful booking, an overlapping booking, another room, and an invalid duration. Run the tests.

**Response / result:** Six tests all passed. See `tests/` and `audit/evidence/test_run.txt`.

## Prompt 4 — Prepare an explicitly controlled Dependency Rule failure

> Because the proposed clean scaffold otherwise has no outward import, **deliberately insert** the classic incorrect dependency: import the concrete `InMemoryBookingGateway` from `frameworks_and_drivers` inside the use-case interactor. Preserve that file for evidence, and be transparent that this failure was inserted for the lab audit.

**Response / result:** The intentionally wrong import appeared on **line 5** of `study_room_booking/use_cases/book_study_room.py`. The full before-fix version is preserved under `audit/evidence/book_study_room_BEFORE_FIX.py`.

## Prompt 5 — Audit every import and catch the problem

> Audit each import or using statement in the entities and use-cases circles. List the file, line, import, circle named, and inward-or-violation verdict. Save the first audit and report the failure rather than hiding it.

**Response / result:** `audit/check_dependency_rule.py` detected **7 imports, 1 violation**, and returned a nonzero exit status. See `audit/evidence/first_audit_before_fix.txt`.

## Prompt 6 — Fix, rerun, and write the deliverables

> Remove the outward concrete-gateway import while leaving `BookingGateway` injected as a use-case port. Rerun the whole round trip, dependency audit, and tests. Produce a complete final audit table and a one-page memo with the scream test, counts, line reference, fix, Dependency Rule argument, and AI attribution. Do not make up a GitHub link.

**Response / result:** Final audit: **6 imports, 0 violations**. Successful console run and six passing tests are recorded. The final code still uses the gateway protocol for dependency inversion. The memo includes an unfilled GitHub URL field because no repository has been published.

