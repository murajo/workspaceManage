import xdotool as xdo

id_array = xdo.get_window_id("atom")
print(id_array)
for id in id_array:
    print(xdo.set_window_workspace(id, "2"))
