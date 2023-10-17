from datetime import date, timedelta
from Lab.tipos.Fechas import Fecha

fecha1 = Fecha.of(2023, 3, 17)
date1 = date(2023,3, 17)



def test_nombre_mes(nombre_mes):
    print('Test_nombre_mes:')
    print ('Mes de',fecha1,':',fecha1.nombre_mes)
    mesdate1=date1.strftime('%B')
    print ('Mes de',date1,':',mesdate1)

def test_dia_semana(dia_semana):
    print('Test_dia_semana:')
    print ('Dia de',fecha1,':',fecha1.dia_semana)
    semanadate1=date1.strftime('%A')
    print (f'Semana de {date1}:{semanadate1}')
    
    
def test_sumar_dias(sumar_dias):
    print("test_sumar_dias: ")
    fecha2 = fecha1.sumar_dias(121)
    print(fecha1," + 121 días: ",fecha2)
    date2 = date1+timedelta(121)
    print(date1," + 121 días: ",date2)


def test_restar_dias(restar_dias):
    print("test_restar_dias: ")
    fecha2 = fecha1.restar_dias(121)
    print(fecha1," - 121 días: ",fecha2)
    date2 = date1-timedelta(121)
    print(date1," - 121 días: ",date2)

def test_diferencia_dias(diferencia_en_dias):
    print("test_diferencias_en_dias: ")
    fecha2 = Fecha.of(2023,3,31)
    diferencia=Fecha.diferencia_en_dias(fecha1,fecha2)
    print(f'{fecha1}-{fecha2}:{diferencia}')
    date2 = date(2023,  3,31)
    print(f'{date1}-{date2}:{abs(date1-date2).days}')
    
    
    
if __name__ == '__main__':
#
    test_nombre_mes(Fecha)
    test_dia_semana(Fecha)
    test_sumar_dias(Fecha) 
    test_restar_dias(Fecha)
    test_diferencia_dias(Fecha)