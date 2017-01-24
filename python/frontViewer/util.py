#from httpseleniumpythonqa.blogspot.com201508generate-full-page-screenshot-in-chrome.html
#install pillow from pip if necessary.

#to avoid dialog box when firefox crash httpsleonax.netp7disable-application-error-dialog
#

#selenum python api httpselenium-python.readthedocs.ioapi.html

import os
import time

import PIL as pillow
from PIL import Image

def fullpage_screenshot(driver, file, executeAfterScroll = '', executeAfterLoad = ''):
    #IE8 browser in the screenshot will directly intercept the entire page, do not need to intercept several times and then merge the deal.
    print(Starting chrome full page screenshot workaround ...)
    #detect IE. IE11 will fail here.
    isIe = False
    try
        isIe = driver.execute_script(return window.ActiveXObject  true  false;)
        #print ([util] IE is... + str(isIe))
        if(isIe)
            driver.get_screenshot_as_file(file)
            return True
    except
        print (got error when find if IE...)
        
    try
        driver.execute_script(executeAfterLoad)
    except
        print (got error when run AfterLoad...)
        
    total_width = driver.execute_script(return document.body.offsetWidth)
    total_height = driver.execute_script(return document.body.parentNode.scrollHeight)
    viewport_width = driver.execute_script(return document.body.clientWidth)
    viewport_height = driver.execute_script(return window.innerHeight)
    if(isIe and (not viewport_height))
        #fix if Ie js...
        viewport_height = driver.execute_script(return document.documentElement.clientHeight)
        
    print(Total ({0}, {1}), Viewport ({2},{3}).format(total_width, total_height,viewport_width,viewport_height))
    rectangles = []

    i = 0
    while i  total_height
        ii = 0
        top_height = i + viewport_height

        if top_height  total_height
            top_height = total_height

        while ii  total_width
            top_width = ii + viewport_width

            if top_width  total_width
                top_width = total_width

            print(Appending rectangle ({0},{1},{2},{3}).format(ii, i, top_width, top_height))
            rectangles.append((ii, i, top_width,top_height))

            ii = ii + viewport_width

        i = i + viewport_height

    stitched_image = Image.new('RGB', (total_width, total_height))
    previous = None
    part = 0

    for rectangle in rectangles
        if not previous is None
            driver.execute_script(window.scrollTo({0}, {1}).format(rectangle[0], rectangle[1]))
            print(Scrolled To ({0},{1}).format(rectangle[0], rectangle[1]))
            time.sleep(0.2)

        file_name = part_{0}.png.format(part)
        print(Capturing {0} ....format(file_name))
        
        if(len (executeAfterScroll)  0)
            print ([util]run script  + str(executeAfterScroll))
            try
                driver.execute_script(str(executeAfterScroll))
            except
                print (run script got an error...)

        driver.get_screenshot_as_file(file_name)
        screenshot = Image.open(file_name)

        if rectangle[1] + viewport_height  total_height
            offset = (rectangle[0], total_height - viewport_height)
        else
            offset = (rectangle[0], rectangle[1])

        print(Adding to stitched image with offset ({0}, {1}).format(offset[0],offset[1]))
        stitched_image.paste(screenshot, offset)

        del screenshot
        os.remove(file_name)
        part = part + 1
        previous = rectangle

    stitched_image.save(file)
    print(Finishing chrome full page screenshot workaround...)
    return True