def Hanoi(count_disks: int, source, middle, destination):
    if count_disks == 1:
        print(f"Move disk {count_disks} from {source} to {destination}")
        return
    Hanoi(count_disks - 1, source, destination, middle)
    print(f"Moving disk {count_disks} from{source} to {destination}")
    Hanoi(count_disks - 1, middle, source, destination)


Hanoi(4, 'A', 'B', 'C')
