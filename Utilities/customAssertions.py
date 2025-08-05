def assert_with_screenshot(driver, actual, expected, message, screenshot_path):
    """
    Asserts actual == expected and saves screenshot if assertion fails.

    :param driver: WebDriver instance
    :param actual: Actual result
    :param expected: Expected result
    :param message: Message to show in assertion error
    :param screenshot_path: Path to save screenshot if assertion fails
    """
    try:
        assert actual == expected, message
    except AssertionError as e:
        driver.save_screenshot(screenshot_path)
        raise e
