import os
import shutil
import sys

def compare_folders(folder_a, folder_b, folder_c):
    """
    比较两个文件夹的子文件夹差异，并将A中有而B中缺少的子文件夹复制到C文件夹
    
    参数:
    folder_a (str): A文件夹的路径（包含子文件夹）
    folder_b (str): B文件夹的路径（包含子文件夹）
    folder_c (str): C文件夹的路径
    """
    
    # 确保C文件夹存在
    if not os.path.exists(folder_c):
        os.makedirs(folder_c)
        print(f"✅ 创建C文件夹: {folder_c}")
    
    # 获取A和B文件夹中的直接子文件夹名
    def get_subfolders(path):
        """获取路径下的直接子文件夹名（不包括文件）"""
        return {name for name in os.listdir(path) 
                if os.path.isdir(os.path.join(path, name))}
    
    subfolders_a = get_subfolders(folder_a)
    subfolders_b = get_subfolders(folder_b)
    
    # 找出A中有而B中没有的子文件夹
    missing_in_b = subfolders_a - subfolders_b
    # 找出B中有而A中没有的子文件夹
    missing_in_a = subfolders_b - subfolders_a
    
    # 复制缺少的子文件夹（A中有B中没有的）到C文件夹
    for folder in missing_in_b:
        src_path = os.path.join(folder_a, folder)
        dest_path = os.path.join(folder_c, folder)
        
        # 检查C中是否已有同名文件夹，如果有则先删除
        if os.path.exists(dest_path):
            shutil.rmtree(dest_path)
            print(f"⚠️ 已删除C中已有的同名文件夹: {dest_path}")
        
        # 复制子文件夹
        shutil.copytree(src_path, dest_path)
        print(f"✅ 已复制子文件夹: {folder} → {dest_path}")
    
    # 打印B中有而A中缺少的子文件夹（不复制，但提示）
    if missing_in_a:
        print(f"\n⚠️ B中有而A中缺少的子文件夹 ({len(missing_in_a)}个):")
        for folder in missing_in_a:
            print(f"   - {folder}")
    
    # 打印比较结果
    print(f"\n📊 比较完成 | A中有而B中缺少: {len(missing_in_b)} 个子文件夹")
    if missing_in_a:
        print(f"          B中有而A中缺少: {len(missing_in_a)} 个子文件夹")
    print(f"  A文件夹: {folder_a}")
    print(f"  B文件夹: {folder_b}")
    print(f"  C文件夹: {folder_c}")

if __name__ == "__main__":
    # 按照您提供的路径设置（使用原始字符串避免转义问题）
    folder_a = r"D:\steam\steamapps\workshop\content\431960"
    folder_b = r"D:\steam\steamapps\common\wallpaper_engine\projects\BackWP"
    folder_c = r"D:\steam\steamapps\common\wallpaper_engine\projects\TmpWP"
    
    print("🚀 开始比较子文件夹...")
    print(f"  A: {folder_a}")
    print(f"  B: {folder_b}")
    print(f"  C: {folder_c}\n")
    
    # 验证路径是否存在
    if not os.path.exists(folder_a):
        print(f"❌ 错误: A文件夹不存在 - {folder_a}")
        sys.exit(1)
    if not os.path.exists(folder_b):
        print(f"❌ 错误: B文件夹不存在 - {folder_b}")
        sys.exit(1)
    
    compare_folders(folder_a, folder_b, folder_c)
    
    print("\n💡 提示: Steam Workshop文件夹通常包含多个子文件夹（每个代表一个作品）")
    print("        仅复制了A中有而B中缺少的子文件夹到C文件夹")
    print("        B有而A中缺少的子文件夹已列出，但未复制")