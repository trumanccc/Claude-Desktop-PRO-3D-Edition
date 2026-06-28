
from printing3d.utils.materials import estimate_weight

def estimate(volume_cm3,material='PLA',price_per_kg=20.0):
    grams=estimate_weight(volume_cm3,material)
    cost=(grams/1000.0)*price_per_kg
    return {
        'weight_g':round(grams,2),
        'cost':round(cost,2)
    }
