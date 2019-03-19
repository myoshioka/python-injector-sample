import os
import sys
from injector import Injector
from container.service_di_container import ServiceDiContainer
from domain.car import Car

# path
pardir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(pardir)


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
    car.run()

    # ElectroEngine
    injector = Injector(
        [ServiceDiContainer(config['services']['ElectroEngine'])])
    car = injector.get(Car)
    car.run()


if __name__ == '__main__':
    main()
