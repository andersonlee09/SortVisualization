# 以下为python排序代码
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.messagebox
import random

random.seed(1)  # 随机种子

# 设置数据
data = []

# 设置颜色
colors = []
# 颜色参数
# #22BB9C = GREEN  #D0505D = RED  #FFDA5C = YELLOW  #5191E1 = BLUE

# 设置速度
speed = 0.02


def draw(data):
    plt.clf()  # 清屏
    plt.xticks([])  # x,y轴消失
    plt.yticks([])
    plt.bar(range(len(data)), data, width=0.85, color=colors)  # 画画
    plt.pause(speed / 300)  # 展示时间


def before_color(j, k):  # 两个数交换前两个柱子颜色变化
    colors[j] = '#D0505D'
    colors[k] = '#D0505D'


def after_color(j, k):  # 两个数交换后两个柱子颜色变化
    colors[j] = '#22BB9C'
    colors[k] = '#22BB9C'


def change_color():  # 结束后全部变为黄色
    for i in range(len(colors)):
        colors[i] = '#FFDA5C'


def end_of_sort(data):  # 排序结束
    plt.clf()  # 清屏
    change_color()
    plt.xticks([])
    plt.yticks([])
    plt.bar(range(len(data)), data, width=0.85, color=colors)
    plt.show()


def bubble_sort(data):  # 冒泡排序
    plt.bar(range(len(data)), data, width=0.85, color=colors)
    for i in range(len(data) - 1):
        flag = 0
        for j in range(len(data) - i - 1):  # 下标经过优化
            colors[j] = '#5191E1'  # 每扫描一次都变一次颜色
            draw(data)
            colors[j] = '#22BB9C'
            if data[j] > data[j + 1]:
                before_color(j, j + 1)
                draw(data)
                data[j], data[j + 1] = data[j + 1], data[j]
                after_color(j, j + 1)
                flag = 1
        if flag == 0:
            break
    end_of_sort(data)  # 排序结束


def selection_sort(data):
    for i in range(len(data) - 1):
        min_num = i
        for j in range(i + 1, len(data)):
            colors[j] = '#5191E1'  # 每扫描一次都变一次颜色
            draw(data)
            colors[j] = '#22BB9C'  # #22BB9C = GREEN  #D0505D = RED  #FFDA5C = YELLOW  #5191E1 = BLUE
            if data[j] < data[min_num]:
                min_num = j  # 每次选择一个最小数字
        before_color(i, min_num)  # 换颜色
        draw(data)
        data[i], data[min_num] = data[min_num], data[i]  # 交换数字
        after_color(i, min_num)
    end_of_sort(data)


def insert_sort(data):
    for i in range(1, len(data)):
        tmp = data[i]  # 将摸到的牌储存到 tmp
        j = i - 1  # 将 j 看做手里的牌的下标
        draw(data)
        while j >= 0 and data[j] > tmp:  # 如果手里的牌大于摸到的牌
            colors[j] = '#5191E1'  # 每扫描一次都变一次颜色
            draw(data)
            colors[j] = '#22BB9C'
            colors[j + 1] = '#D0505D'  # 画之前换颜色
            draw(data)
            data[j + 1] = data[j]  # 将手里的牌往右移一个位置（将手里的牌赋值给下一个位置）
            colors[j + 1] = '#22BB9C'  # 画之后换颜色
            j -= 1  # 将手里的牌的下标减 1，再次准备与摸到的牌进行比较
        colors[j + 1] = '#D0505D'  # 画之前换颜色
        data[j + 1] = tmp  # 将摸到的牌插入到 j+1 位置
        colors[j + 1] = '#22BB9C'  # 画之后换颜色
    end_of_sort(data)


def shell_gap(data, gap):  # 将 gap 看做隔 gap 个距离摸一张牌，而不是依次按照顺序摸牌
    for i in range(gap, len(data)):  # 将 i 看做摸到的牌的下标
        tmp = data[i]  # 将摸到的牌储存到 tmp
        j = i - gap  # 将 j 看做手里的牌的下标
        while j >= 0 and data[j] > tmp:  # 如果手里的牌大于摸到的牌
            colors[j] = '#5191E1'  # 每扫描一次都变一次颜色
            draw(data)
            colors[j] = '#22BB9C'  # 扫描后换颜色
            before_color(j + gap, j)
            draw(data)
            data[j + gap] = data[j]  # 将手里的牌往右移一个位置（将手里的牌赋值给下一个位置）
            after_color(j + gap, j)
            draw(data)
            j -= gap  # 将手里的牌的下标减 gap，再次准备与摸到的牌进行比较
        before_color(j + gap, i)
        draw(data)
        data[j + gap] = tmp  # 将摸到的牌插入到 j+gap 位置
        after_color(j + gap, i)
        draw(data)


