# fall-foliage-forecast

The goal of this project is to use historical images of a forest, and try to predict the peak fall foliage time based on model

### Notes
- SkyWatch is able to create interval pipelines of locations on their [console](https://console.earthcache.com/)
    - Using the [API](https://api-docs.earthcache.com/#tag/intervalResults/operation/intervalResultsList), we are able to retrieve interval results and get image URLs
<br/>

- <u>Development idea</u>

    - Use an S3 database to store images
    - Using images of "peak", pre and post fall activity images, create a model that determines what "stage" the fall foliage is at.
        - The key is to determine peak foliage, then calculate a range to determine the pre and post
    - Data collection portion
        - Collect images from very popular fall foliage spots from all over the world using SkyWatch, and record data from beginning to end of potential fall foliage dates, more data the better! Daily frequency if allows
        - Deploy some cron function to pull code everyday and save to S3 for storage
    - Model
        - Using color detection, [article here](https://pyimagesearch.com/2014/08/04/opencv-python-color-detection/)
        - Select fall colors range (red, orange, yellow) and determine the % of color in the photo, this will determine the "stage" of fall foliage
        - We will need to keep track of timestamps as well, perhaps a SQL db to keep track of URL and historical data
        - With timing, we can produce a model to give an estimate of when peak will be
            - historical data model for peak estimates

### TODO
- <s>Write openCV code to determine % of fall colors in an image and allow a range of fall colors to be determined</s>
- After data collection and using color percentage code, begin to create a ML model to give a time estimate on when peak fall foliage would be based on satellite photo


### Fall Foliage locations to map
- <s>Rangeley Lakes Region, Maine</s>
- <s>Letchworth State Park, New York</s>
- <s>Kancamagus Scenic Highway, New Hampshire</s>
- <s>Big South Fork National Recreation Area, Kentucky</s>
- <s>Lake Geneva Area, Wisconsin</s>
- <s>Shenandoah National Park, Virginia</s>
- <s>Great Smoky Mountain National Park, Tennessee</s>
- <s>Mount Cheaha, Alabama</s>
- <s>Fort Ransom State Park, North Dakota</s>
- <s>Estes Park, Colorado</s>
- <s>Ozark National Forest, Arkansas</s>
- <s>Olympic National Park, Washington</s>
- <s>Million Dollar Highway, Colorado</s>
- <s>Great Mountain Highway, Vermont</s>
- <s>Neuschwanstein Castle, Germany</s>
- <s>Denali National Park and Preserve, Alaska</s>
- <s>Central Park, New York</s>
- <s>Niagara Falls, New York</s>
- <s>Santa Fe, New Mexico</s>
- <s>Highlands, Scotland</s>
- <s>Quebec, Canada</s>
- <s>Lapland, Finland</s>
- <s>Lake Louise, Canada</s>
- <s>Asheville, North Carolina</s>
- <s>Lake Superior, Michigan</s>