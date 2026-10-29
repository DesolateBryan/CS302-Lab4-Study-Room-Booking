# Dependency Rule: use cases may depend on entities and stable Python types only; never outer adapters or drivers.
# Input and output contracts belong to the use-case layer.
from dataclasses import dataclass
from typing import Protocol
from study_room_booking.entities.study_room_reservation import StudyRoomReservation


@dataclass(frozen=True)
class BookingRequest:
    student_id: str
    room_id: str
    day: str
    start_hour: int
    duration_hours: int


@dataclass(frozen=True)
class BookingResponse:
    success: bool
    message: str
    confirmation: str = ""
    room_id: str = ""
    day: str = ""
    start_hour: int = 0
    duration_hours: int = 0


class BookingInputBoundary(Protocol):
    def execute(self, request: BookingRequest) -> None: ...


class BookingOutputBoundary(Protocol):
    def present(self, response: BookingResponse) -> None: ...


class BookingGateway(Protocol):
    def next_confirmation(self) -> str: ...
    def has_overlap(self, reservation: StudyRoomReservation) -> bool: ...
    def save(self, reservation: StudyRoomReservation) -> None: ...
