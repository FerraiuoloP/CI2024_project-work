import numpy as np

def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0])

#np.multiply(np.multiply(np.add(np.add(np.add(np.multiply(7.885793211722174, -7.8931273901629595), np.multiply(x[0], x[1])), np.subtract(np.multiply(x[0], x[1]), np.subtract(-9.996265568395703, -3.5368479505381583))), np.multiply(np.multiply(5.517038333390751, x[0]), np.reciprocal(np.divide(1.5827088050437421, x[2])))), np.add(np.subtract(np.multiply(x[1], 4.978572892293439), np.divide(np.multiply(7.885793211722174, x[2]), np.add(0.05336626761377872, -1.6943696697781867))), np.multiply(np.subtract(1.7392443126434909, -7.8931273901629595), x[0]))), np.multiply(np.add(np.multiply(np.multiply(x[1], np.cosh(-3.6182647063354416)), np.reciprocal(np.divide(-3.6182647063354416, x[2]))), np.subtract(np.multiply(x[0], np.multiply(2.6184311110488068, x[2])), np.multiply(np.subtract(5.517038333390751, -9.996265568395703), np.subtract(-9.996265568395703, 6.355714362732318)))), np.divide(np.add(np.add(np.multiply(8.548291176143636, -9.626684954722101), np.multiply(x[0], x[1])), np.absolute(np.multiply(-9.996265568395703, x[0]))), 3.340770779277813)))
def f2(x: np.ndarray) -> np.ndarray:
    return (((((-62.24357039260542 + (x[0] * x[1])) + ((x[0] * x[1]) + 6.459417617857545)) + ((5.517038333390751 * x[0]) * np.reciprocal((1.5827088050437421 / x[2])))) * (((x[1] * 4.978572892293439) - ((7.885793211722174 * x[2]) / -1.641003402164408)) + (9.63237170280645 * x[0]))) * ((((x[1] * 18.649830776786864) * np.reciprocal((-3.6182647063354416 / x[2]))) + ((x[0] * (2.6184311110488068 * x[2])) +253.6732340675021)) * (((-82.29170605396563 + (x[0] * x[1])) + np.absolute((-9.996265568395703 * x[0]))) / 3.340770779277813)))

#np.add(np.multiply(np.arctan(np.add(np.divide(np.subtract(x[2], -2.065621497047198), 3.7609747965545135), 14.11482758558892)), 2.6622227984463516), np.negative(np.add(np.add(np.multiply(np.square(x[0]), -2.0), np.divide(3.503326125821749, np.reciprocal(x[2]))), np.multiply(x[1], np.square(x[1])))))
def f3(x: np.ndarray) -> np.ndarray:
    return ((np.arctan((((x[2] - -2.065621497047198) / 3.7609747965545135) + 14.11482758558892)) * 2.6622227984463516) + -((((np.square(x[0]) * -2.0) + (3.503326125821749 / np.reciprocal(x[2]))) + (x[1] * np.square(x[1])))))

# np.add(np.multiply(np.cos(x[1]), 7.000000792991886), np.multiply(np.subtract(np.subtract(1.6102655062320324, np.power(np.add(15.27657903079583, x[0]), -4.681065427551907)), np.power(2.2239667716288487, np.subtract(-10.64590793887777, np.power(1.4396983786605233, x[0])))), np.divide(np.add(-8.731509378683597, np.divide(np.subtract(14.312198011080312, x[0]), -2.490229650218498)), -7.108999793736638)))
def f4(x: np.ndarray) -> np.ndarray: 
    return ((np.cos(x[1]) * 7.000000792991886) + (((1.6102655062320324 - np.power((15.27657903079583 + x[0]), -4.681065427551907)) - np.power(2.2239667716288487, (-10.64590793887777 - np.power(1.4396983786605233, x[0])))) * ((-8.731509378683597 + ((14.312198011080312 - x[0]) / -2.490229650218498)) / -7.108999793736638)))

