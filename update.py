import requests

def update_playlist():
    # public-iptv-org/BD এর রেন্ডম বা নির্দিষ্ট ফাইলটির Raw ইউআরএল এখানে দিন
    # উদাহরণস্বরূপ মূল প্লেলিস্ট ফাইল:
    url = "https://raw.githubusercontent.com/public-iptv-org/BD/main/bd.m3u"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open("playlist.m3u", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("Playlist successfully updated from public-iptv-org/BD!")
        else:
            print(f"Failed to fetch. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_playlist()
