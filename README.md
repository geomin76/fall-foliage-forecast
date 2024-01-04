# fall-foliage-forecast

The goal of this project is to use historical images of popular fall foliage spots and try to predict the peak fall foliage

### Running notes
- `app.py` gets the new data from SkyWatch pipelines, does color analysis and inserts it into the DynamoDB database
- `retrieve_images.py` gets the images from pipelines and saves them locally
- `new_pipeline_script.py` dumps the year's pipeline data to a json file, creates new pipelines for the next year, then deletes old pipelines
    - Run every year in January after the year's pipelines have run

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