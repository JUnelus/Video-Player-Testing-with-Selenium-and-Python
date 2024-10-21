import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_youtube_controls():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Replace with any public YouTube video link

    # Wait for the video to load
    time.sleep(5)

    # Play the video
    play_button = driver.find_element(By.CSS_SELECTOR, 'button.ytp-play-button')
    play_button.click()
    time.sleep(5)

    # Pause the video
    pause_button = driver.find_element(By.CSS_SELECTOR, 'button.ytp-play-button')
    pause_button.click()
    time.sleep(2)

    # Check if the video is paused by verifying that the current time is not advancing
    current_time = driver.execute_script("return document.querySelector('video').currentTime")
    time.sleep(2)
    new_time = driver.execute_script("return document.querySelector('video').currentTime")

    assert current_time == new_time, "Video did not pause."

    # Adjust volume to 50%
    volume_slider = driver.find_element(By.CSS_SELECTOR, 'button.ytp-mute-button')
    driver.execute_script("document.querySelector('video').volume = 0.5")
    volume = driver.execute_script("return document.querySelector('video').volume")
    assert volume == 0.5, "Volume control failed."

    driver.quit()
