# Dependency Rule: use cases may import entities and use-case contracts, never concrete outer storage or UI.
# Interactor: one complete booking request, independent of any framework.
from study_room_booking.entities.study_room_reservation import StudyRoomReservation
from study_room_booking.use_cases.boundaries import BookingRequest, BookingResponse, BookingGateway, BookingOutputBoundary


class BookStudyRoomInteractor:
    def __init__(self, gateway: BookingGateway, output: BookingOutputBoundary):
        self._gateway = gateway
        self._output = output

    def execute(self, request: BookingRequest) -> None:
        try:
            reservation = StudyRoomReservation.create(
                self._gateway.next_confirmation(),
                request.student_id, request.room_id, request.day,
                request.start_hour, request.duration_hours,
            )
        except ValueError as exc:
            self._output.present(BookingResponse(False, str(exc)))
            return

        if self._gateway.has_overlap(reservation):
            self._output.present(BookingResponse(False, "That study room is already booked for those hours."))
            return

        self._gateway.save(reservation)
        self._output.present(BookingResponse(
            True, "Study room reserved.", reservation.confirmation,
            reservation.room_id, reservation.day,
            reservation.start_hour, reservation.duration_hours,
        ))
