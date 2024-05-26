def read_file(archive):
    opened_archive = open(archive, "r")
    content_archive = opened_archive.read()
    opened_archive.close()
    return content_archive