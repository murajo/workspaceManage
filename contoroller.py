import xdotool as xdo
import tkinter
import mainGui as mgui


namearray = ["atom", "chromium","Aspire"]
root = tkinter.Tk()
root.title("workspaceManage")
root.geometry("400x300")
for ix,app_name in enumerate(namearray):
        root = mgui.createWidgets(root, ix, app_name)
root.mainloop()
