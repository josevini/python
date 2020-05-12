dis = float(input('Uma distância em metros: '))
km = dis * 0.001
hm = dis * 0.01
dam = dis * 0.1
dm = dis * 10
cm = dis * 100
mm = dis * 1000
print("""A medida de {:.2f} corresponde a:
{}Km
{}hm
{:.1f}dam
{:.0f}dm
{:.0f}cm
{:.0f}mm""".format(dis, km, hm, dam, dm, cm, mm))
