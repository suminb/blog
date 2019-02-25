---
author:
  display_name: Sumin
  email: suminb@gmail.com
  first_name: Sumin
  last_name: Byeon
categories:
- Geeky Stuff
layout: post
meta: null
post_id: '1920'
published: true
redirect_from:
- /post/raspberry-pi-gpio
status: publish
tags:
- Raspberry Pi
- LED
title: 라즈베리 파이의 GPIO를 이용하여 LED 조작하기
type: post
---

주말을 알차게 보내기 위해 초간단 프로젝트를 준비해보았다. 바로 라즈베리 파이의 GPIO 핀을 이용해서 코드상에서 LED를 켜고 끌 수 있게 만드는 것.

회로 구성
-------

너무 간단해서 회로도가 필요할까 하는 생각도 들지만, 회로 구성은 이렇다.

![](http://www.raspberrypi.org/documentation/usage/gpio/images/simple-circuit.png)

회로도와 자세한 설명은 [이 페이지](http://www.raspberrypi.org/documentation/usage/gpio/)에서 볼 수 있다.

저항을 붙여놓은 이유가 LED를 보호하기 위해서[^1]라고 원문은 설명하고 있는데, 그 *보호*한다는 의미가 LED가 원래 GPIO 핀에서 나오는 전류보다 낮은 전류에서 작동한다는 뜻이 아닐까 한다.

그리고 회로에 있는 스위치의 역할을 프로그램 코드가 해 줄 것이다.


GPIO
----

말 그대로 범용(general purpose) 입출력 장치이다. 라즈베리 파이 B+ 타입을 보면 핀이 40개 있는데, 이 중 26개가 범용 입출력 핀이다. 출력도 되고 입력도 된다. 각 핀의 역할은 [이 페이지](http://www.panu.it/raspberry/)를 참고하면 알 수 있다.


Python Code
-----------

    import RPi.GPIO as GPIO
    import time
     
    PIN = 3
    INTERVAL = 1.0
     
    def main():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(PIN, GPIO.OUT)
     
        while True:
            GPIO.output(PIN, 1)
            time.sleep(INTERVAL)
     
            GPIO.output(PIN, 0)
            time.sleep(INTERVAL)
     
     
    if __name__ == '__main__':
        try:
            main()
        except KeyboardInterrupt:
            GPIO.cleanup()

Go Code
-------

[github.com/davecheney/gpio 에 있는 예제](https://github.com/davecheney/gpio/blob/master/examples/blink/blink.go)를 약간 변형해봤다.

    import (
            "fmt"
            "os"
            "os/signal"
            "time"
     
            "github.com/davecheney/gpio"
    )
     
    func main() {
        // set GPIO25 to output mode
        pin, err := gpio.OpenPin(2, gpio.ModeOutput)
        if err != nil {
            fmt.Printf("Error opening pin! %s\n", err)
            return
        }
 
        // turn the led off on exit
        c := make(chan os.Signal, 1)
        signal.Notify(c, os.Interrupt)
        go func() {
            for _ = range c {
                fmt.Printf("\nClearing and unexporting the pin.\n")
                pin.Clear()
                pin.Close()
                os.Exit(0)
            }
        }()
 
        for {
            pin.Set()
            time.Sleep(1000 * time.Millisecond)
            pin.Clear()
            time.Sleep(1000 * time.Millisecond)
        }
    }

[^1]: *the resistor is there to protect the LED*