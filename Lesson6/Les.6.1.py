from time import sleep


class TrafficLight:

    _position = {'Красным': 7, 'Жёлтым': 3, 'Зелёным': 10}
    _color = ''

    def running(self):

        for color, ps_time in self._position.items():
            self._color = color

            print(f"Светофор будет гореть '{self._color}' цветом "
                  f"ещё {ps_time} секунд.")

            sleep(ps_time)


if __name__ == '__main__':
    TrafficLight = TrafficLight()
    TrafficLight.running()
