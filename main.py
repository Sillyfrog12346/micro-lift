def on_button_pressed_a():
    global floorNumber
    if floorNumber == 0:
        basic.show_leds("""
            # # # # .
            # . . . #
            # # # # .
            # . . . #
            # # # # .
            """)
        basic.show_leds("""
            . . . . .
            # # # # .
            # . . . #
            # # # # .
            # . . . #
            """)
        basic.show_leds("""
            . # # # .
            . . . . .
            # # # # .
            # . . . #
            # # # # .
            """)
        basic.show_leds("""
            # . . . #
            . # # # .
            . . . . .
            # # # # .
            # . . . #
            """)
        basic.show_leds("""
            # . . # #
            # . . . #
            . # # # .
            . . . . .
            # # # # .
            """)
        basic.show_leds("""
            # . . . .
            # . . # #
            # . . . #
            . # # # .
            . . . . .
            """)
        basic.show_leds("""
            . # # # .
            # . . . .
            # . . # #
            # . . . #
            . # # # .
            """)
        floorNumber += 1
    else:
        if floorNumber == 1:
            basic.show_leds("""
                . # # # .
                # . . . .
                # . . # #
                # . . . #
                . # # # .
                """)
            basic.show_leds("""
                . . . . .
                . # # # .
                # . . . .
                # . . # #
                # . . . #
                """)
            basic.show_leds("""
                # # # # #
                . . . . .
                . # # # .
                # . . . .
                # . . # #
                """)
            basic.show_leds("""
                . . # . .
                # # # # #
                . . . . .
                . # # # .
                # . . . .
                """)
            basic.show_leds("""
                . . # . .
                . . # . .
                # # # # #
                . . . . .
                . # # # .
                """)
            basic.show_leds("""
                . # # . .
                . . # . .
                . . # . .
                # # # # #
                . . . . .
                """)
            basic.show_leds("""
                . . # . .
                . # # . .
                . . # . .
                . . # . .
                # # # # #
                """)
            floorNumber += 1
        else:
            if floorNumber == 2:
                basic.show_leds("""
                    . . # . .
                    . # # . .
                    . . # . .
                    . . # . .
                    # # # # #
                    """)
                basic.show_leds("""
                    . . . . .
                    . . # . .
                    . # # . .
                    . . # . .
                    . . # . .
                    """)
                basic.show_leds("""
                    # # # # #
                    . . . . .
                    . . # . .
                    . # # . .
                    . . # . .
                    """)
                basic.show_leds("""
                    . # . . .
                    # # # # #
                    . . . . .
                    . . # . .
                    . # # . .
                    """)
                basic.show_leds("""
                    . . # . .
                    . # . . .
                    # # # # #
                    . . . . .
                    . . # . .
                    """)
                basic.show_leds("""
                    . . . # #
                    . . # . .
                    . # . . .
                    # # # # #
                    . . . . .
                    """)
                basic.show_leds("""
                    . # # # .
                    # . . # #
                    . . # . .
                    . # . . .
                    # # # # #
                    """)
                floorNumber = 3
            else:
                if floorNumber == 3:
                    basic.show_leds("""
                        # . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        # . . . #
                        """)
    basic.pause(2500)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global floorNumber
    if floorNumber == 1:
        basic.show_leds("""
            . # # # .
            # . . . .
            # . . # #
            # . . . #
            . # # # .
            """)
        basic.show_leds("""
            # . . . .
            # . . # #
            # . . . #
            . # # # .
            . . . . .
            """)
        basic.show_leds("""
            # . . # #
            # . . . #
            . # # # .
            . . . . .
            # # # # .
            """)
        basic.show_leds("""
            # . . . #
            . # # # .
            . . . . .
            # # # # .
            # . . . #
            """)
        basic.show_leds("""
            . # # # .
            . . . . .
            # # # # .
            # . . . #
            # # # # .
            """)
        basic.show_leds("""
            . . . . .
            # # # # .
            # . . . #
            # # # # .
            # . . . #
            """)
        basic.show_leds("""
            # # # # .
            # . . . #
            # # # # .
            # . . . #
            # # # # .
            """)
        floorNumber += -1
    else:
        if floorNumber == 2:
            basic.show_leds("""
                . . # . .
                . # # . .
                . . # . .
                . . # . .
                # # # # #
                """)
            basic.show_leds("""
                . # # . .
                . . # . .
                . . # . .
                # # # # #
                . . . . .
                """)
            basic.show_leds("""
                . . # . .
                . . # . .
                # # # # #
                . . . . .
                . # # # .
                """)
            basic.show_leds("""
                . . # . .
                # # # # #
                . . . . .
                . # # # .
                # . . . .
                """)
            basic.show_leds("""
                # # # # #
                . . . . .
                . # # # .
                # . . . .
                # . . # #
                """)
            basic.show_leds("""
                . . . . .
                . # # # .
                # . . . .
                # . . # #
                # . . . #
                """)
            basic.show_leds("""
                . # # # .
                # . . . .
                # . . # #
                # . . . #
                . # # # .
                """)
            basic.show_leds("""
                # . . . .
                # . . # #
                # . . . #
                . # # # .
                . . . . .
                """)
            basic.show_leds("""
                # . . # #
                # . . . #
                . # # # .
                . . . . .
                # # # # .
                """)
            basic.show_leds("""
                # . . . #
                . # # # .
                . . . . .
                # # # # .
                # . . . #
                """)
            basic.show_leds("""
                . # # # .
                . . . . .
                # # # # .
                # . . . #
                # # # # .
                """)
            basic.show_leds("""
                . . . . .
                # # # # .
                # . . . #
                # # # # .
                # . . . #
                """)
            basic.show_leds("""
                # # # # .
                # . . . #
                # # # # .
                # . . . #
                # # # # .
                """)
            floorNumber = 0
        else:
            if floorNumber == 0:
                basic.show_leds("""
                    # . . . #
                    . # . # .
                    . . # . .
                    . # . # .
                    # . . . #
                    """)
            else:
                if floorNumber == 3:
                    basic.show_leds("""
                        . # # # .
                        # . . # #
                        . . # . .
                        . # . . .
                        # # # # #
                        """)
                    basic.show_leds("""
                        # . . # .
                        . . # . .
                        . # . . .
                        # # # # #
                        . . . . .
                        """)
                    basic.show_leds("""
                        . . # . .
                        . # . . .
                        # # # # #
                        . . . . .
                        . . # . .
                        """)
                    basic.show_leds("""
                        . # . . .
                        # # # # #
                        . . . . .
                        . . # . .
                        . # # . .
                        """)
                    basic.show_leds("""
                        # # # # #
                        . . . . .
                        . . # . .
                        . # # . .
                        . . # . .
                        """)
                    basic.show_leds("""
                        . . . . .
                        . . # . .
                        . # # . .
                        . . # . .
                        . . # . .
                        """)
                    basic.show_leds("""
                        . . # . .
                        . # # . .
                        . . # . .
                        . . # . .
                        # # # # #
                        """)
                    basic.show_leds("""
                        . # # . .
                        . . # . .
                        . . # . .
                        # # # # #
                        . . . . .
                        """)
                    basic.show_leds("""
                        . . # . .
                        . . # . .
                        # # # # #
                        . . . . .
                        . # # # .
                        """)
                    basic.show_leds("""
                        . . # . .
                        # # # # #
                        . . . . .
                        . # # # .
                        # . . . .
                        """)
                    basic.show_leds("""
                        # # # # #
                        . . . . .
                        . # # # .
                        # . . . .
                        # . . # #
                        """)
                    basic.show_leds("""
                        . . . . .
                        . # # # .
                        # . . . .
                        # . . # #
                        # . . . #
                        """)
                    basic.show_leds("""
                        . # # # .
                        # . . . .
                        # . . # #
                        # . . . #
                        . # # # .
                        """)
                    basic.show_leds("""
                        # . . . .
                        # . . # #
                        # . . . #
                        . # # # .
                        . . . . .
                        """)
                    basic.show_leds("""
                        # . . # #
                        # . . . #
                        . # # # .
                        . . . . .
                        # # # # .
                        """)
                    basic.show_leds("""
                        # . . . #
                        . # # # .
                        . . . . .
                        # # # # .
                        # . . . #
                        """)
                    basic.show_leds("""
                        . # # # .
                        . . . . .
                        # # # # .
                        # . . . #
                        # # # # .
                        """)
                    basic.show_leds("""
                        . . . . .
                        # # # # .
                        # . . . #
                        # # # # .
                        # . . . #
                        """)
                    basic.show_leds("""
                        # # # # .
                        # . . . #
                        # # # # .
                        # . . . #
                        # # # # .
                        """)
                    floorNumber = 0
                else:
                    if floorNumber == 0:
                        basic.show_leds("""
                            # . . . #
                            . # . # .
                            . . # . .
                            . # . # .
                            # . . . #
                            """)
    basic.pause(2500)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global floorNumber
    if floorNumber == 0:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
    else:
        if floorNumber == 1:
            basic.show_icon(IconNames.NO)
        else:
            if floorNumber == 2:
                basic.show_leds("""
                    . . # . .
                    . # # . .
                    . . # . .
                    . . # . .
                    # # # # #
                    """)
                basic.show_leds("""
                    . # # . .
                    . . # . .
                    . . # . .
                    # # # # #
                    . . . . .
                    """)
                basic.show_leds("""
                    . . # . .
                    . . # . .
                    # # # # #
                    . . . . .
                    . # # # .
                    """)
                basic.show_leds("""
                    . . # . .
                    # # # # #
                    . . . . .
                    . # # # .
                    # . . . .
                    """)
                basic.show_leds("""
                    # # # # #
                    . . . . .
                    . # # # .
                    # . . . .
                    # . . # #
                    """)
                basic.show_leds("""
                    . . . . .
                    . # # # .
                    # . . . .
                    # . . # #
                    # . . . #
                    """)
                basic.show_leds("""
                    . # # # .
                    # . . . .
                    # . . # #
                    # . . . #
                    . # # # .
                    """)
                floorNumber += -1
            else:
                if floorNumber == 3:
                    basic.show_leds("""
                        . # # # .
                        # . . # #
                        . . # . .
                        . # . . .
                        # # # # #
                        """)
                    basic.show_leds("""
                        # . . # #
                        . . # . .
                        . # . . .
                        # # # # #
                        . . . . .
                        """)
                    basic.show_leds("""
                        . . # . .
                        . # . . .
                        # # # # #
                        . . . . .
                        . . # . .
                        """)
                    basic.show_leds("""
                        . # . . .
                        # # # # #
                        . . . . .
                        . . # . .
                        . # # . .
                        """)
                    basic.show_leds("""
                        # # # # #
                        . . . . .
                        . . # . .
                        . # # . .
                        . . # . .
                        """)
                    basic.show_leds("""
                        . . . . .
                        . . # . .
                        . # # . .
                        . . # . .
                        . . # . .
                        """)
                    basic.show_leds("""
                        . . # . .
                        . # # . .
                        . . # . .
                        . . # . .
                        # # # # #
                        """)
                    floorNumber += -1
    basic.pause(2500)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

floorNumber = 0
led.set_brightness(200)
basic.show_leds("""
    . # # # .
    # . . . #
    # . . . #
    # . . . #
    . # # # .
    """)
basic.pause(1000)
basic.show_leds("""
    . . . . .
    # # # # #
    # . . . #
    # # # # #
    . . . . .
    """)
for index in range(26):
    led.toggle(1, 2)
    basic.pause(100)
    led.toggle(2, 2)
    basic.pause(100)
    led.toggle(3, 2)
    basic.pause(100)
floorNumber = 1
basic.show_leds("""
    # . . . #
    # . . . #
    # # # # #
    # . . . #
    # . . . #
    """)
basic.show_leds("""
    # # # # #
    . . # . .
    . . # . .
    . . # . .
    # # # # #
    """)
basic.show_string(" Basement=A+B")
basic.clear_screen()

def on_forever():
    pass
basic.forever(on_forever)