def shell_sort(data):  # 快速排序
    d = len(data) // 2  # 第一次分组
    while d >= 1:
        shell_gap(data, d)  # 调用插入排序
        d //= 2  # 整除 2 后再次分组
    end_of_sort(data)


# 堆排序
def creat_head(data, n, k):
    i = k  # i是要建堆的二叉树根节点下标
    j = 2 * i + 1  # j是i左孩子下标
    temp = data[i]
    while j < n:
        if j < n - 1 and data[j] < data[j + 1]:  # 选出左右孩子较大者
            j += 1
        if temp > data[j]:  # 如果父亲大于孩子
            break
        else:
            before_color(i, j)
            draw(data)
            data[i] = data[j]  # 否则上移孩子
            after_color(i, j)
            draw(data)
            i = j
            j = 2 * i + 1
    colors[i] = "#D0505D"
    draw(data)
    data[i] = temp  # 把最初data[i]给最后的a[j]
    colors[i] = "#22BB9C"
    draw(data)


def init_creat_head(data, n):  # 初始化最大堆
    i = (n - 2) / 2
    while i >= 0:
        creat_head(data, n, int(i))  # 可能会变成浮点型
        i -= 1


def heap_sort(data):  # 堆排序
    n = len(data)
    init_creat_head(data, n)  # 初始化最大堆
    i = n - 1  #
    while i > 0:
        before_color(0, i)
        draw(data)
        data[0], data[i] = data[i], data[0]  # 堆顶元素和最大堆最后一个元素交换
        after_color(0, i)
        draw(data)
        creat_head(data, i, 0)  # 调整根节点
        i -= 1  # 最大堆个数每次递减1
    end_of_sort(data)


def quick_sort(data, left, right):  # 快速排序
    if left > right:
        return

    temp = data[left]  # temp为基准数
    i = left
    j = right
    while i != j:
        while data[j] >= temp and i < j:  # 先从右向左找
            j -= 1
            colors[j] = "#5191E1"
            draw(data)
            colors[j] = "#22BB9C"
        while data[i] <= temp and i < j:  # 后从左向右找
            i += 1
            colors[i] = "#5191E1"
            draw(data)
            colors[i] = "#22BB9C"
        if i < j:
            before_color(i, j)
            draw(data)
            data[i], data[j] = data[j], data[i]  # 交换
            after_color(i, j)
            draw(data)
    before_color(left, i)
    draw(data)
    data[left] = data[i]  # 最终将基准数归位
    after_color(left, i)
    draw(data)
    colors[i] = "#D0505D"
    draw(data)
    data[i] = temp
    colors[i] = "#22BB9C"
    draw(data)
    quick_sort(data, left, i - 1)  # 继续处理左边
    quick_sort(data, i + 1, right)  # 继续处理右边
    return


def quickly_sort(data):
    quick_sort(data, 0, len(data) - 1)  # 调用快速排序
    end_of_sort(data)


def merge(data, l, mid, r):
    print(len(data), max(data))
    left = data[l:mid + 1]
    right = data[mid + 1:r + 1]
    k = l
    colors[k] = '#5191E1'
    draw(data)
    colors[k] = '#22BB9C'
    i, j = 0, 0
    while left and right:
        if left[i] <= right[0]:
            colors[k] = '#D0505D'
            data[k] = left[0]
            draw(data)
            colors[k] = '#22BB9C'
            draw(data)
            left.pop(0)
            # data[k] = left.pop(0)  # 移除第一个元素
        else:
            colors[k] = '#D0505D'
            data[k] = right[0]
            draw(data)
            colors[k] = '#22BB9C'
            draw(data)
            right.pop(0)
            # data[k] = right.pop(0)
        k += 1
    tail = left if left else right
    for n in tail:
        colors[k] = '#D0505D'
        draw(data)
        data[k] = n
        colors[k] = '#22BB9C'
        k += 1


