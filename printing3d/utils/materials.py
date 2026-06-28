DENSITY={
'PLA':1.24,'PLA+':1.25,'PETG':1.27,'ABS':1.04,'TPU':1.21
}
def estimate_weight(volume_cm3,material='PLA'):
    return volume_cm3*DENSITY.get(material,1.24)
