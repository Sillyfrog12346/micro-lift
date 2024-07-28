input.onButtonPressed(Button.A, function () {
    if (floorNumber == 0) {
        basic.showLeds(`
            # # # # .
            # . . . #
            # # # # .
            # . . . #
            # # # # .
            `)
        basic.showLeds(`
            . . . . .
            # # # # .
            # . . . #
            # # # # .
            # . . . #
            `)
        basic.showLeds(`
            . # # # .
            . . . . .
            # # # # .
            # . . . #
            # # # # .
            `)
        basic.showLeds(`
            # . . . #
            . # # # .
            . . . . .
            # # # # .
            # . . . #
            `)
        basic.showLeds(`
            # . . # #
            # . . . #
            . # # # .
            . . . . .
            # # # # .
            `)
        basic.showLeds(`
            # . . . .
            # . . # #
            # . . . #
            . # # # .
            . . . . .
            `)
        basic.showLeds(`
            . # # # .
            # . . . .
            # . . # #
            # . . . #
            . # # # .
            `)
        floorNumber += 1
    } else if (floorNumber == 1) {
        basic.showLeds(`
            . # # # .
            # . . . .
            # . . # #
            # . . . #
            . # # # .
            `)
        basic.showLeds(`
            . . . . .
            . # # # .
            # . . . .
            # . . # #
            # . . . #
            `)
        basic.showLeds(`
            # # # # #
            . . . . .
            . # # # .
            # . . . .
            # . . # #
            `)
        basic.showLeds(`
            . . # . .
            # # # # #
            . . . . .
            . # # # .
            # . . . .
            `)
        basic.showLeds(`
            . . # . .
            . . # . .
            # # # # #
            . . . . .
            . # # # .
            `)
        basic.showLeds(`
            . # # . .
            . . # . .
            . . # . .
            # # # # #
            . . . . .
            `)
        basic.showLeds(`
            . . # . .
            . # # . .
            . . # . .
            . . # . .
            # # # # #
            `)
        floorNumber += 1
    } else if (floorNumber == 2) {
        basic.showLeds(`
            . . # . .
            . # # . .
            . . # . .
            . . # . .
            # # # # #
            `)
        basic.showLeds(`
            . . . . .
            . . # . .
            . # # . .
            . . # . .
            . . # . .
            `)
        basic.showLeds(`
            # # # # #
            . . . . .
            . . # . .
            . # # . .
            . . # . .
            `)
        basic.showLeds(`
            . # . . .
            # # # # #
            . . . . .
            . . # . .
            . # # . .
            `)
        basic.showLeds(`
            . . # . .
            . # . . .
            # # # # #
            . . . . .
            . . # . .
            `)
        basic.showLeds(`
            . . . # #
            . . # . .
            . # . . .
            # # # # #
            . . . . .
            `)
        basic.showLeds(`
            . # # # .
            # . . # #
            . . # . .
            . # . . .
            # # # # #
            `)
        floorNumber = 3
    } else if (floorNumber == 3) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
    }
    basic.pause(2500)
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function () {
    if (floorNumber == 1) {
        basic.showLeds(`
            . # # # .
            # . . . .
            # . . # #
            # . . . #
            . # # # .
            `)
        basic.showLeds(`
            # . . . .
            # . . # #
            # . . . #
            . # # # .
            . . . . .
            `)
        basic.showLeds(`
            # . . # #
            # . . . #
            . # # # .
            . . . . .
            # # # # .
            `)
        basic.showLeds(`
            # . . . #
            . # # # .
            . . . . .
            # # # # .
            # . . . #
            `)
        basic.showLeds(`
            . # # # .
            . . . . .
            # # # # .
            # . . . #
            # # # # .
            `)
        basic.showLeds(`
            . . . . .
            # # # # .
            # . . . #
            # # # # .
            # . . . #
            `)
        basic.showLeds(`
            # # # # .
            # . . . #
            # # # # .
            # . . . #
            # # # # .
            `)
        floorNumber += -1
    } else if (floorNumber == 2) {
        basic.showLeds(`
            . . # . .
            . # # . .
            . . # . .
            . . # . .
            # # # # #
            `)
        basic.showLeds(`
            . # # . .
            . . # . .
            . . # . .
            # # # # #
            . . . . .
            `)
        basic.showLeds(`
            . . # . .
            . . # . .
            # # # # #
            . . . . .
            . # # # .
            `)
        basic.showLeds(`
            . . # . .
            # # # # #
            . . . . .
            . # # # .
            # . . . .
            `)
        basic.showLeds(`
            # # # # #
            . . . . .
            . # # # .
            # . . . .
            # . . # #
            `)
        basic.showLeds(`
            . . . . .
            . # # # .
            # . . . .
            # . . # #
            # . . . #
            `)
        basic.showLeds(`
            . # # # .
            # . . . .
            # . . # #
            # . . . #
            . # # # .
            `)
        basic.showLeds(`
            # . . . .
            # . . # #
            # . . . #
            . # # # .
            . . . . .
            `)
        basic.showLeds(`
            # . . # #
            # . . . #
            . # # # .
            . . . . .
            # # # # .
            `)
        basic.showLeds(`
            # . . . #
            . # # # .
            . . . . .
            # # # # .
            # . . . #
            `)
        basic.showLeds(`
            . # # # .
            . . . . .
            # # # # .
            # . . . #
            # # # # .
            `)
        basic.showLeds(`
            . . . . .
            # # # # .
            # . . . #
            # # # # .
            # . . . #
            `)
        basic.showLeds(`
            # # # # .
            # . . . #
            # # # # .
            # . . . #
            # # # # .
            `)
        floorNumber = 0
    } else if (floorNumber == 0) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
    } else if (floorNumber == 3) {
        basic.showLeds(`
            . # # # .
            # . . # #
            . . # . .
            . # . . .
            # # # # #
            `)
        basic.showLeds(`
            # . . # .
            . . # . .
            . # . . .
            # # # # #
            . . . . .
            `)
        basic.showLeds(`
            . . # . .
            . # . . .
            # # # # #
            . . . . .
            . . # . .
            `)
        basic.showLeds(`
            . # . . .
            # # # # #
            . . . . .
            . . # . .
            . # # . .
            `)
        basic.showLeds(`
            # # # # #
            . . . . .
            . . # . .
            . # # . .
            . . # . .
            `)
        basic.showLeds(`
            . . . . .
            . . # . .
            . # # . .
            . . # . .
            . . # . .
            `)
        basic.showLeds(`
            . . # . .
            . # # . .
            . . # . .
            . . # . .
            # # # # #
            `)
        basic.showLeds(`
            . # # . .
            . . # . .
            . . # . .
            # # # # #
            . . . . .
            `)
        basic.showLeds(`
            . . # . .
            . . # . .
            # # # # #
            . . . . .
            . # # # .
            `)
        basic.showLeds(`
            . . # . .
            # # # # #
            . . . . .
            . # # # .
            # . . . .
            `)
        basic.showLeds(`
            # # # # #
            . . . . .
            . # # # .
            # . . . .
            # . . # #
            `)
        basic.showLeds(`
            . . . . .
            . # # # .
            # . . . .
            # . . # #
            # . . . #
            `)
        basic.showLeds(`
            . # # # .
            # . . . .
            # . . # #
            # . . . #
            . # # # .
            `)
        basic.showLeds(`
            # . . . .
            # . . # #
            # . . . #
            . # # # .
            . . . . .
            `)
        basic.showLeds(`
            # . . # #
            # . . . #
            . # # # .
            . . . . .
            # # # # .
            `)
        basic.showLeds(`
            # . . . #
            . # # # .
            . . . . .
            # # # # .
            # . . . #
            `)
        basic.showLeds(`
            . # # # .
            . . . . .
            # # # # .
            # . . . #
            # # # # .
            `)
        basic.showLeds(`
            . . . . .
            # # # # .
            # . . . #
            # # # # .
            # . . . #
            `)
        basic.showLeds(`
            # # # # .
            # . . . #
            # # # # .
            # . . . #
            # # # # .
            `)
        floorNumber = 0
    } else if (floorNumber == 0) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
    }
    basic.pause(2500)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    if (floorNumber == 0) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
    } else if (floorNumber == 1) {
        basic.showIcon(IconNames.No)
    } else if (floorNumber == 2) {
        basic.showLeds(`
            . . # . .
            . # # . .
            . . # . .
            . . # . .
            # # # # #
            `)
        basic.showLeds(`
            . # # . .
            . . # . .
            . . # . .
            # # # # #
            . . . . .
            `)
        basic.showLeds(`
            . . # . .
            . . # . .
            # # # # #
            . . . . .
            . # # # .
            `)
        basic.showLeds(`
            . . # . .
            # # # # #
            . . . . .
            . # # # .
            # . . . .
            `)
        basic.showLeds(`
            # # # # #
            . . . . .
            . # # # .
            # . . . .
            # . . # #
            `)
        basic.showLeds(`
            . . . . .
            . # # # .
            # . . . .
            # . . # #
            # . . . #
            `)
        basic.showLeds(`
            . # # # .
            # . . . .
            # . . # #
            # . . . #
            . # # # .
            `)
        floorNumber += -1
    } else if (floorNumber == 3) {
        basic.showLeds(`
            . # # # .
            # . . # #
            . . # . .
            . # . . .
            # # # # #
            `)
        basic.showLeds(`
            # . . # #
            . . # . .
            . # . . .
            # # # # #
            . . . . .
            `)
        basic.showLeds(`
            . . # . .
            . # . . .
            # # # # #
            . . . . .
            . . # . .
            `)
        basic.showLeds(`
            . # . . .
            # # # # #
            . . . . .
            . . # . .
            . # # . .
            `)
        basic.showLeds(`
            # # # # #
            . . . . .
            . . # . .
            . # # . .
            . . # . .
            `)
        basic.showLeds(`
            . . . . .
            . . # . .
            . # # . .
            . . # . .
            . . # . .
            `)
        basic.showLeds(`
            . . # . .
            . # # . .
            . . # . .
            . . # . .
            # # # # #
            `)
        floorNumber += -1
    }
    basic.pause(2500)
    basic.clearScreen()
})
let floorNumber = 0
led.setBrightness(200)
basic.showLeds(`
    . # # # .
    # . . . #
    # . . . #
    # . . . #
    . # # # .
    `)
basic.pause(1000)
basic.showLeds(`
    . . . . .
    # # # # #
    # . . . #
    # # # # #
    . . . . .
    `)
for (let index = 0; index < 26; index++) {
    led.toggle(1, 2)
    basic.pause(100)
    led.toggle(2, 2)
    basic.pause(100)
    led.toggle(3, 2)
    basic.pause(100)
}
floorNumber = 1
basic.showLeds(`
    # . . . #
    # . . . #
    # # # # #
    # . . . #
    # . . . #
    `)
basic.showLeds(`
    # # # # #
    . . # . .
    . . # . .
    . . # . .
    # # # # #
    `)
basic.showString(" Basement=A+B")
basic.clearScreen()
basic.forever(function () {
	
})
