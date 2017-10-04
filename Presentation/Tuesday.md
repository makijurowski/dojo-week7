## Tuesday In-Class Activity
*Present to the class information on one standard library module and one non-standard library module.*

#### Standard Library:
- os
- re
- unittest
- math
- sys
- datetime
- itertools
- functools
- shutil
- logging
- urllib/2
- timeit

#### Non-Standard Library:
- requests
- scrapy/beautifulsoup
- IPython
- nose/pytest/mock

#### Information to Include:
- What is it, why is it useful, etc.
- Demo on how to use it
- "Mock assignment" (how could we hook this up to an assignment that's been completed)
- Github gist that summarizes the above information


## Standard Library: datetime
- Adds support for manipulating dates and times in many ways
- Two kinds of date/time objects: *naive* and *aware*
    - *Naive* objects do not contain enough info to be located 'unambiguously' relative to other datetime objects
    - *Aware* objects represent a specific moment in time, including time zone and DST info & can be located 'unambiguously'
- **Types:**
    - datetime.date: Idealized *naive* date 
        - Attributes: year, month, day
    - datetime.time: Idealized time independent of date (no leap year consideration)
        - Attributes: hour, minute, second, microsecond, tzinfo
    - datetime.datetime: Combo of date and time
        - Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo
    - datetime.timedelta: Expresses difference between two datetime instances
    - datetime.tzinfo: Timezone info
- **Usage:** 
    - from **datetime** import timedelta
    - Can use strftime(format) method to create a string of the time following a specified format <https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior>

## Non-Standard Library: PIL / Pillow (Python Imaging Library) 
- Adds image processing capabilities to Python. Original PIL latest version released in 2009. No longer being developed, successor project is named "Pillow." 
    - **CANNOT** use both, must install either PIL or Pillow.

- **Installation:** pip install Pillow
- **Usage:**
    - To load an image & print attributes:
        - from _\_\_future_\_\_ import print_function<br>
        from PIL import Image<br>
        im = Image.open("lena.ppm")<br>
        print(im.format, im.size, im.mode)
            - OUTPUT >>> PPM (512, 512) RGB

- **Select External Libraries:** 
    - ***libjpeg*** for JPEG functionality
    - ***zlib*** for compressed PNGs
    - ***libtiff*** for compressed TIFF
    - ***littlecms*** for color management
    - ***openjpeg*** for JPEG 2000 funtionality

- **Features:**
    - **Image archiving and batch processing:** thumbnail creation, file format conversion, print formats, etc.
    - **Image display:** save image to disk, external display support
    - **Image processing:** filtering, color-space conversions, image resizing, rotation, statistical analysis