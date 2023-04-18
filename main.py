from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

youtube_trending_url='https://www.youtube.com/feed/trending'


def get_driver():
  chrome_options = Options()
  chrome_options.add_argument("-no-sandbox")
  chrome_options.add_argument("–-headless")
  chrome_options.add_argument("–-disable-dev-shm-usage")
  driver=webdriver.Chrome(options=chrome_options)
  return driver
  
def get_videos(driver):
  driver.get(youtube_trending_url)
  video_div_tag='ytd-video-renderer'
  time.sleep(5)
  videos=driver.find_elements(By.TAG_NAME,video_div_tag)
  return videos
  

if __name__=='__main__':
  print('creating driver')
  driver=get_driver()
  
  print('fetching the trending videos')
  video_no=get_videos(driver)

  print(f'no of videos are: {len(video_no)}')

#title,channel, thumbnail_url,url,uploaded,views,describtion



def parse_videos(video):
  title_tag=video.find_element(By.ID,'video-title')
  title=title_tag.text
  url=title_tag.get_attribute('href')
  Thumbnail_URL_tag=video.find_element(By.ID,'img')
  Thumbnail_Url=Thumbnail_URL_tag.get_attribute('src')
  channel_name=video.find_element(By.CLASS_NAME,'ytd-channel-name').text
  Describtion=video.find_element(By.ID,'description-text').text
  views_uploaded=video.find_element(By.CLASS_NAME,'ytd-video-meta-block').text

  return {'Title':title,
          'URL':url,
         'Thumbnail_Url':Thumbnail_Url,
         'Channel_Name':channel_name,
         'Describtion':Describtion,
         'views_uploaded':views_uploaded
         }

print('parsing the top 10 videos')
videos_data=[parse_videos(video) for video in video_no[:10]]

print(videos_data[3])

print('save the video data as csv')

videos_df=pd.DataFrame(videos_data)
print(videos_df)

videos_df.to_csv('trendingvideos.csv',index=None)
  

  







  


