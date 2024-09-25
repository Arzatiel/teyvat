'''
final_de_semana = ['sábado', 'domingo']
ingresso = 15
final de semana com chuva terá acrescimento de 10%
final de semana sem chuva terá acréscimo de 50%
dia de semana com chuva terá desconto de 10%
dia de semana sem chuva terá preço normal
'''

fds = ['sábado', 'domingo']
ing = 15
fds_c_chuva = 15 + (15 * 0.1)
fds_s_chuva = 15 + (15 * 0.5)
dds_c_chuva = 15 - (15 * 0.1)

dia = input("Diga o dia: ")
chuva = input("Estará chovendo? ")
if dia in fds and chuva == 'sim':
    print(f"O ingresso custará {fds_c_chuva} reais.")
elif dia in fds and chuva == 'não':
    print(f"O ingresso custará {fds_s_chuva} reais.")
elif dia not in fds and chuva == 'sim':
    print(f"O ingresso custará {dds_c_chuva} reais.")
else:
    print(f"O ingresso custará {ing} reais.")