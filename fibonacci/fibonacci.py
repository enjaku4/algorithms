def calc_fib(position):
  if position < 0:
    raise ValueError
  elif position in [0, 1]:
    return position
  else:
    return calc_fib(position - 1) + calc_fib(position - 2)