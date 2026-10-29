# Caught violation and remediation

The interactor in `study_room_booking/use_cases/book_study_room.py` originally included this **deliberate** import at line 5:

```python
from study_room_booking.frameworks_and_drivers.in_memory_booking_gateway import InMemoryBookingGateway  # INTENTIONAL AUDIT VIOLATION
```

This was a violation even though the name was unused: the use-case circle would name an outer implementation detail. The auto-audit flagged it (7 imports, 1 violation). The fix was to remove that import, leaving `BookingGateway` defined in `use_cases/boundaries.py`. The outer `main.py` supplies the concrete `InMemoryBookingGateway` when it constructs the interactor. Thus storage can change without an inward import.

Files proving sequence: first audit, before-fix code, patch, final audit, console run, 6 tests.
