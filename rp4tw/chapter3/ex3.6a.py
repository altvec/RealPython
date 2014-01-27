import gdata.youtube
import gdata.youtube.service

youtube_service = gdata.youtube.service.YouTubeService()

# Prompt the user to enter the YouTube user ID
playlist = raw_input("Please enter the user ID: ")

# Setup the actual API call
url = "http://gdata.youtube.com/feeds/api/users/"
playlist_url = url + playlist + "/playlists"

# Retrieve Youtube playlist
video_feed = youtube_service.GetYouTubePlaylistVideoFeed(playlist_url)

print "\nPlaylists for " + str.format(playlist) + ":\n"

# Display each playlist to the screen
for p in video_feed.entry:
    print p.title.text

print video_feed
