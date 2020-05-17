from youtube_transcript_api import YouTubeTranscriptApi
from os import getenv
from commons import get_logger

def get_transcript(videoId, language):
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(videoId)
        transcript = transcript_list.find_manually_created_transcript([language])
        return transcript.fetch()
    except:
        return None

def get_video_from_playlist(playlistId):
    developer_key = getenv("DEVELOPER_KEY")
    log_level = getenv("LOG_LEVEL", "INFO")
    logger = get_logger("pyutils.youtube.get_video_from_playlist", log_level)
    youtube = build("youtube", "v3", developerKey=developer_key)
    playlistItems = []
    pageToken = None
    while True:
        response = youtube.playlistItems().list(part = "snippet", playlistId = playlistId, pageToken = pageToken, maxResults = 100).execute()
        playlistItems += response["items"]
        logger.info("Fetch {} of {} results".format(len(playlistItems), response["pageInfo"]["totalResults"]))
        pageToken = response.get("nextPageToken", None)
        if pageToken == None:
            break
    return playlistItems
