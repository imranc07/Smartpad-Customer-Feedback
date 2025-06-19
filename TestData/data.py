"""
data.py

contains the test data for the Feedback page of the smartpad customer feedback application.

"""


class FeedbackPageData:
    """
    This class contains the test data for the Feedback page.
    """

    # URL of the Feedback page
    url = "https://smartpad-customer-feedback.vercel.app/"

    # Sample feedback data
    name = "Lara Croft"
    email = "lara.croft@tombraider.com"
    invalid_email = "lara.croft@tombraider"
    feedback = "Great service!"