def merge_sort_head(lst, l, r):
    if l < r:
        mid = (l + r - 1) // 2
        merge_sort_head(lst, l, mid)
        merge_sort_head(lst, mid + 1, r)
        merge(lst, l, mid, r)


def merge_sort(data, l, r):
    merge_sort_head(data, 0, len(data))
    end_of_sort(data)


window = tk.Tk()
window.title('Wlecome to Sort')
window.geometry('450x400')
var = tk.StringVar()

# Label只画文字
tk.Label(window, text='The speed of the Sort:').place(x=55, y=20)
tk.Label(window, text='The lenth of the array:').place(x=62, y=50)
tk.Label(window, text='Please select the sort method:').place(x=17, y=130)

# Entry画输入字符的窗口
var_lenth = tk.StringVar()  # 设置字符种类
var_lenth.set('35')  # 设置默认值
entry_lenth = tk.Entry(window, textvariable=var_lenth)
entry_lenth.place(x=200, y=52)  # place处理位置信息

# Entry画输入速度的窗口
var_speed = tk.StringVar()  # 设置字符种类
var_speed.set('5.0')  # 设置默认值
entry_speed = tk.Entry(window, textvariable=var_speed)
entry_speed.place(x=200, y=22)  # place处理位置信息


def user_go():
    global data, colors, speed  # 全局化变量
    len_arrary = var_lenth.get()  # 从输入框得到len_array
    speed = var_speed.get()  # 从输入框的到speed
    speed = 10 - float(speed)
    len_arrary = str(len_arrary)  # 先将len_array字符化
    if len_arrary.isdigit():  # 如果len_array是纯整数
        len_arrary = int(len_arrary)
        data = [i for i in range(1, len_arrary + 1)]
        random.shuffle(data)
        for i in range(len(data)):
            colors.append('#22BB9C')
        tk.messagebox.showinfo(title="Success",
                               message="Success load the information!\n"
                                       "Please select the sorting method.")
    else:
        tk.messagebox.askyesno("Error", "Please input an integer(int)!")


def user_exit():
    window.destroy()


# go and exit button
# Button 画开始的按钮
btn_login = tk.Button(window, text='Load the information', command=user_go)
btn_login.place(x=150, y=90)
btn_login = tk.Button(window, text='  Exit  ', command=user_exit)
btn_login.place(x=190, y=345)


def super_sort():
    if len(data) == 0:
        tk.messagebox.askyesno("Error", "Please load the information!")
        return
    random.shuffle(data)
    for i in range(len(data)):
        colors[i] = '#22BB9C'
    if var.get() == 'A':
        bubble_sort(data)
    if var.get() == 'B':
        insert_sort(data)
    if var.get() == 'C':
        selection_sort(data)
    if var.get() == 'D':
        shell_sort(data)
    if var.get() == 'E':
        heap_sort(data)
    if var.get() == 'F':
        quickly_sort(data)
    if var.get() == 'G':
        merge_sort(data, 0, len(data))


# Radiobutton 画排序种类的按钮
rad_but1 = tk.Radiobutton(window, text='BubbleSort',
                          variable=var, value='A',
                          command=super_sort)
rad_but2 = tk.Radiobutton(window, text='InsertSort',
                          variable=var, value='B',
                          command=super_sort)
rad_but3 = tk.Radiobutton(window, text='SelectionSort',
                          variable=var, value='C',
                          command=super_sort)
rad_but4 = tk.Radiobutton(window, text='ShellSort',
                          variable=var, value='D',
                          command=super_sort)
rad_but5 = tk.Radiobutton(window, text='HeapSort',
                          variable=var, value='E',
                          command=super_sort)
rad_but6 = tk.Radiobutton(window, text='QuicklySort',
                          variable=var, value='F',
                          command=super_sort)
rad_but7 = tk.Radiobutton(window, text='MergeSort',
                          variable=var, value='G',
                          command=super_sort)
rad_but1.place(x=200, y=130)
rad_but2.place(x=200, y=160)
rad_but3.place(x=200, y=190)
rad_but4.place(x=200, y=220)
rad_but5.place(x=200, y=250)
rad_but6.place(x=200, y=280)
rad_but7.place(x=200, y=310)

window.mainloop()
