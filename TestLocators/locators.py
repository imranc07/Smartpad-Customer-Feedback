"""
locators.py

This module contains the locators for the Feedback page of the smartpad customer feedback application.
"""

class FeedbackPageLocators:
    """
    This class contains the locators for the Feedback page.
    """

    # Locators for the Feedback form fields
    get_started_button_locator = "/html/body/div/div[1]/div/div[2]/div[3]/div"
    beer_locator = "//div[contains(text(), 'Beer')]"
    without_login_button_locator = '//div[contains(text(),"Continue without an account")]'
    age_declaration_locator = "//button[contains(text(), 'Yes')]"
    affigem_locator = "//h2[contains(text(), 'Affigem')]"
    share_feedback_button_locator = '//p[contains(text(),"Share Feedback")]'
    name_locator = "//input[@placeholder='Type your name here...']"
    email_locator = "//input[@placeholder='Type your email here...']"
    rating_locator = "/html/body/div/div[2]/div/div[3]/div/div[5]/p"
    comment_locator = "//textarea[@placeholder='Type your comments here...']"

    # Locators for the buttons
    submit_button_locator = '//div[@role="button"]'

    # Locators for error messages
    feedback_error = "//div[@role='status']" # Please give a rating, Please enter your name, Please enter your email
    success_message = "//div[text()='Thankyou!']" # Success message after valid submission