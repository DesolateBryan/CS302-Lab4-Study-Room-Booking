# Dependency Rule: outer console view depends on a view model, not the other way around.
from study_room_booking.interface_adapters.booking_presenter import BookingViewModel


def print_view(model: BookingViewModel) -> None:
    print(f"[{model.status}] {model.headline}")
    print(f"  {model.details}")
