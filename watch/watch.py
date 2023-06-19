import re
import sys

def main():
    html = sys.argv[1]
    print(parse(html))

def parse(s):
    pattern = r'<iframe.*?src="https?://(?:www\.)?youtube\.com/embed/(.*?)".*?>'
    match = re.search(pattern, s)
    if match:
        youtube_id = match.group(1)
        youtu_be_url = f"https://youtu.be/{youtube_id}"
        return youtu_be_url
    return None

if __name__ == "__name__":
    main()