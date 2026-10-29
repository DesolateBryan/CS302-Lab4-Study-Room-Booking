"""Use-case tests use only the Python standard library, no UI framework."""
import unittest
from study_room_booking.use_cases.boundaries import BookingRequest
from study_room_booking.use_cases.book_study_room import BookStudyRoomInteractor
from study_room_booking.interface_adapters.booking_presenter import BookingPresenter
from study_room_booking.frameworks_and_drivers.in_memory_booking_gateway import InMemoryBookingGateway


class BookStudyRoomTests(unittest.TestCase):
    def setUp(self):
        self.gateway = InMemoryBookingGateway()
        self.presenter = BookingPresenter()
        self.interactor = BookStudyRoomInteractor(self.gateway, self.presenter)

    def test_successful_booking(self):
        self.interactor.execute(BookingRequest("JU123", "LIB-201", "2026-10-29", 14, 2))
        self.assertEqual(self.presenter.view_model.status, "SUCCESS")
        self.assertEqual(len(self.gateway.reservations), 1)

    def test_overlap_does_not_book_twice(self):
        self.interactor.execute(BookingRequest("JU123", "LIB-201", "2026-10-29", 14, 2))
        self.interactor.execute(BookingRequest("JU456", "LIB-201", "2026-10-29", 15, 1))
        self.assertEqual(self.presenter.view_model.status, "FAILED")
        self.assertEqual(len(self.gateway.reservations), 1)

    def test_different_room_is_allowed(self):
        self.interactor.execute(BookingRequest("JU123", "LIB-201", "2026-10-29", 14, 2))
        self.interactor.execute(BookingRequest("JU456", "LIB-202", "2026-10-29", 15, 1))
        self.assertEqual(self.presenter.view_model.status, "SUCCESS")
        self.assertEqual(len(self.gateway.reservations), 2)

    def test_invalid_duration(self):
        self.interactor.execute(BookingRequest("JU123", "LIB-201", "2026-10-29", 14, 3))
        self.assertEqual(self.presenter.view_model.status, "FAILED")
        self.assertEqual(len(self.gateway.reservations), 0)


if __name__ == "__main__":
    unittest.main()
