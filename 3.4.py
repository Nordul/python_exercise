invitation_list = ['nordul', 'lendul', 'bei cheng']
print(f'嘿我的朋友{invitation_list[0].title()}，我想邀请你来共进晚餐')
print(f'嘿我的朋友{invitation_list[1].title()}，我想邀请你来共进晚餐')
print(f'嘿我的朋友{invitation_list[2].title()}，我想邀请你来共进晚餐')
print(f'十分抱歉，我的另一位朋友{invitation_list[2].title()}有事情来不了了')
invitation_list[2] = 'bai ming'
print(f'嘿我的朋友{invitation_list[0].title()}，我想邀请你来共进晚餐')
print(f'嘿我的朋友{invitation_list[1].title()}，我想邀请你来共进晚餐')
print(f'嘿我的朋友{invitation_list[2].title()}，我想邀请你来共进晚餐')
print('就在刚才，我定到了更大的餐桌，所以我打算邀请更多人')
invitation_list.insert(0, 'tian suo')
invitation_list.insert(2, 'pu xiu')
invitation_list.append('python')
print(f'嘿我的朋友{invitation_list[0].title()}，我想邀请你来共进晚餐')
print(f'嘿我的朋友{invitation_list[1].title()}，我想邀请你来共进晚餐')
print(f'嘿我的朋友{invitation_list[2].title()}，我想邀请你来共进晚餐')
print(f'嘿我的朋友{invitation_list[3].title()}，我想邀请你来共进晚餐')
print(f'嘿我的朋友{invitation_list[4].title()}，我想邀请你来共进晚餐')
print(f'嘿我的朋友{invitation_list[5].title()}，我想邀请你来共进晚餐')
print(len(invitation_list))
No_appointment_list5 = invitation_list.pop(5)
print(f'哦抱歉，餐厅临时调整，很抱歉今晚不能邀请你过来了{No_appointment_list5.title()}')
No_appointment_list4 = invitation_list.pop(4)
print(f'哦抱歉，餐厅临时调整，很抱歉今晚不能邀请你过来了{No_appointment_list4.title()}')
No_appointment_list3 = invitation_list.pop(3)
print(f'哦抱歉，餐厅临时调整，很抱歉今晚不能邀请你过来了{No_appointment_list3.title()}')
No_appointment_list2 = invitation_list.pop(2)
print(f'哦抱歉，餐厅临时调整，很抱歉今晚不能邀请你过来了{No_appointment_list2.title()}')
print(f'哦我的朋友{invitation_list[1].title()}，今晚只有两位客人了，你刚好在其中之一，请准时到达')
print(f'哦我的朋友{invitation_list[0].title()}，今晚只有两位客人了，你刚好在其中之一，请准时到达')
del invitation_list[0]
del invitation_list[0]
print(invitation_list)
print(len(invitation_list))