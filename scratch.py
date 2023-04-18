#requests lib does not execute javascript,so data load dynamically is not getting by requests
import requests
from bs4 import BeautifulSoup

youtube_trending_url='https://www.youtube.com/feed/trending'

response=requests.get(youtube_trending_url)
print('status_code:',response.status_code)
#print('output',response.text[:1000])

with open('trending.html','w') as f:
  f.write(response.text)

doc=BeautifulSoup(response.text,'html.parser')

print('page_title:',doc.title.text)

#Find all the divs which contain the whole video data
if __name__=='__main__':
  print('creating driver')
  driver=get_driver()
  
  print('fetching the trending videos')
  video_no=get_videos(driver)

  print(f'no of videos are: {len(video_no)}')

print('parsing the first video')
video=video_no[0]

video_divs=doc.find_all('div',class_='style-scope ytd-video-renderer')
print(f'found {len(video_divs)} videos')


title_tag=video.find_element(By.ID,'video-title')
title=title_tag.text
print('Title:', title)

url=title_tag.get_attribute('href')
print('URL:', url)

Thumbnail_URL_tag=video.find_element(By.ID,'img')
Thumbnail_Url=Thumbnail_URL_tag.get_attribute('src')
print('Thumbnail_Url:',Thumbnail_Url)


channel_name=video.find_element(By.CLASS_NAME,'ytd-channel-name').text
print("channel_name:",channel_name)

Describtion=video.find_element(By.ID,'description-text').text
print('Describtion:',Describtion)

views_uploaded=video.find_element(By.CLASS_NAME,'ytd-video-meta-block').text
print(views_uploaded)