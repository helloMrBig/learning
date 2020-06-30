# 需求：实现注册与登录文件版(验证是否是已经注册)


# 提示用户选择注册与登录
num = input("请选择[1.注册 or 2.登录]: ")
#if语句判断用户操作
if num == "1":
    print("注册")
    # 提示用户输入用户名与密码
    name = input("请输入用户名: ")
    pwd = input("请输入密码: ")
    # 打开文件
    fp = open("users.txt", "r", encoding="utf-8")

    # 操作文件，遍历每行信息
    for data in fp.readlines():
        # 先去除空白,再拆分,返回一个包含用户名与密码的列表user
        user1 = data.strip().split("|")
        #判断登录信息是否正确
        if name == user1[0]:
            print("用户存在，注册失败.")
            break  # 如果登录成功,就break结束循环
    else:
        fp = open("users.txt", "a", encoding="utf-8")
        # 写入用户注册信息
        fp.write(f"{name}|{pwd}\n")
        # 给出提示
        print(f"{name} 注册成功")

    # 关闭文件
    fp.close()

#判断用户操作是登录
elif num == "2":
    print("登录")
    #输入登录信息
    name = input("用户名: ")
    pwd = input("密码: ")

    # 遍历文件users.txt,取出用户名与密码
    # 打开文件
    fp = open("users.txt", "r", encoding="utf-8")

    # 操作文件，遍历每行信息
    for data in fp.readlines():
        # 先去除空白,再拆分,返回一个包含用户名与密码的列表user
        user = data.strip().split("|")
        #判断登录信息是否正确
        if name == user[0] and pwd == user[1]:
            print("登录成功.")
            break  # 如果登录成功,就break结束循环
    else:
        print("登录失败")  # 注意: 遍历完了都没有登录成功(break)

    # 关闭文件
    fp.close()

else:
    exit("输入有误.")
