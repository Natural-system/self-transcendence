import os
import re
import hashlib

POSTS_DIR = '_posts'

def get_short_hash(text):
    # 提取 MD5 的前 8 位作为短 Hash
    return hashlib.md5(text.encode('utf-8')).hexdigest()[:8]

def process_posts():
    if not os.path.exists(POSTS_DIR):
        return

    for root, _, files in os.walk(POSTS_DIR):
        for file in files:
            if file.endswith('.md') or file.endswith('.markdown'):
                file_path = os.path.join(root, file)
                
                # 基于文件相对路径计算 Hash，保证唯一性且同一文章 Hash 永久固定
                rel_path = os.path.relpath(file_path, POSTS_DIR)
                short_id = get_short_hash(rel_path)
                target_permalink = f"/p/{short_id}/"

                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 如果 Front Matter 已存在，插入 permalink
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        yaml_header = parts[1]
                        # 避免重复插入
                        if 'permalink:' not in yaml_header:
                            new_yaml = yaml_header.rstrip() + f"\npermalink: {target_permalink}\n"
                            new_content = f"---{new_yaml}---" + parts[2]
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                else:
                    # 如果文章没有 Front Matter，自动补充
                    new_content = f"---\npermalink: {target_permalink}\n---\n" + content
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

if __name__ == '__main__':
    process_posts()