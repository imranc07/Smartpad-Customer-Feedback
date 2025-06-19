"""
FeedbackPage.py

This module contains the Page Object for the Feedback page of the smartpad customer feedback application.

"""

# import necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Exception Handling
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException

# Webdriver wait utilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Importing Test Locators and Test Data
from TestLocators.locators import FeedbackPageLocators
from TestData.data import FeedbackPageData

class FeedbackPage:

    def __init__(self):
        """
        Initializes the WebDriver and sets up explicit wait.
        """
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 50)

 
    def start(self):
        """
        Navigates to the Feedback page.

        """
        self.driver.get(FeedbackPageData.url)
        self.driver.maximize_window()

    def _navigate_to_feedback_form(self):
        """
        Helper method to navigate to the feedback form by clicking common initial buttons.
        This reduces code duplication submission methods.
        """
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, FeedbackPageLocators.get_started_button_locator))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, FeedbackPageLocators.beer_locator))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, FeedbackPageLocators.without_login_button_locator))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, FeedbackPageLocators.age_declaration_locator))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, FeedbackPageLocators.affigem_locator))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, FeedbackPageLocators.share_feedback_button_locator))).click()
        except (NoSuchElementException, TimeoutException, ElementClickInterceptedException) as e:
            print(f"Error navigating to feedback form: {e}")
            raise # Re-raise the exception to fail the test if navigation fails


    def valid_submission(self):
        """
        Submits valid feedback.

        Returns:
            str: The success message displayed after submission.
        """
        self._navigate_to_feedback_form()

        self.wait.until(EC.visibility_of_element_located((By.XPATH, FeedbackPageLocators.name_locator))).send_keys(FeedbackPageData.name)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, FeedbackPageLocators.email_locator))).send_keys(FeedbackPageData.email)
        self.driver.find_element(By.XPATH, FeedbackPageLocators.rating_locator).click() # Click is fine here if it's always clickable
        self.wait.until(EC.visibility_of_element_located((By.XPATH, FeedbackPageLocators.comment_locator))).send_keys(FeedbackPageData.feedback)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, FeedbackPageLocators.submit_button_locator))).click()

        try:
            self.wait.until(EC.text_to_be_present_in_element((By.XPATH, FeedbackPageLocators.success_message), "Thankyou!"))
            success_message = self.driver.find_element(By.XPATH, FeedbackPageLocators.success_message).text
            return success_message

        except TimeoutException:
            return "Success message not found or incorrect."

        except NoSuchElementException:
            return "Success message element not found."


    def invalid_email_submission(self):
        """
        Submits feedback with an invalid email.

        Returns:
            str: The error message displayed for invalid email.
        """
        self._navigate_to_feedback_form()

        self.wait.until(EC.visibility_of_element_located((By.XPATH, FeedbackPageLocators.name_locator))).send_keys(FeedbackPageData.name)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, FeedbackPageLocators.email_locator))).send_keys(FeedbackPageData.invalid_email)
        self.driver.find_element(By.XPATH, FeedbackPageLocators.rating_locator).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, FeedbackPageLocators.comment_locator))).send_keys(FeedbackPageData.feedback)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, FeedbackPageLocators.submit_button_locator))).click()

        try:
            self.wait.until(EC.text_to_be_present_in_element((By.XPATH, FeedbackPageLocators.feedback_error), "Please enter a valid email"))
            error_message = self.driver.find_element(By.XPATH, FeedbackPageLocators.feedback_error).text
            return error_message
        
        except TimeoutException:
            return "Error message for invalid email not found or incorrect."
        except NoSuchElementException:
            return "Error message element not found."


    def empty_submission(self):
        """
        Submits empty feedback.

        Returns:
            str: The error message displayed for empty submission.
        """
        self._navigate_to_feedback_form()

        self.wait.until(EC.visibility_of_element_located((By.XPATH, FeedbackPageLocators.name_locator))).click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, FeedbackPageLocators.submit_button_locator))).click()

        try:
            self.wait.until(EC.text_to_be_present_in_element((By.XPATH, FeedbackPageLocators.feedback_error), "Please give a rating"))
            error_message = self.driver.find_element(By.XPATH, FeedbackPageLocators.feedback_error).text
            return error_message

        except TimeoutException:
            return "Error message for empty submission not found or incorrect."

        except NoSuchElementException:
            return "Error message element not found."

    def shutdown(self):
        """
        Closes the Webdriver.
        """
        self.driver.quit()
