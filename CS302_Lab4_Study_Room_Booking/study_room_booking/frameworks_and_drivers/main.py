# Dependency Rule: the outer composition root wires all layers without making inner layers depend outward.
from study_room_booking.frameworks_and_drivers.in_memory_booking_gateway import InMemoryBookingGateway
from study_room_booking.frameworks_and_drivers.console_view import print_view
from study_room_booking.interface_adapters.booking_presenter import BookingPresenter
from study_room_booking.interface_adapters.booking_controller import BookingController
from study_room_booking.use_cases.book_study_room import BookStudyRoomInteractor


def main() -> None:
    gateway = InMemoryBookingGateway()
    presenter = BookingPresenter()
    interactor = BookStudyRoomInteractor(gateway, presenter)
    controller = BookingController(interactor, presenter)

    # Two round trips: a valid booking, then a blocked overlapping booking.
    print_view(controller.book("JU123", "LIB-201", "2026-10-29", 14, 2))
    print_view(controller.book("JU456", "LIB-201", "2026-10-29", 15, 1))


if __name__ == "__main__":
    main()
