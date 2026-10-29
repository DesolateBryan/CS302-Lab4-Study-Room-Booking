"""Presenter-only unit tests; no GUI or console imports (Humble Object split)."""
import unittest
from study_room_booking.interface_adapters.booking_presenter import BookingPresenter
from study_room_booking.use_cases.boundaries import BookingResponse


class BookingPresenterTests(unittest.TestCase):
    def test_success_view_model(self):
        presenter = BookingPresenter()
        presenter.present(BookingResponse(True, "Study room reserved.", "SR-0001", "LIB-201", "2026-10-29", 14, 2))
        self.assertEqual(presenter.view_model.status, "SUCCESS")
        self.assertIn("SR-0001", presenter.view_model.details)
        self.assertIn("14:00-16:00", presenter.view_model.details)

    def test_failure_view_model(self):
        presenter = BookingPresenter()
        presenter.present(BookingResponse(False, "Already booked."))
        self.assertEqual(presenter.view_model.status, "FAILED")
        self.assertIn("No reservation", presenter.view_model.details)


if __name__ == "__main__":
    unittest.main()
