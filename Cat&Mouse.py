mouse = 20
cat = 72
while mouse > 0:
    mouse = mouse - 2
    cat = cat - 7
    print(mouse,cat)
if cat > 0:
    print("не догонит потому,что количество оставшихся шагов для кошки ",cat,"а мышка забежала в нору",mouse)