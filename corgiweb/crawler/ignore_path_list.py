ignore_list = """whatsapp:
    whatsapp.
    facebook.
    twitter.
    google.
    .jpg
    .jpeg
    .png
    .mp4
    .gif
    '
    share=
    #print
    telegram.
    attachment_id=
    #respond
    @@search?
    search_rss?
    archive_query
    /galeria/
    e=rostros&id=
    /tag/
    /tags/
    /me/
    /app/
    /cdn-cgi/
    /fotos/
    /busqueda?
    searchtag.html?tag=
    mailto:
    'desk=1'
    sharer.php?"""


def get_ignore_list():
    return [line.strip() for line in ignore_list.splitlines()]