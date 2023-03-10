import numpy as np

def rebar_convert(size):
    return {
        '#3': '#3',
        '#4': '#4',
        '#5': '#5',
        '#6': '#6',
        '#7': '#7',
        'DEF #3': '#3',
        'DEF #4': '#4',
        'DEF #5': '#5',
        'DEF #6': '#6',
        'DEF #7': '#7',
        '#3"': '#3',
        '#4"': '#4',
        '#5"': '#5',
        '#6"': '#6',
        '#7"': '#7',
        '10mm': '#3',
        '13mm': '#4',
        '15mm': '#5',
        '16mm': '#5',
        '10 mm': '#3',
        '13 mm': '#4',
        '15 mm': '#5',
        '16 mm': '#5',
        '10MM': '#3',
        '13MM': '#4',
        '15MM': '#5',
        '16MM': '#5',
        '10 MM': '#3',
        '13 MM': '#4',
        '15 MM': '#5',
        '16 MM': '#5',
        'DEF 10': '#3',
        'DEF 13': '#4',
        'DEF 15': '#5',
        'DEF 16': '#5'
        }.get(size, np.nan)

def rebar_to_dec_str(size):
    'Clean up rebar size then convert'
    return {
        '#3': '0.375',
        '#4': '0.500',
        '#5': '0.625',
        '#6': '0.750',
    }.get(rebar_convert(size), np.nan)

#%% Size conversions
def frac_to_dec(fraction):
    #try:
    return {
        '5.5mm': 0.21875,
        '5.5mm"': 0.21875,
        '5.5MM': 0.21875,
        '5.5MM"': 0.21875,
        '5.5 mm': 0.21875,
        '5.5 mm"': 0.21875,
        '5.5 MM': 0.21875,
        '5.5 MM"': 0.21875,
        '1/64': 0.015625,
        '1/32': 0.03125,
        '3/64': 0.046875,
        '1/16': 0.0625,
        '5/64': 0.078125,
        '3/32': 0.09375,
        '7/64': 0.109375,
        '1/8': 0.125,
        '9/64': 0.140625,
        '5/32': 0.15625,
        '11/64': 0.171875,
        '3/16': 0.1875,
        '13/64': 0.203125,
        '7/32': 0.21875,
        '15/64': 0.234375,
        '1/4': 0.25,
        '17/64': 0.265625,
        '9/32': 0.28125,
        '19/64': 0.296875,
        '5/16': 0.3125,
        '21/64': 0.328125,
        '11/32': 0.34375,
        '23/64': 0.359375,
        '3/8': 0.375,
        '25/64': 0.390625,
        '13/32': 0.40625,
        '27/64': 0.421875,
        '7/16': 0.4375,
        '29/64': 0.453125,
        '15/32': 0.46875,
        '31/64': 0.484375,
        '1/2': 0.5,
        '33/64': 0.515625,
        '17/32': 0.53125,
        '35/64': 0.546875,
        '9/16': 0.5625,
        '37/64': 0.578125,
        '19/32': 0.59375,
        '39/64': 0.609375,
        '5/8': 0.625,
        '41/64': 0.640625,
        '21/32': 0.65625,
        '43/64': 0.671875,
        '11/16': 0.6875,
        '45/64': 0.703125,
        '23/32': 0.71875,
        '47/64': 0.734375,
        '3/4': 0.75,
        '49/64': 0.765625,
        '25/32': 0.78125,
        '51/64': 0.796875,
        '13/16': 0.8125,
        '53/64': 0.828125,
        '27/32': 0.84375,
        '55/64': 0.859375,
        '7/8': 0.875,
        '57/64': 0.890625,
        '29/32': 0.90625,
        '59/64': 0.921875,
        '15/16': 0.9375,
        '61/64': 0.953125,
        '31/32': 0.96875,
        '63/64': 0.984375,
        '1/64"': 0.015625,
        '1/32"': 0.03125,
        '3/64"': 0.046875,
        '1/16"': 0.0625,
        '5/64"': 0.078125,
        '3/32"': 0.09375,
        '7/64"': 0.109375,
        '1/8"': 0.125,
        '9/64"': 0.140625,
        '5/32"': 0.15625,
        '11/64"': 0.171875,
        '3/16"': 0.1875,
        '13/64"': 0.203125,
        '7/32"': 0.21875,
        '15/64"': 0.234375,
        '1/4"': 0.25,
        '17/64"': 0.265625,
        '9/32"': 0.28125,
        '19/64"': 0.296875,
        '5/16"': 0.3125,
        '21/64"': 0.328125,
        '11/32"': 0.34375,
        '23/64"': 0.359375,
        '3/8"': 0.375,
        '25/64"': 0.390625,
        '13/32"': 0.40625,
        '27/64"': 0.421875,
        '7/16"': 0.4375,
        '29/64"': 0.453125,
        '15/32"': 0.46875,
        '31/64"': 0.484375,
        '1/2"': 0.5,
        '33/64"': 0.515625,
        '17/32"': 0.53125,
        '35/64"': 0.546875,
        '9/16"': 0.5625,
        '37/64"': 0.578125,
        '19/32"': 0.59375,
        '39/64"': 0.609375,
        '5/8"': 0.625,
        '41/64"': 0.640625,
        '21/32"': 0.65625,
        '43/64"': 0.671875,
        '11/16"': 0.6875,
        '45/64"': 0.703125,
        '23/32"': 0.71875,
        '47/64"': 0.734375,
        '3/4"': 0.75,
        '49/64"': 0.765625,
        '25/32"': 0.78125,
        '51/64"': 0.796875,
        '13/16"': 0.8125,
        '53/64"': 0.828125,
        '27/32"': 0.84375,
        '55/64"': 0.859375,
        '7/8"': 0.875,
        '57/64"': 0.890625,
        '29/32"': 0.90625,
        '59/64"': 0.921875,
        '15/16"': 0.9375,
        '61/64"': 0.953125,
        '31/32"': 0.96875,
        '63/64"': 0.984375
        }.get(fraction, np.nan)
    #except KeyError as e:
    #    raise KeyError("Fraction '{}' was not found in lookup".format(e))

