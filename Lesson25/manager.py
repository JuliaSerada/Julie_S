from bus import Bus


class Manager:

    # fool-prove

    def find_bus(buses):
        if not isinstance(buses, (list, tuple)):
            return Bus()

        target = buses[0]  # first bus by index 0

        for bus in buses:
            if isinstance(bus, Bus):
                if (bus.price / bus.number) < (target.price / target.number):
                    target = bus

        return target
