VIDEO_PREFIX = "/video/engadget"

NAME = L('Title')

# make sure to replace artwork with what you want
# these filenames reference the example files in
# the Contents/Resources/ folder in the bundle
ART  = 'art-default.jpg'
ICON = 'icon-default.png'

URL = 'http://www.engadget.com/video/'

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
                ) url=video_nav.get('href'), page=1))

    # ... and then return the container
    return dir

def VideoLibrary(sender, url, page):
    dir = MediaContainer(title2=sender.itemTitle)

    for video in HTML.ElementFromURL(url).xpath('.//ul[@class="video_content_item_list"]/li'):
        Log("Hello World")

    return dir

