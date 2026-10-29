# Dependency Rule: interface adapters may import use cases/entities, never require an inner layer to import them.
# Presenter: convert use-case data into a display-ready view model.
from dataclasses import dataclass
from study_room_booking.use_cases.boundaries import BookingResponse


@dataclass(frozen=True)
class BookingViewModel:
    status: str
    headline: str
    details: str


class BookingPresenter:
    def __init__(self):
        self.view_model = BookingViewModel("", "", "")

    def present(self, response: BookingResponse) -> None:
        if response.success:
            self.view_model = BookingViewModel(
                "SUCCESS", response.message,
                f"Confirmation: {response.confirmation} | Room: {response.room_id} | "
                f"Date: {response.day} | Time: {response.start_hour:02}:00-"
                f"{response.start_hour + response.duration_hours:02}:00",
            )
        else:
            self.view_model = BookingViewModel("FAILED", response.message, "No reservation created.")
