import requests

def update_playlist():
    # যে সোর্স থেকে ফাইল আনবেন তার সঠিক Raw লিংক এখানে দিতে হবে
    url = "https://raw.githubusercontent.com/public-iptv-org/BD/main/index.m3u"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open("playlist.m3u", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("Playlist successfully updated!")
        else:
            print(f"Failed to fetch, status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_playlist()
