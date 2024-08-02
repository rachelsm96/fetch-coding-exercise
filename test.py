import pageMethods


def test_find_the_fake_bar():
    left = 0
    right = 1
    sign = None
    pageMethods.set_up()
    while right < 8:
        pageMethods.insert_value_in_left_board(str(left))
        pageMethods.insert_value_in_right_board(str(right))
        pageMethods.click_weigh()
        sign = pageMethods.get_result()
        pageMethods.click_reset()
        if sign == ">" or sign == "<":
            break
        else:
            left += 2
            right += 2
    if sign == ">":
        pageMethods.click_answer(str(right))
    elif sign == "<":
        pageMethods.click_answer(str(left))
    else:
        pageMethods.click_answer("8")
    pageMethods.print_alert_text()
    pageMethods.dismiss_alert()
    pageMethods.output_weightings_list()
    pageMethods.tear_down()