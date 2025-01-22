import numpy as np

def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0])

#np.multiply(np.multiply(np.add(np.add(np.add(-51.81814669987016, np.multiply(x[0], x[1])), np.maximum(np.multiply(x[0], x[1]), -4.884217383927211)), np.multiply(np.multiply(4.893313914157078, x[0]), np.reciprocal(np.divide(1.5827088050437421, x[2])))), np.add(np.subtract(np.multiply(x[1], 4.953136254469275), np.multiply(-4.884217383927211, x[2])), np.multiply(9.996265568395703, np.minimum(x[0], 4.356894927194286)))), np.multiply(np.add(np.multiply(np.multiply(x[1], 18.649830776786864), np.reciprocal(np.divide(-3.493460646283637, x[2]))), np.subtract(np.multiply(x[0], np.multiply(2.510264066743016, x[2])), -248.23328707719287)), np.divide(np.add(np.add(-82.50101783674046, np.multiply(x[0], x[1])), np.absolute(np.multiply(-9.996265568395703, x[0]))), 3.0042241506957357)))
def f2(x: np.ndarray) -> np.ndarray:
    return (((((-51.81814669987016 + (x[0] * x[1])) + np.maximum((x[0] * x[1]), -4.884217383927211)) + ((4.893313914157078 * x[0]) * np.reciprocal((1.5827088050437421 / x[2])))) * (((x[1] * 4.953136254469275) - (-4.884217383927211 * x[2])) + (9.996265568395703 * np.minimum(x[0], 4.356894927194286)))) * ((((x[1] * 18.649830776786864) * np.reciprocal((-3.493460646283637 / x[2]))) + ((x[0] * (2.510264066743016 * x[2])) - -248.23328707719287)) * (((-82.50101783674046 + (x[0] * x[1])) + np.absolute((-9.996265568395703 * x[0]))) / 3.0042241506957357)))

#np.add(np.multiply(np.arctan(np.add(np.divide(np.subtract(x[2], -2.065621497047198), 3.7609747965545135), 14.11482758558892)), 2.6622227984463516), np.negative(np.add(np.add(np.multiply(np.square(x[0]), -2.0), np.divide(3.503326125821749, np.reciprocal(x[2]))), np.multiply(x[1], np.square(x[1])))))
def f3(x: np.ndarray) -> np.ndarray:
    return ((np.arctan((((x[2] - -2.065621497047198) / 3.7609747965545135) + 14.11482758558892)) * 2.6622227984463516) + -((((np.square(x[0]) * -2.0) + (3.503326125821749 / np.reciprocal(x[2]))) + (x[1] * np.square(x[1])))))

# np.subtract(np.multiply(7.000000614701995, np.cos(np.reciprocal(np.reciprocal(x[1])))), np.subtract(np.divide(np.subtract(np.add(x[0], x[0]), 3.1292631691925386), 21.99978866375695), 3.1371774184176267))
def f4(x: np.ndarray) -> np.ndarray: 
    return ((7.000000614701995 * np.cos(np.reciprocal(np.reciprocal(x[1])))) - ((((x[0] + x[0]) - 3.1292631691925386) / 21.99978866375695) - 3.1371774184176267))
    
#np.multiply(4.356153822762008e-11, np.divide(np.add(0.18873497848879503, np.add(-4.311704549797579, np.power(np.sqrt(x[0]), x[1]))), np.divide(-4.311704549797579, np.add(3.8872132896946994, np.power(np.sqrt(x[0]), x[1])))))
def f5(x: np.ndarray) -> np.ndarray: 
    return (4.356153822762008e-11 * ((0.18873497848879503 + (-4.311704549797579 + np.power(np.sqrt(x[0]), x[1]))) / (-4.311704549797579 / (3.8872132896946994 + np.power(np.sqrt(x[0]), x[1])))))

#np.add(np.multiply(0.6946269287372357, np.multiply(-0.9998472454638713, np.minimum(8.692112438892295, x[0]))), np.divide(-7.69887037157223, np.divide(-4.543393686903389, x[1])))
def f6(x: np.ndarray) -> np.ndarray: 
    return ((0.6946269287372357 * (-0.9998472454638713 * np.minimum(8.692112438892295, x[0]))) + (-7.69887037157223 / (-4.543393686903389 / x[1])))

#np.subtract(np.power(np.power(np.square(np.subtract(x[1], x[0])), np.divide(x[0], -5.239844422536422)), np.add(np.minimum(1.896493075050202, x[0]), np.remainder(x[1], 0.17997037571963403))), np.divide(np.multiply(0.5318365347088865, np.square(x[1])), np.add(-1.0085421764494056, np.cos(np.subtract(x[1], x[0])))))
def f7(x: np.ndarray) -> np.ndarray:
    return (np.power(np.power(np.square((x[1] - x[0])), (x[0] / -5.239844422536422)), (np.minimum(1.896493075050202, x[0]) + np.remainder(x[1], 0.17997037571963403))) - ((0.5318365347088865 * np.square(x[1])) / (-1.0085421764494056 + np.cos((x[1] - x[0])))))

#np.add(np.add(np.divide(np.subtract(-7540.826857026908, np.subtract(np.square(x[1]), np.add(x[2], x[0]))), np.multiply(np.multiply(-19.741842726315273, np.exp(x[5])), -3.9779795080988234)), np.add(np.multiply(np.multiply(np.square(x[5]), -32.660938490698086), -1.6690374979040925), np.subtract(np.divide(-18.385241718800962, np.exp(x[4])), np.multiply(-4.963012888395526, np.sinh(x[3]))))), np.add(np.multiply(np.subtract(x[5], np.power(0.9422005781130904, np.exp(x[5]))), np.subtract(np.multiply(np.square(x[5]), np.square(x[5])), np.multiply(-16.345502872293693, np.exp(x[5])))), np.subtract(np.divide(np.add(np.multiply(x[5], 17.60134866937029), np.multiply(x[5], 17.60134866937029)), -0.26962500598603156), np.subtract(np.multiply(np.exp(x[4]), 18.34079626746933), np.add(122.0987615004006, np.multiply(9.539347080016679, x[3]))))))
def f8(x: np.ndarray) -> np.ndarray: 
    return ((((-7540.826857026908 - (np.square(x[1]) - (x[2] + x[0]))) / ((-19.741842726315273 * np.exp(x[5])) * -3.9779795080988234)) + (((np.square(x[5]) * -32.660938490698086) * -1.6690374979040925) + ((-18.385241718800962 / np.exp(x[4])) - (-4.963012888395526 * np.sinh(x[3]))))) + (((x[5] - np.power(0.9422005781130904, np.exp(x[5]))) * ((np.square(x[5]) * np.square(x[5])) - (-16.345502872293693 * np.exp(x[5])))) + ((((x[5] * 17.60134866937029) + (x[5] * 17.60134866937029)) / -0.26962500598603156) - ((np.exp(x[4]) * 18.34079626746933) - (122.0987615004006 + (9.539347080016679 * x[3]))))))


