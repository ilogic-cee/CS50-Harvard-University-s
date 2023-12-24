def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Use regex to find the YouTube URL in the src attribute
    match = re.search(r'<iframe[^>]*src="(?:https?://)?(?:www\.)?youtube\.com/embed/([^"]+)"', s)

    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    else:
        return None


if __name__ == "__main__":
    main()
