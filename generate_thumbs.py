"""
Generate thumbnails for images under the media/ directory.
Thumbnails are saved as: <same-folder>/thumbs/<basename>_thumb.jpg
"""

from PIL import Image
from pathlib import Path

SIZE = (400, 300)  # default thumbnail size (WxH)
MEDIA_DIR = Path('media')
THUMBS_DIR_NAME = 'thumbs'

def make_thumb(src_path: Path, dst_path: Path, size=SIZE):
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with Image.open(src_path) as im:
            im.thumbnail(size, Image.LANCZOS)
            # convert to RGB to ensure jpg compatibility
            if im.mode in ('RGBA', 'P'):
                im = im.convert('RGB')
            im.save(dst_path, 'JPEG', quality=85)
            print('Thumb saved:', dst_path)
    except Exception as e:
        print('Failed to create thumb for', src_path, e)

def main():
    if not MEDIA_DIR.exists():
        print('Media directory not found. Create a "media" directory and put your photos inside.')
        return
    
    # 遍历media目录下所有文件，但跳过thumbs目录
    for img_path in MEDIA_DIR.rglob('*'):
        if img_path.is_file():
            # 跳过thumbs目录中的文件，避免缩略图的缩略图
            if THUMBS_DIR_NAME in img_path.parts:
                # print(f"Skipping thumbnail or file inside thumbs: {img_path}")
                continue
            
            if img_path.suffix.lower() in ('.jpg', '.jpeg', '.png', '.gif'):
                thumb_dir = img_path.parent / THUMBS_DIR_NAME
                thumb_name = img_path.stem + '_thumb.jpg'
                dst = thumb_dir / thumb_name
                
                if dst.exists():
                    # print(f"Thumbnail already exists, skipping: {dst}")
                    continue
                
                make_thumb(img_path, dst)

if __name__ == '__main__':
    main()
