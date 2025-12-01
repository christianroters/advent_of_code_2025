def turn_wheel(amount: int, direction: str, current_position: int) -> int:
    """Turn the wheel in the specified direction by the specified amount."""
    pos = wheel.index(current_position)
    if direction == "R":
        new_pos = (pos + amount) % len(wheel)
        return wheel[new_pos]
    elif direction == "L":
        new_pos = (pos - amount) % len(wheel)
        return wheel[new_pos]
    else:
        raise ValueError("Invalid direction; must be 'R' or 'L'.")
    

def part_1(start_position: int, data: list[str]) -> None:
    """Calculate how many times the wheel points at 0 after a series of turns."""
    counter = 0
    wheel_position = start_position
    for line in data:
        direction, amount = line[0], int(line[1:])
        wheel_position = turn_wheel(amount, direction, wheel_position)
        counter += 1 if wheel_position == 0 else 0
    print(f"The wheel pointed at 0: {counter} times")
    

def part_2(start_position: int, data: list[str]) -> None:
    """Calculate how many times the wheel clicks past 0 after a series of turns."""
    wheel_position = start_position
    click_counter = 0
    for line in data:
        direction, amount = line[0], int(line[1:])
        previous_position = wheel_position
        wheel_position = turn_wheel(amount, direction, wheel_position)
        click_counter += amount // 100
        if direction == "R":
            if previous_position + amount % 100 > 99:
                click_counter += 1
        elif direction == "L":
            if previous_position - amount % 100 < 1 and previous_position > 0:
                click_counter += 1
    print(f"The wheel clicked past 0: {click_counter} times")
    

if __name__ == "__main__":
    input = open("./day_01/input.txt", "r").read().splitlines()
    wheel = range(0, 100, 1)
    part_1(50, input)
    part_2(50, input)