#np.multiply(4.356153822762008e-11, np.divide(np.add(0.18873497848879503, np.add(-4.311704549797579, np.power(np.sqrt(x[0]), x[1]))), np.divide(-4.311704549797579, np.add(3.8872132896946994, np.power(np.sqrt(x[0]), x[1])))))
def f5(x: np.ndarray) -> np.ndarray: 
    return (4.356153822762008e-11 * ((0.18873497848879503 + (-4.311704549797579 + np.power(np.sqrt(x[0]), x[1]))) / (-4.311704549797579 / (3.8872132896946994 + np.power(np.sqrt(x[0]), x[1])))))

#np.add(np.divide(np.divide(9.570811396234019, np.divide(3.2990756682061715, x[1])), 1.7120363063134838), np.multiply(np.divide(np.multiply(x[0], -0.342886656605085), 0.9853790256442974), 1.9959027865438197))
def f6(x: np.ndarray) -> np.ndarray: 
    return (((9.570811396234019 / (3.2990756682061715 / x[1])) / 1.7120363063134838) + (((x[0] * -0.342886656605085) / 0.9853790256442974) * 1.9959027865438197))

#np.subtract(np.power(np.power(np.square(np.subtract(x[1], x[0])), np.divide(x[0], -5.56363914354592)), np.add(x[0], 0.09503004875559984)), np.divide(np.multiply(0.5529900399168103, np.absolute(np.multiply(x[1], x[0]))), np.add(-1.0085421764494056, np.cos(np.subtract(x[1], x[0])))))
def f7(x: np.ndarray) -> np.ndarray:
    return (np.power(np.power(np.square((x[1] - x[0])), (x[0] / -5.56363914354592)), (x[0] + 0.09503004875559984)) - ((0.5529900399168103 * np.absolute((x[1] * x[0]))) / (-1.0085421764494056 + np.cos((x[1] - x[0])))))

#np.add(np.add(np.divide(np.subtract(-7540.826857026908, np.multiply(np.divide(x[1], 8.805913543617692), np.subtract(x[0], x[2]))), np.multiply(np.multiply(-19.741842726315273, np.exp(x[5])), -3.985603633378034)), np.add(np.multiply(np.multiply(np.square(x[5]), -32.50461510432733), -1.6711840162616087), np.subtract(np.divide(-18.279198870917952, np.exp(x[4])), np.add(np.multiply(x[3], -19.98753306315633), np.multiply(x[5], 19.966935689922764))))), np.add(np.multiply(np.subtract(x[5], np.power(0.9495060041270773, np.exp(x[5]))), np.subtract(np.multiply(np.square(x[5]), np.square(x[5])), np.multiply(-16.345502872293693, np.exp(x[5])))), np.subtract(np.divide(np.add(np.multiply(x[5], 19.966935689922764), np.multiply(x[5], 19.966935689922764)), -0.3773407102695644), np.subtract(np.multiply(np.exp(x[4]), 18.439101242496115), np.subtract(124.00906935452382, np.multiply(x[3], -19.98753306315633))))))
def f8(x: np.ndarray) -> np.ndarray: 
    return ((((-7540.826857026908 - ((x[1] / 8.805913543617692) * (x[0] - x[2]))) / ((-19.741842726315273 * np.exp(x[5])) * -3.985603633378034)) + (((np.square(x[5]) * -32.50461510432733) * -1.6711840162616087) + ((-18.279198870917952 / np.exp(x[4])) - ((x[3] * -19.98753306315633) + (x[5] * 19.966935689922764))))) + (((x[5] - np.power(0.9495060041270773, np.exp(x[5]))) * ((np.square(x[5]) * np.square(x[5])) - (-16.345502872293693 * np.exp(x[5])))) + ((((x[5] * 19.966935689922764) + (x[5] * 19.966935689922764)) / -0.3773407102695644) - ((np.exp(x[4]) * 18.439101242496115) - (124.00906935452382 - (x[3] * -19.98753306315633))))))
