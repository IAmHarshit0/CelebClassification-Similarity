from icrawler.builtin import GoogleImageCrawler
import os

men = ['Shah Rukh Khan', 'Salman Khan', 'Amitabh Bachchan', 'Anil Kapoor', 'Ajay Devgn']
women = ['Madhuri Dixit', 'Juhi Chawla', 'Kajol', 'Shilpa Shetty Kundra', 'Sridevi']

# Extra keywords for better face-focused images
extra_keywords = [" face", " portrait"]

def download_images(keyword, folder, count=100):
    os.makedirs(folder, exist_ok=True)
    
    crawler = GoogleImageCrawler(storage={'root_dir': folder})
    total_downloaded = 0
    
    # Try multiple keyword variations to get more unique results
    for extra_kw in extra_keywords:
        if total_downloaded >= count:
            break
        
        query = keyword + extra_kw
        remaining = count - total_downloaded
        
        crawler.crawl(
            keyword=query,
            max_num=remaining,
            min_size=(200, 200),  # Avoid tiny images
            max_size=None,
            file_idx_offset='auto'
        )
        
        total_downloaded += remaining
        print(f"Downloaded ~{total_downloaded} images for {keyword}")

# Download images for men
for person in men:
    folder_name = person.replace(" ", "_")
    folder_path = f'dataset/men/{folder_name}'
    download_images(person, folder=folder_path, count=100)

# Download images for women
for person in women:
    folder_name = person.replace(" ", "_")
    folder_path = f'dataset/women/{folder_name}'
    download_images(person, folder=folder_path, count=100)
