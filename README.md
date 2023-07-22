# fall-foliage-forecast

The goal of this project is to use historical images of a forest, and try to predict the peak fall foliage time based on model

### Notes
- SkyWatch is able to create interval pipelines of locations on their [console](https://console.earthcache.com/)
    - Using the [API](https://api-docs.earthcache.com/#tag/intervalResults/operation/intervalResultsList), we are able to retrieve interval results and get image URLs
    - The interval can be daily, weekly, etc
    - Low-res is free!