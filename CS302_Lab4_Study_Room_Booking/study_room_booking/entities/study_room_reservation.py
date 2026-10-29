# Dependency Rule: entities must not import use cases, adapters, or frameworks.
# Entity: a study-room reservation and its simple booking policies.
from dataclasses import dataclass


@dataclass(frozen=True)
class StudyRoomReservation:
    confirmation: str
    student_id: str
    room_id: str
    day: str
    start_hour: int
    duration_hours: int

    @classmethod
    def create(cls, confirmation: str, student_id: str, room_id: str,
               day: str, start_hour: int, duration_hours: int):
        if not student_id.strip() or not room_id.strip() or not day.strip():
            raise ValueError("Student, room, and date are required.")
        if not (8 <= start_hour <= 21):
            raise ValueError("Start hour must be between 8 and 21.")
        if duration_hours not in (1, 2) or start_hour + duration_hours > 22:
            raise ValueError("Bookings must be 1 or 2 hours and end by 22:00.")
        return cls(confirmation, student_id.strip(), room_id.strip().upper(),
                   day.strip(), start_hour, duration_hours)

    def overlaps(self, other: "StudyRoomReservation") -> bool:
        return (self.room_id == other.room_id
                and self.day == other.day
                and self.start_hour < other.start_hour + other.duration_hours
                and other.start_hour < self.start_hour + self.duration_hours)
