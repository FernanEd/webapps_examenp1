def calcularComision(num):
  if num < 50000:
    return num * 0.05
  elif num < 250000:
    return num * 0.0365
  elif num < 500000:
    return num * 0.0345
  elif num < 1000000:
    return  num * 0.0315
  else:
    return num * 0.0295