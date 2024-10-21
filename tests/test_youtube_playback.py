import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_youtube_playback():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Replace with any public YouTube video link

    # Wait for the video to load
    time.sleep(5)

    # Play the video
    play_button = driver.find_element(By.CSS_SELECTOR, 'button.ytp-play-button')
    play_button.click()

    # Wait for a few seconds to ensure video is playing
    time.sleep(5)

    # Check if the video is playing by verifying that the current time is advancing
    current_time = driver.execute_script("return document.querySelector('video').currentTime")
    time.sleep(2)
    new_time = driver.execute_script("return document.querySelector('video').currentTime")

    assert new_time > current_time, "Video is not playing."

    driver.quit()
