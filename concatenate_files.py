import os
import glob
import re

def concatenate_files():
    """about.txt と episode_*.txt を連結して union.txt に出力する"""

    output_file = "union.txt"
    about_file = "about.txt"

    # 出力ファイルを開く
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # 1. about.txt を先頭に追加（メタデータ区切りで囲む）
        if os.path.exists(about_file):
            print(f"Processing: {about_file}")
            outfile.write('==== BEGIN META ====\n')
            with open(about_file, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
            outfile.write('\n==== END META ====\n\n')  # 改行2行
        else:
            print(f"Warning: {about_file} not found, skipping...")

        # 2. episode_*.txt ファイルを取得してソート
        episode_files = glob.glob("episode_*.txt")

        # ファイル名から番号を抽出してソート
        def extract_number(filename):
            match = re.search(r'episode_(\d+)\.txt', filename)
            return int(match.group(1)) if match else 0

        episode_files.sort(key=extract_number)

        # 3. 各 episode ファイルを連結
        for i, episode_file in enumerate(episode_files):
            if os.path.exists(episode_file):
                print(f"Processing: {episode_file}")

                # ファイルを読み込んでタイトル（2行目）を取得
                with open(episode_file, 'r', encoding='utf-8') as infile:
                    lines = infile.readlines()

                # タイトルを取得（2行目、存在しない場合はファイル名を使用）
                title = lines[1].strip() if len(lines) >= 2 else episode_file

                # エピソードの開始区切りを書き込み
                outfile.write(f'==== BEGIN EPISODE {title} ====\n')

                # ファイルの内容を書き込み
                outfile.write(''.join(lines))

                # エピソードの終了区切りを書き込み
                outfile.write(f'\n==== END EPISODE {title} ====')

                # 最後のファイル以外は改行2行を追加
                if i < len(episode_files) - 1:
                    outfile.write('\n\n')
            else:
                print(f"Warning: {episode_file} not found, skipping...")

    print(f"\nCompleted! Output written to: {output_file}")
    print(f"Total files processed: {len(episode_files) + (1 if os.path.exists(about_file) else 0)}")

if __name__ == "__main__":
    concatenate_files()
