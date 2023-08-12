from color_analysis import color_analysis

# # cron job to pull data from SkyWatch
# once a week, pull data from earth cache from all pipelines

# store image in s3 and get URL
url = "images/fall.jpg"

# run color_analysis on image
percentage = color_analysis(url)

# store data in dynamodb