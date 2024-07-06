def celsiusToFahrenheit(celsius):
    return (celsius * 9.0/5.0) + 32

def fahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

cel=fahrenheitToCelsius(98)
feh=celsiusToFahrenheit(32)

print(cel)
print(feh)