def frac_to_dec_str(fraction):
    formatted = "{:0.3f}".format(frac_to_dec(fraction))
    if formatted == 'nan':
        return rebar_convert(fraction)
    else:
        return formatted

def frac_to_dec_nom(fraction):
    return float(frac_to_dec_str(fraction))

def dec_to_dec_str(dec):
    try:
        return {
            0.46875: '0.469',
            0.296875: '0.297',
            0.2165: '0.219',
            0.21875: '0.219',
            0.3125: '0.312',
            0.5: '0.500',
            0.4375: '0.438',
            0.34375: '0.344',
            0.28125: '0.281',
            0.5625: '0.562',
            0.40625: '0.406',
            0.6875: '0.688',
            0.469: '0.469',
            0.375: '0.375',
            0.297: '0.297',
            0.217: '0.219',
            0.219: '0.219',
            0.250: '0.250',
            0.312: '0.312',
            0.313: '0.312',
            0.438: '0.438',
            0.344: '0.344',
            0.281: '0.281',
            0.562: '0.562',
            0.625: '0.625',
            0.406: '0.406',
            0.688: '0.688',
            }.get(dec, np.NaN)
    except KeyError as e:
        raise KeyError("Decimal '{}' was not found in lookup".format(e))

def dec_to_frac(dec):
    try:
        return {
            0.46875: '15/32"',
            0.375: '3/8"',
            0.296875: '19/64"',
            0.2165: '5.5mm',
            0.21875: '7/32"',
            0.25: '1/4"',
            0.3125: '5/16"',
            0.5: '1/2"',
            0.4375: '7/16"',
            0.34375: '11/32"',
            0.28125: '9/32"',
            0.5625: '9/16"',
            0.625: '5/8"',
            0.40625: '13/32"',
            0.6875: '11/16"',
        }[dec]
    except KeyError as e:
        raise KeyError("Fractional '{}' was not found in lookup".format(e))

def size_to_num_stand(size):
    try:
        return {
            '15/32"': 6,
            '3/8"': 8,
            '19/64"': 8,
            '5.5mm': 10,
            '7/32"': 10,
            '1/4"': 10,
            '5/16"': 8,
            '1/2"': 4,
            '7/16"': 6,
            '17/32"': 4,
            '11/32"': 8,
            '9/32"': 10,
            '9/16"': 4,
            '5/8"': 2,
            '3/4"': 2,
            '13/32"': 6,
            '11/16"': 2,
            '15/32': 6,
            '3/8': 8,
            '19/64': 8,
            '5.5': 10,
            '7/32': 10,
            '17/32': 4,
            '1/4': 10,
            '5/16': 8,
            '1/2': 4,
            '7/16': 6,
            '11/32': 8,
            '9/32': 10,
            '9/16': 4,
            '5/8': 2,
            '3/4': 2,
            '13/32': 6,
            '11/16': 2}[size]
    except KeyError as e:
        raise KeyError("Size '{}' was not found in lookup".format(e))

def alpha_to_frac(size):
    try:
        return {
            'A': '7/32"',
            'B': '1/4"',
            'C': '9/32"',
            'D': '5/16"',
            'E': '11/32"',
            'F': '3/8"',
            'G': '13/32"',
            'H': '7/16"',
            'I': '15/32"',
            'J': '1/2"',
            #'K': ,
            'L': '9/16"',
            #'M': ,
            'N': '5/8"',
            #'O': ,
            'P': '11/16"',
            #'Q':
            'R': '3/4"'
        }[size]
    except KeyError as e:
        raise KeyError(f"Size {e} as not found in lookup")

if __name__ == "__main__":
    from fractions import Fraction
    a = dict(
        [('{}/{}'.format(Fraction(i, 64).numerator,
            Fraction(i, 64).denominator), eval('{}/64'.format(i)))
            for i in range(1, 64)] +
        [('{}/{}"'.format(Fraction(i, 64).numerator,
            Fraction(i, 64).denominator), eval('{}/64'.format(i))) 
            for i in range(1, 64)]
    )
    b = dict(zip(a.values(), a.keys()))

# %%
