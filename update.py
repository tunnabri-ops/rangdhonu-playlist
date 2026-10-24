import requests

def update_and_combine():
    urls = [
        "https://raw.githubusercontent.com/public-iptv-org/BD/main/rangdhonu-playlist.m3u8",
        "https://raw.githubusercontent.com/public-iptv-org/BD/main/rangdhonu-playlist"
    ]
    
    combined_content = ""
    
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                combined_content += response.text + "\n\n"
            else:
                print(f"Failed to fetch {url}, status code: {response.status_code}")
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            
    # Sobsheše ekti file-e combine kore save korbe
    with open("combined-playlist.m3u8", "w", encoding="utf-8") as f:
        f.write(combined_content)
        
    print("Playlists combined and updated successfully!")

if __name__ == "__main__":
    update_and_combine()
