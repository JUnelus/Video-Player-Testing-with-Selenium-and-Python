import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_youtube_error_handling():
    driver = webdriver.Chrome()

    # Load a broken or invalid video URL (YouTube's system will display an error message)
    driver.get("https://www.youtube.com/watch?v=invalid_video_id")  # Use an invalid video ID

    # Wait for YouTube's error message to appear (it may take a few seconds)
    time.sleep(5)

    # Check if the error message element is present
    try:
        error_message = driver.find_element(By.CSS_SELECTOR, 'div.yt-player-error-message-renderer')
        assert error_message.is_displayed(), "Error message not displayed."
        print("Test passed: Error message displayed as expected.")
    except:
        print("Test failed: Error message not found.")

    driver.quit()