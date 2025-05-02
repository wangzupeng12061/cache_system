# common/dataset_loader.py

import csv
import os

def load_unsplash_photos(unsplash_dir):
    """
    加载 Unsplash 数据集中 photos.tsv 文件，并返回一个列表或字典。
    """
    photos_file = os.path.join(unsplash_dir, 'photos.tsv')
    photos = []
    with open(photos_file, encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            photos.append(row)
    return photos

def load_tencent_io_trace(trace_file):
    """
    加载腾讯 I/O trace 文件，解析 CSV/TSV 格式的数据。
    假设 trace_file 是解压后的 CSV 文件。
    """
    traces = []
    with open(trace_file, encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            # 假设字段依次为：Timestamp, Offset, Size, IOType, VolumeID
            trace = {
                "timestamp": row[0],
                "offset": row[1],
                "size": row[2],
                "io_type": row[3],
                "volume_id": row[4]
            }
            traces.append(trace)
    return traces

# 你可以写一些简单的测试代码：
if __name__ == "__main__":
    unsplash_data = load_unsplash_photos(os.path.join("datasets", "unsplash"))
    print(f"Loaded {len(unsplash_data)} unsplash photos")
    
    # 假设腾讯 trace 数据已解压为 "2018-10-01-01.csv"
    tencent_data = load_tencent_io_trace(os.path.join("datasets", "tencent_io", "2018-10-01-01.csv"))
    print(f"Loaded {len(tencent_data)} I/O trace records")
