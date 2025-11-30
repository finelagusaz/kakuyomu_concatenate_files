# File Concatenation Tool

カクヨムのバックアップ機能で出力されるテキストファイルを連結させるPythonスクリプトです。

## 機能

- `about.txt` をメタデータ区切りで囲んで先頭に配置
- `episode_*.txt` パターンのファイルを番号順に連結
- 各エピソードのタイトル（ファイルの2行目）を区切りに使用
- ファイル間に改行2行を自動挿入
- 存在しないファイルはスキップして処理を継続

## 使い方

### 実行方法

```bash
python concatenate_files.py
```

### ファイル構成

スクリプトと同じディレクトリに以下のファイルを配置してください：

```
.
├── concatenate_files.py
├── about.txt
├── episode_0001.txt
├── episode_0002.txt
├── episode_0003.txt
└── ...
```

### エピソードファイルの形式

各 `episode_*.txt` ファイルは以下の形式を推奨します：

```
【タイトル】
第1話 救出・前編【Depth 1】

[本文...]
```

**2行目**がエピソードのタイトルとして使用されます。

### 出力

実行すると `union.txt` が生成されます：

```
==== BEGIN META ====
[about.txt の内容]
==== END META ====

==== BEGIN EPISODE 第1話 救出・前編【Depth 1】 ====
【タイトル】
第1話 救出・前編【Depth 1】

[episode_0001.txt の本文...]
==== END EPISODE 第1話 救出・前編【Depth 1】 ====

==== BEGIN EPISODE 第2話 救出・断章【Depth 2】 ====
【タイトル】
第2話 救出・断章【Depth 2】

[episode_0002.txt の本文...]
==== END EPISODE 第2話 救出・断章【Depth 2】 ====

...
```

## 仕様

- **入力ファイル**: `about.txt` および `episode_*.txt`
- **出力ファイル**: `union.txt`
- **メタデータ区切り**: `==== BEGIN META ====` / `==== END META ====`
- **エピソード区切り**: `==== BEGIN EPISODE [タイトル] ====` / `==== END EPISODE [タイトル] ====`
- **タイトル取得**: 各エピソードファイルの2行目を使用
- **ファイル間の区切り**: 改行2行
- **ソート順**: ファイル名の番号部分で昇順ソート
- **エラー処理**: 存在しないファイルは警告を表示してスキップ
- **文字エンコーディング**: UTF-8

## 実行例

```bash
$ python concatenate_files.py
Processing: about.txt
Processing: episode_0001.txt
Processing: episode_0002.txt
Processing: episode_0003.txt

Completed! Output written to: union.txt
Total files processed: 4
```

## 必要な環境

- Python 3.6 以上
- 標準ライブラリのみ使用（追加パッケージ不要）

## ライセンス

自由に使用・改変可能です。
