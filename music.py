from mutagen.id3 import ID3, TIT2 ,TPE1,TALB
import os
import glob

# 指定你想要遍历的文件夹路径
folder_path = 'L:\music\MUSIC'

# 使用glob来获取所有MP3文件
mp3_files = glob.glob(os.path.join(folder_path, '*.mp3'))

# 遍历所有MP3文件
for mp3_file in mp3_files:
    # print(mp3_file)
    filename =os.path.basename(mp3_file).replace('.mp3','')
    names= filename.split('-')
  
    
    # 打开文件
    audio = ID3(mp3_file)

    # 读取歌曲名
    title = audio.get('TIT2')
    if title:
        cur_title =title.text[0]
        # print("Current title:", cur_title)


    # 读取当前作者名
    author = audio.get('TPE1')
    if author:
        cur_auth =author.text[0]
        # print("Current author:", cur_auth)

    # 读取专辑名称
    album = audio.get('TALB')
    if album:
        cur_album = album.text[0]
        print("Current album:", cur_album)

    if(len(names)>1):
        title_name = names[1].strip()
        auth =  names[0].strip()
    else:
        title_name= names[0].strip()
        print(title_name)
        auth =cur_auth
        
    # 修改歌曲名
    audio["TIT2"] = TIT2(encoding=3, text=title_name)
    # 修改作者名
    audio["TPE1"] = TPE1(encoding=3, text=auth)
    # 修改作者名
    audio["TALB"] = TALB(encoding=3, text='')
    # 保存修改
    audio.save()
    
    
    if("（"in title_name or '('in title_name):
        name =filename.split('(')[0]
        name =filename.split('（')[0]
        name =filename.split('(')[0]

        print(name)
        new_file_name =name+".mp3"
        new_file_path = os.path.join(os.path.dirname(mp3_file), new_file_name)
        # print(new_file_path)
        try:
            os.rename(mp3_file, new_file_path)
            print(f'文件已成功重命名为: {new_file_name}')
        except OSError as e:
            print(f'重命名文件时出错: {e}')

