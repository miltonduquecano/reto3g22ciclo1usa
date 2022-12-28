PEDALIER_MIN=240
PEDALIER_MAX=300
BIELAS_MIN=160
BIELAS_MAX=180
SILLIN_MIN=240
SILLIN_MAX=275
MANILAR_MAX=50
baseDatos=[]
salida=[]
cumple=False
cantidadLineas = int(input())
for i in range(cantidadLineas):
    linea = input().split(" ")
    baseDatos.append(linea)
i=1
for pedalier,bielas,sillin,manilar,precio in baseDatos:
    pedalier=int(pedalier)
    bielas=int(bielas)
    sillin=int(sillin)
    manilar=int(manilar)
    precio=int(precio)
    i+=1
    if (pedalier >= PEDALIER_MIN and pedalier <= PEDALIER_MAX) and \
       (bielas >= BIELAS_MIN and bielas<= BIELAS_MAX) and \
        (sillin >= SILLIN_MIN and sillin <=SILLIN_MAX) and \
        (manilar <= MANILAR_MAX):
        cumple=True
        salida.append(precio)
if cumple:
    for precio in salida:
        print(precio)
else:
    print("NO DISPONIBLE")