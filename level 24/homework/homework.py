#1)
list = ["apple" , "bannana" , "peach" , "watermelon" , "melon"]
print(list)
#2)
pc_peripherials = ["keyboard" , "mouse" , "headset" , "camera" , "microfone"]
most_used = "mouse"
index = pc_peripherials.index(most_used)
print(index)
#3)
monacemebi = ["integer" , "float" , "string" , "boolean" , "list"] * 2
print([i for i in monacemebi if i == "boolean"])
#4)
mates_list = ["integer" , "float" , "string" , "boolean" , "list" ]
print(mates_list[-3])