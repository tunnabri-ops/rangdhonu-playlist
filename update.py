import requests

def update_playlist():
    # সরাসরি আপনার দেওয়া ফাইলের Raw লিংক
    url = "https://raw.githubusercontent.com/public-iptv-org/BD/main/rangdhonu-playlist.m3u8"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open("rangdhonu-playlist.m3u8", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("Rangdhonu playlist updated successfully!")
        else:
            print(f"Failed to fetch. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_playlist()
