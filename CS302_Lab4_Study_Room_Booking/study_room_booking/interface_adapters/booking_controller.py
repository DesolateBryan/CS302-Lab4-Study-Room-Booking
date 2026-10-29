# Dependency Rule: interface adapters may call the use-case input boundary, never the opposite direction.
# Controller: translate external input to a use-case request.
from study_room_booking.use_cases.boundaries import BookingInputBoundary, BookingRequest
from study_room_booking.interface_adapters.booking_presenter import BookingPresenter, BookingViewModel


class BookingController:
    def __init__(self, input_boundary: BookingInputBoundary, presenter: BookingPresenter):
        self._input_boundary = input_boundary
        self._presenter = presenter

    def book(self, student: str, room: str, day: str, start_hour: int,
             duration_hours: int) -> BookingViewModel:
        request = BookingRequest(student, room, day, start_hour, duration_hours)
        self._input_boundary.execute(request)
        return self._presenter.view_model
