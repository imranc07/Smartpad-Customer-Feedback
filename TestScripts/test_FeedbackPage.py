"""
test_FeedbackPage.py

This module contains the test cases for the Feedback page of the smartpad customer feedback application.
"""

from PageObjects.FeedbackPage import FeedbackPage
import pytest


# Test case TC01 for Valid submission
@pytest.mark.order(1)
def test_TC01_valid_submission():
    feedback_page = FeedbackPage()
    feedback_page.start()
    success_message = feedback_page.valid_submission()
    assert success_message == "Thankyou!"
    print("Test_TC01_valid_submission: PASS")

    feedback_page.shutdown()


# Test case TC02 for Invalid email submission
@pytest.mark.order(2)
def test_TC02_invalid_email():
    feedback_page = FeedbackPage()
    feedback_page.start()
    error_message = feedback_page.invalid_email_submission()
    assert error_message == "Please enter a valid email"
    print("Test_TC02_invalid_email: PASS")
    feedback_page.shutdown()

# Test case TC03 for Empty form submission
@pytest.mark.order(3)
def test_TC03_empty_submission():
    feedback_page = FeedbackPage()
    feedback_page.start()
    error_message = feedback_page.empty_submission()
    assert error_message == "Please give a rating"
    print("Test_TC03_empty_submission: PASS")
    feedback_page.shutdown()
