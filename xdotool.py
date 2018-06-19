import subprocess
import os
import sys

# 指定したアプリケーションのwindowIDを配列で返す
# return array(str)
def get_window_id(name):
    res = subprocess.check_output(["xdotool", "search", "--name", name])
    split_num_array = str(res).strip("b'").split("\\n")[:-1]
    return split_num_array

# 指定したwindowIDのワークスペースを変更
# return int
def set_window_workspace(window_id, work_num):
    res = subprocess.check_call(["xdotool", "set_desktop_for_window", window_id, work_num])
    return res

# ワークスペースの数を返す
# return str
def get_workspace_count():
    count = subprocess.check_output(["xdotool", "get_num_desktops"])
    count = str(count).strip("b'\\n")
    return count
