import requests
import re
response=requests.get('https://movie.douban.com/cinema/nowplaying/beijing/')
#print(response.status_code)
#print(response.content)
#print(response.text)
urls=re.findall(r'正在上映.*即将上映',response.text,re.S)
#print(urls)
titles=re.findall(r'data-title="(.*?)"', urls[0], re.S)
scores=re.findall(r'data-score="(.*?)"', urls[0], re.S)
print("北京正在上映的影片及其评分：")
i=0
for title in titles:
    print(title+":"+scores[i])
    i+=1;
