import glob
import os 
from icrawler.builtin import GoogleImageCrawler

extra_keywords = [" face", " portrait"]

def count_images(folder):
    return len(glob.glob(os.path.join(folder, "*.jpg"))) + \
           len(glob.glob(os.path.join(folder, "*.png")))

def download_images(keyword, folder, count=100):
    os.makedirs(folder, exist_ok=True)
    
    crawler = GoogleImageCrawler(storage={'root_dir': folder})
    
    for extra_kw in extra_keywords:
        query = keyword + extra_kw
        crawler.crawl(
            keyword=query,
            max_num=count,
            min_size=(200, 200),
            file_idx_offset='auto'
        )
        
        actual = count_images(folder)
        print(f"Currently {actual}/{count} images downloaded for {keyword}")
        
        if actual >= count:
            break

# Edit This:
person = 'Kajol'
folder_name = person
folder_path = f'dataset/women/{folder_name}'
download_images(keyword=person, folder=folder_path, count=100)
