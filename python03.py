def pressure(v,t,n):
    """ compute the pressure in pascals of an ideal gas
    
    applies the ideal gas law
    v--- volume of gas , in cubic meters
    t--- absolute temperature in degrees kelvin
    n--- particles of gas """
    
    k= (1.38e-23) # boltznann constant
    result= n*k*t/v
