import io
import pytest
import requests

from applitools.images import Eyes, BatchInfo, logger
from PIL import Image

logger.set_logger(logger.StdoutLogger())

@pytest.fixture(name="eyes", scope="function")
def eyes_setup():
    """
    Basic Eyes setup. It'll abort test if wasn't closed properly.
    """
    eyes = Eyes()
    eyes.configure.batch = BatchInfo("Demo Batch - Images - Python")
    yield eyes
    # If the test was aborted before eyes.close was called, ends the test as aborted.
    eyes.abort()


def test_tutorial(eyes):
    # Start the session and set app name and test name.
    eyes.open("Demo App - Images Python", "Smoke Test - Images Python")

    image = Image.open(io.BytesIO(requests.get("https://i.ibb.co/bJgzfb3/applitools.png").content))

    # Visual checkpoint #1.
    eyes.check_image(image)

    # End the test.
    eyes.close(False)
