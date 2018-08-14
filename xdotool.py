import subprocess

# 指定したアプリケーションのwindowIDを配列で返す
# return array(str)
def get_window_id(name):
    try:
        res = subprocess.check_output(["xdotool", "search", "--name", name])
        res = str(res).strip("b'").split("\\n")[:-1]
    except:
        res = ["-1"]
    return res

# 指定したwindowIDのワークスペースを変更
# return int
def set_window_workspace(window_id, work_num):
    try:
        res = subprocess.check_call(["xdotool", "set_desktop_for_window", window_id, work_num])
    except:
        res = -1
    return res

# ワークスペースの数を返す
# return str
def get_workspace_count():
    try:
        res = subprocess.check_output(["xdotool", "get_num_desktops"])
        res = str(res).strip("b'\\n")
    except:
        res = "-1"
    return res

# 指定したwindowIDのワークスペースの場所を表示
# return int
def get_workspace_num(window_id):
    try:
        res = subprocess.check_output(["xdotool", "get_desktop_for_window", window_id])
        res = int(str(res).strip("b'\\n"))
    except:
        res = -1
    return res
