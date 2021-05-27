def calcularComision(num):
  if num < 50000:
    return 5
  elif num < 250000:
    return 5 + ( num * 0.0365 )
  elif num < 500000:
    return 5 + ( num * 0.0345 )
  elif num < 1000000:
    return  5 + ( num * 0.0315 )
  else:
    return 5 + ( num * 0.0295 )