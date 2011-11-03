VIDEO_PREFIX = "/video/engadget"

NAME = L('Title')

# make sure to replace artwork with what you want
# these filenames reference the example files in
# the Contents/Resources/ folder in the bundle
ART  = 'art-default.jpg'
ICON = 'icon-default.png'

URL = 'http://www.engadget.com/video/'
VIDDLER_URL = 'http://www.viddler.com/simple/%s'

####################################################################################################

def Start():
    Plugin.AddPrefixHandler(VIDEO_PREFIX, VideoMainMenu, NAME, ICON, ART)

    Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")
    Plugin.AddViewGroup("List", viewMode="List", mediaType="items")

    MediaContainer.title1 = NAME
    MediaContainer.viewGroup = "List"
    MediaContainer.art = R(ART)
    DirectoryItem.thumb = R(ICON)
    VideoItem.thumb = R(ICON)
    
    HTTP.CacheTime = CACHE_1HOUR


#
# Example main menu referenced in the Start() method
# for the 'Video' prefix handler
#

def VideoMainMenu():
    dir = MediaContainer(viewGroup="InfoList")

    for video_nav in HTML.ElementFromURL(URL).xpath('.//div[@class="video_content_nav"]/div/a'):
        #Log(video_nav.xpath('.//span/text()')[0])
        dir.Append(
            Function(
                DirectoryItem(
                    VideoLibrary,
                    video_nav.xpath('.//span/text()')[0]
                ), url="http://www.engadget.com/video-nav-grab-tags/featured", page=1))

    # ... and then return the container
    return dir

def VideoLibrary(sender, url, page):
    dir = MediaContainer(title2=sender.itemTitle)

    Log(url)

    #videos is empty why?
    #.//ul[@class="video_content_item_list"]/li
    videos = HTML.ElementFromURL(url).xpath('.//li')

    Log(len(videos))

    for video in videos:
        #Log("Hello World")
        video_title = video.xpath('.//div[@class="video_item_title"]/a/text()')[0]
        #Log(video_title)
        #video_thumb = video.xpath('.//div[@class="video_content_item_image"]/img')[0].get('src')
        #Log(video_thumb)
        #video_date = video.xpath('.//div[@class="video_item_date"]/text()')[0]
        #Log(video_date)
        video_id = video.xpath('.//div[@class="video_item_title"]/a')[0].get('rel')
        #Log(video_id)

        dir.Append(WebVideoItem(url=VIDDLER_URL%video_id, title=video_title))

    return dir

def GetVideosURL(url):
   eou = url.split("/")[-1]

   if eou in ('featured','unboxing','hands-on'):
       return "http://www.engadget.com/video_nav_grab_tags/%s" % eou
   else:
       return "http://www.engadget.com/video_nav_grab_no_tags/engadget"

