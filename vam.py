import os
import sys
import easygui

base_path = getattr(sys, '_MEIPASS', os.path.dirname(
    os.path.abspath(__file__)))
ffmpeg_path = os.path.join(base_path, 'ffmpeg.exe')

video_path = easygui.fileopenbox('选择视频文件')
if not video_path:
    sys.exit()
print(f'视频文件：{video_path}')
last_path = os.path.split(video_path)[0]+'/'

audio_path = easygui.fileopenbox('选择音频文件', default=last_path)
if not audio_path:
    sys.exit()
print(f'音频文件：{audio_path}')
last_path = os.path.split(audio_path)[0]+'/'

output_path = easygui.filesavebox(
    '选择输出文件', default=last_path+'output.mp4', filetypes=['*.mp4'])
if not output_path:
    sys.exit()
print(f'输出文件：{output_path}')

command = rf'{ffmpeg_path} -i "{video_path}" -i "{
    audio_path}" -map 0:v -map 1:a -c:v copy -c:a flac -b:a 4000k "{output_path}"'

print(f'命令：{command}')
stat = os.system(command)
print(f'返回值：{stat}')

if stat == 0 and os.path.isfile(output_path):
    easygui.msgbox('命令执行成功！')
    os.system(rf'explorer /select,"{output_path}"')
else:
    input('命令执行失败，请自行查看错误信息后按回车退出程序。')
