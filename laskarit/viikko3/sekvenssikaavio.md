sequenceDiagram
    External ->>+Machine: Machine()
    Machine->>FuelTank: FuelTank()
    FuelTank ->>FuelTank: fuel_contents = 0
    Machine->>FuelTank: self._tank.fill(40)
    FuelTank ->>FuelTank: fuel_contents = 40

    Machine ->> Engine: Engine(self._tank)
    Engine ->> Engine: fuel_tank = tank
    External ->> Machine: drive
    Machine ->> Engine: start
    Engine ->> FuelTank: consume(5)
    FuelTank ->> FuelTank: fuel_contents = 35
    loop
    Machine ->>+ Engine: is_running()
    Engine ->> FuelTank: fuel_contents > 0
    Engine -->>- Machine: True
    Machine ->>+ Engine: use_energy()
    Engine ->> FuelTank: consume(10)
    FuelTank ->> FuelTank: fuel_contents += -10
    end
    FuelTank ->> FuelTank: fuel_contents = -5
    Engine -->>- Machine: False
