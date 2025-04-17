def strip_youtube_url(url):
    base_url = "https://www.youtube.com/watch?v="
    if url.startswith(base_url):
        return url[len(base_url):]
    else:
        exit(1)

