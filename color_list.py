color_list1=input("enter first color list seperated by comma:")
color_list1=color_list1.split(",")
color_list2=input("enter second color list seperated by comma:")
color_list2=color_list2.split(",")

diff_colors=[c for c in color_list1 if c not in color_list2]
print("Colors in list1 not in list2",diff_colors)