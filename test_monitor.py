from monitor import check_status

assert check_status(200) == True
assert check_status(201) == True
assert check_status(404) == False
assert check_status(500) ==False