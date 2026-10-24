import os

def update_playlist():
    # আপনার আইপিটিভি লিংক বা ফাইল প্রসেস করার লজিক এখানে লিখবেন
    print("Checking and updating playlist files...")
    
    # উদাহরণস্বরূপ একটি ফাইল আপডেট করার কোড
    file_path = "bd.m3u" # আপনার মূল ফাইলের নাম এখানে দিন
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # এখানে লিংক ভ্যালিডেশন বা আপডেট লজিক যোগ করতে পারেন
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Playlist processed successfully.")
    else:
        print(f"{file_path} not found!")

if __name__ == "__main__":
    update_playlist()
