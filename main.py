import os
import sys
from injector import Injector
from container.service_di_container import ServiceDiContainer
from domain.car import Car


def main():

    config = {
        'services': {
            'DieselEngine': {
                'class': 'domain.diesel_engine.DieselEngine'
            },
            'GasolineEngine': {
                'class': 'domain.gasoline_engine.GasolineEngine'
            },
            'ElectroEngine': {
                'class': 'domain.electro_engine.ElectroEngine'
            }
        }
    }

    # DieselEngine
    injector = Injector(
        [ServiceDiContainer(config['services']['DieselEngine'])])
    car = injector.get(Car)
    rtn = car.run()
    print(rtn)

    # ElectroEngine
    injector = Injector(
        [ServiceDiContainer(config['services']['ElectroEngine'])])
    car = injector.get(Car)
    rtn = car.run()
    print(rtn)


if __name__ == '__main__':
    main()
