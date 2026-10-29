# Dependency Rule: outer frameworks/drivers may import inner entities and contracts, but inner layers must not import this module.
# Persistence detail: replaceable in-memory storage adapter.
from study_room_booking.entities.study_room_reservation import StudyRoomReservation


class InMemoryBookingGateway:
    def __init__(self):
        self._reservations: list[StudyRoomReservation] = []
        self._sequence = 0

    def next_confirmation(self) -> str:
        self._sequence += 1
        return f"SR-{self._sequence:04}"

    def has_overlap(self, reservation: StudyRoomReservation) -> bool:
        return any(reservation.overlaps(existing) for existing in self._reservations)

    def save(self, reservation: StudyRoomReservation) -> None:
        self._reservations.append(reservation)

    @property
    def reservations(self) -> tuple[StudyRoomReservation, ...]:
        return tuple(self._reservations)
