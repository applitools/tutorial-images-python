import os
import io
import pytest
import requests
from PIL import Image

from applitools.images import Eyes, BatchInfo, logger

logger.set_logger(logger.StdoutLogger())

@pytest.fixture(name="eyes", scope="function")
def eyes_setup():
    """
    Basic Eyes setup. It'll abort test if wasn't closed properly.
    """
    eyes = Eyes()
    # Initialize the eyes SDK and set your private API key.
    eyes.api_key = os.environ["APPLITOOLS_API_KEY"]
    eyes.configure.batch = BatchInfo("Some general Test cases name")
    yield eyes
    # If the test was aborted before eyes.close was called, ends the test as aborted.
    eyes.abort()


def test_tutorial(eyes):
    # Start the session and set app name and test name.
    eyes.open("Test app", "First test")

    image = Image.open(io.BytesIO(requests.get("https://applitools.com/tutorials/applitools.jpg").content))
    # Visual checkpoint #1.
    eyes.check_image(image)

    # End the test.
    eyes.close(False)
