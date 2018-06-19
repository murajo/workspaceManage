import subprocess
import os
import sys

# 指定したアプリケーションのwindowIDを配列で返す
def get_window_id(name):
    res = subprocess.check_output(["xdotool", "search", "--name", name])
    split_num_array = str(res).strip("b'").split("\\n")[:-1]
    return split_num_array

# 指定したwindowIDのワークスペースを変更
def set_window_workspace(window_id, work_num):
    res = subprocess.check_call(["xdotool", "set_desktop_for_window", window_id, work_num])
    return res
